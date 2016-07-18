# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

"""
Tests for `ivy.plugin.plugin_factory ` module.

author: jakeret
"""
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest

from ivy.exceptions.exceptions import UnsupportedPluginTypeException
from ivy.plugin.plugin_factory import PluginFactory
from ivy.context import ctx
from test.plugin import simple_plugin


PLUGIN_NAME = "test.plugin.simple_plugin"

class TestPluginFactory(object):


    def test_simple(self):
        plugin = PluginFactory.createInstance(PLUGIN_NAME, ctx())
        assert plugin is not None
        assert isinstance(plugin, simple_plugin.Plugin)

    def test_unknown_module(self):
        pluginName = "unknown.plugin.invalid"
        try:
            plugin = PluginFactory.createInstance(pluginName, ctx())
            pytest.fail("UnsupportedPluginTypeException expected", False)
            assert False
        except UnsupportedPluginTypeException as ex:
            assert True
        
    def test_invalid_module(self):
        pluginName = "ivy.plugin.BasePlugin"
        try:
            plugin = PluginFactory.createInstance(pluginName, ctx())
            pytest.fail("UnsupportedPluginTypeException expected", False)
            assert False
        except UnsupportedPluginTypeException as ex:
            assert True
        
    def teardown(self):
        #tidy up
        print("tearing down " + __name__)
        pass
    
    
if __name__ == '__main__':
    pytest.main()