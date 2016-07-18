# Copyright (c) 2013 ETH Zurich, Institute for Astronomy

'''
Tests for `ivy.utils` module.

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest

from ivy.exceptions.exceptions import IllegalAccessException
from ivy.utils.struct import ImmutableStruct
from ivy.utils.struct import Struct


class TestStruct(object):

    def test_struct(self):
        
        a = Struct()
        a['x'] = 1
        assert a.x == 1
        
        a.y = 2
        assert a['y'] == 2

    def test_init(self):
        a = Struct(z=3)
        assert a['z'] == 3
        assert a.z == 3

    def test_copy(self):
        a = Struct(z=3)
        b = a.copy()
        assert b.z == 3
        
        
    def test_immutableStruct(self):
        a = ImmutableStruct()
        try:
            a['x'] = 1
            pytest.fail("Not mutation allowd on immutable", False)
        except IllegalAccessException:
            assert True
            
