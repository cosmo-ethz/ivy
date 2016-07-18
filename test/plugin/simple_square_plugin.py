# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 5, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals
from ivy.plugin.base_plugin import BasePlugin


class Plugin(BasePlugin):
    '''
    Plugin that computes the square of ctx.value
    '''
    
    def __str__(self):
        return __name__
    
    def __call__(self):
        self.ctx.value = self.ctx.value**2
#         s = 0 
#         for i in range(10**3):
#             for j in range(10**3):
#                 s += i*j
