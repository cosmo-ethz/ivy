# IVY is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# IVY is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with IVY.  If not, see <http://www.gnu.org/licenses/>.


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


    