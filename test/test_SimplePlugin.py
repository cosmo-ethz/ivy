# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

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