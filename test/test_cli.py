# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

"""
Tests for `ivy.cli` module.

author: jakeret
"""
import pytest

from ivy.context import ctx
from ivy.cli.main import _main
from ivy import context
from ctx_sensitive_test import ContextSensitiveTest

class TestCli(ContextSensitiveTest):


    def test_launch_empty(self):

        _main(*[])
        assert context.global_ctx is None #empty

    def test_launch_loop(self):
        _main(*["test.config.workflow_config_cli"])
        assert ctx() is not None
        assert ctx().params is not None
        assert ctx().params.plugins is not None
        assert len(ctx().timings)==2
        

        
    def teardown(self):
        #tidy up
        print("tearing down " + __name__)
        pass
    
    
if __name__ == '__main__':
    pytest.main("-k TestCli")