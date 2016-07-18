# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 4, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals

from abc import ABCMeta, abstractmethod
from ivy.context import loopCtx
from ivy.utils.struct import WorkflowState
from ivy.exceptions.exceptions import InvalidAttributeException

class StopCriteria(object):
    """
    Abstract implementation of stopping criteria
    """
    
    __metaclass__ = ABCMeta
    
    parent = None
    
    @abstractmethod
    def isStop(self):
        pass

class RangeStopCriteria(StopCriteria):
    """
    Stopping criteria which stops after `maxIter` iterations
    """
    
    def __init__(self, maxIter):
        if maxIter < 1:
            raise InvalidAttributeException("Minimum iteration is 1")
        
        self.maxIter = maxIter
        
    def isStop(self):
        ctx = loopCtx(self.parent)
        if(ctx.iter >= self.maxIter):
            ctx.stop()
            
        return ctx.state == WorkflowState.STOP
    
class SimpleStopCriteria(RangeStopCriteria):
    """
    Simple implementation of a stopping criteria. Stops after `one` iteration
    """
    
    def __init__(self):
        super(SimpleStopCriteria, self).__init__(maxIter = 1)


    