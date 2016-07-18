# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 4, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import

from abc import ABCMeta
from ivy.exceptions.exceptions import NotImplementedException

class BasePlugin(object):
    '''
    Abstract base class for all the plugins providing standardized
    interfaces
    '''
    __metaclass__ = ABCMeta

    def __init__(self, ctx, **kwargs):
        self.ctx = ctx
        self.ctx.update(kwargs)
        
    def __str__(self):
        raise NotImplementedException()

    def __call__(self):
        raise NotImplementedException()