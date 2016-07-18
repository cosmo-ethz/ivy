# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 5, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals
from ivy.plugin.base_plugin import BasePlugin


class Plugin(BasePlugin):
    '''
    Simple implementation of the BasePlugin
    '''
    
    def __init__(self, ctx, **kwargs):
        self.value = kwargs.pop("value", None)
        super(Plugin, self).__init__(ctx, **kwargs)
        
    def __str__(self):
        return __name__
    
    def __call__(self):
        if self.value is not None:
            print(self.value)
