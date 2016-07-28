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
Tests for `ivy.simple_plugin` module.

author: jakeret
"""
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest

from test.plugin.simple_plugin import Plugin
from ivy.context import ctx

class TestSimplePlugin(object):


    def test_simple(self):
        plugin = Plugin(ctx())
        assert plugin.value is None
        
        plugin = Plugin(ctx(), value=1)
        assert plugin.value == 1
        
        plugin = Plugin(ctx(), foo=1)
        assert ctx().foo == 1
        

    def teardown(self):
        #tidy up
        print("tearing down " + __name__)
        pass
    
    
if __name__ == '__main__':
    pytest.main()