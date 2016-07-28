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


'''
Tests for `ivy.stop_criteria` module.

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest
from ivy.utils.stop_criteria import RangeStopCriteria
from ivy.exceptions.exceptions import InvalidAttributeException
from ivy.loop import Loop
from ivy.context import loopCtx



class TestStopCriteria(object):

    def test_RangeStopCriteria(self):
        try:
            stopCriteria = RangeStopCriteria(0)
            pytest.fail("0 iterations not allowed")
        except InvalidAttributeException:
            assert True
            
        stopCriteria = RangeStopCriteria(1)
        loop = Loop("", stopCriteria)
        assert False == stopCriteria.isStop()
        
        loopCtx(loop).increment()
        assert True == stopCriteria.isStop()
