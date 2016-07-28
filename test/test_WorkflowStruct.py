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
Tests for `ivy.WorkflowStruct` module.

author: jakeret
"""
from __future__ import print_function, division, absolute_import, unicode_literals
import pytest

from ivy.utils.struct import WorkflowStruct
from ivy.utils.struct import WorkflowState



class TestWorkflowStruct(object):


    def test_states(self):
        ctx = WorkflowStruct()
        
        assert ctx.state == WorkflowState.RUN
        ctx.stop()
        assert ctx.state == WorkflowState.STOP
        ctx.reset()
        assert ctx.state == WorkflowState.RUN
        ctx.exit()
        assert ctx.state == WorkflowState.EXIT
        ctx.reset()
        ctx.resume()
        assert ctx.state == WorkflowState.RESUME

    def test_iterator(self):
        ctx = WorkflowStruct()
        
        assert ctx.iter == 0
        ctx.increment()
        assert ctx.iter == 1

        
    def teardown(self):
        #tidy up
        print("tearing down " + __name__)
        pass
    
    
if __name__ == '__main__':
    pytest.main()