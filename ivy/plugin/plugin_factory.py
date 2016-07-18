# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 5, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals
from ivy.exceptions.exceptions import UnsupportedPluginTypeException
import importlib


class PluginFactory(object):
    """
    Simple factory creating instances of plugins
    """

    @staticmethod
    def createInstance(pluginName, ctx):
        """
        Instantiates the given plugin. Expects that the given module contains a class
        
        with the name 'Plugin'
        
        :param pluginName: name of the plugin to instanciate
        
        :return plugin: an instance of the plugin
        
        :raises: UnsupportedPluginTypeException
        """
        try:
            module = importlib.import_module(pluginName)
            plugin = module.Plugin(ctx)
            return plugin
        except ImportError as ex:
            raise UnsupportedPluginTypeException("Module '%s' could not be loaded" % pluginName, ex)
        except AttributeError as ex:
#             print("Module '%s' has no class definition 'Plugin'" % pluginName)
#             print("Old skool 'plugin' is deprecated! Adapt your implementation")
#             try:
#                 plugin = module.plugin()
#                 return plugin
#             except AttributeError:
                raise UnsupportedPluginTypeException("Module '%s' has no class definition 'Plugin(ctx)'" % pluginName)
            
        except Exception as ex:
            raise UnsupportedPluginTypeException("Module '%s' could not be instantiated'" % pluginName, ex)
        