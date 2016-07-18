# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 18, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals


class Plugin(object):
    '''
    classdocs
    '''


    def __init__(self, ctx):
        '''
        Constructor
        '''
        self.ctx = ctx
    
    def reduce(self, ctxList):
        sum = 0
        for ctx in ctxList:
            sum += ctx.value
        
        self.ctx.valuesSum = sum