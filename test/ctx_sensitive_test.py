# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 11, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals
from ivy import context


class ContextSensitiveTest(object):
    '''
    Simple base class which resets the context after method execution
    '''


    def teardown_method(self, method):
        context.global_ctx = None
