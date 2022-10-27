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
Tests for `ivy.cli` module.

author: jakeret
"""
import pytest

from ivy import context
from ivy.cli.main import _main
from ivy.context import ctx
from test.ctx_sensitive_test import ContextSensitiveTest


class TestCli(ContextSensitiveTest):

    def test_launch_empty(self):
        _main(*[])
        assert context.global_ctx is None  # empty

    def test_launch_loop(self):
        _main(*["test.config.workflow_config_cli"])
        assert ctx() is not None
        assert ctx().params is not None
        assert ctx().params.plugins is not None
        assert len(ctx().timings) == 2

    def teardown(self):
        # tidy up
        print("tearing down " + __name__)
        pass


if __name__ == '__main__':
    pytest.main("-k TestCli")
