# Copyright (C) 2014 ETH Zurich, Institute for Astronomy

"""
Tests for `ivy.context_provider` module.

author: jakeret
"""
from __future__ import print_function, division, absolute_import, unicode_literals
import pytest

from ivy.workflow_manager import WorkflowManager
from ivy.context import ctx

from ivy.context_provider import PickleContextProvider
from ivy import context
import os
from test.ctx_sensitive_test import ContextSensitiveTest
from ivy.context_provider import DefaultContextProvider
from ivy.utils.struct import Struct
from ivy.utils.struct import ImmutableStruct

class TestContextProvider(ContextSensitiveTest):


    def test_create_ctx(self):
        ctx = DefaultContextProvider.createContext()
        assert isinstance(ctx, Struct)

        ctx = DefaultContextProvider.createContext(a=3)
        assert isinstance(ctx, Struct)
        assert ctx.a == 3

        args = {"a":3}
        ctx = DefaultContextProvider.createContext(**args)
        assert isinstance(ctx, Struct)
        assert ctx.a == 3

    def test_create_immu_ctx(self):
        ctx = DefaultContextProvider.createImmutableContext()
        assert isinstance(ctx, ImmutableStruct)

        ctx = DefaultContextProvider.createImmutableContext(a=3)
        assert isinstance(ctx, ImmutableStruct)
        assert ctx.a == 3

        args = {"a":3}
        ctx = DefaultContextProvider.createImmutableContext(**args)
        assert isinstance(ctx, ImmutableStruct)
        assert ctx.a == 3


class TestPickleContextProvider(ContextSensitiveTest):


    def test_cust_ctx_provider(self):
        context.global_ctx = None
        args = ["test.config.workflow_config_cust"]
        
        mgr = WorkflowManager(args)
        mgr.launch()
        
        assert ctx() is not None
        from ivy.context import getContextProvider
        assert getContextProvider() == PickleContextProvider

    def test_storeContext(self, tmpdir):
        path = str(tmpdir.join("le_ctx"))
        ctx().ctx_file_name = path
        PickleContextProvider.storeContext()
        assert os.path.exists(path)

    def teardown(self):
        #tidy up
        print("tearing down " + __name__)
        context.global_ctx = None
    
    
if __name__ == '__main__':
    pytest.main()