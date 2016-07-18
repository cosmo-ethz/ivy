# Copyright (c) 2013 ETH Zurich, Institute for Astronomy

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
