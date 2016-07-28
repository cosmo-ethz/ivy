# IVY is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# IVY is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with IVY.  If not, see <http://www.gnu.org/licenses/>.


"""
Tests for `ivy.context` module.

author: jakeret
"""
from __future__ import print_function, division, absolute_import, unicode_literals
import pytest

from test.ctx_sensitive_test import ContextSensitiveTest
from ivy.loop import Loop
from ivy.context import register
from ivy.exceptions.exceptions import InvalidLoopException
from ivy.context import loopCtx
from ivy import context
from ivy.utils.struct import Struct
from ivy.utils.struct import ImmutableStruct

class TestContext(ContextSensitiveTest):


    def test_register(self):
        loop = Loop("plugin")
        try:
            register(loop)
            pytest.fail("Loop registered twice")
        except InvalidLoopException as ex:
            assert True

        lctx = loopCtx(loop)
        assert lctx is not None
        
        
    def test_create_ctx(self):
        ctx = context._createCtx()
        assert isinstance(ctx, Struct)

        ctx = context._createCtx(a=3)
        assert isinstance(ctx, Struct)
        assert ctx.a == 3

        args = {"a":3}
        ctx = context._createCtx(**args)
        assert isinstance(ctx, Struct)
        assert ctx.a == 3

    def test_create_immu_ctx(self):
        ctx = context._createImmutableCtx()
        assert isinstance(ctx, ImmutableStruct)

        ctx = context._createImmutableCtx(a=3)
        assert isinstance(ctx, ImmutableStruct)
        assert ctx.a == 3

        args = {"a":3}
        ctx = context._createImmutableCtx(**args)
        assert isinstance(ctx, ImmutableStruct)
        assert ctx.a == 3