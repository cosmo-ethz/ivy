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

from collections import MutableMapping
from ivy.exceptions.exceptions import IllegalAccessException
from ivy.utils.utils import Enum

# In Python 2.7 still, `DictMixin` is an old-style class; thus, we need
# to make `Struct` inherit from `object` otherwise we loose properties
# when setting/pickling/unpickling


class ImmutableStruct(MutableMapping):
    """
    A `dict`-like object, whose keys can be accessed with the usual
    '[...]' lookup syntax, or with the '.' get attribute syntax.

    Examples::

      >>> a = Struct()
      >>> a['x'] = 1
      >>> a.x
      1
      >>> a.y = 2
      >>> a['y']
      2

    Values can also be initially set by specifying them as keyword
    arguments to the constructor::

      >>> a = Struct(z=3)
      >>> a['z']
      3
      >>> a.z
      3

    Like `dict` instances, `Struct`s have a `copy` method to get a
    shallow copy of the instance:

      >>> b = a.copy()
      >>> b.z
      3

    """
    def __init__(self, initializer=None, **extra_args):
        if initializer is not None:
            try:
                # initializer is `dict`-like?
                for name, value in initializer.items():
                    self.__dict__[name] = value
            except AttributeError:
                # initializer is a sequence of (name,value) pairs?
                for name, value in initializer:
                    self.__dict__[name] = value
        for name, value in extra_args.items():
            self.__dict__[name] = value

    def copy(self):
        """Return a (shallow) copy of this `Struct` instance."""
        return ImmutableStruct(self)

    # the `DictMixin` class defines all std `dict` methods, provided
    # that `__getitem__`, `__setitem__` and `keys` are defined.
    def __setitem__(self, name, val):
        raise IllegalAccessException("Trying to modify immutable struct with: %s=%s"%(str(name), str(val)))
        
    def __getitem__(self, name):
        return self.__dict__[name]
    
    def keys(self):
        return self.__dict__.keys()
    
    def __str__(self):
        str = "{\n"
        for name, value in self.items():
            str += ("%s='%s'\n" %(name, value))
        str += "}"
        return str
        
    def __delitem__(self, name):
        del self.__dict__[name]
    
    def __iter__(self,):
        return iter(self.__dict__)
    
    def __len__(self,):
        return len(self.__dict__) 

class Struct(ImmutableStruct):
    """
    Mutable implementation of a Strcut
    """
    
    
    def __setitem__(self, name, val):
        self.__dict__[name] = val
        
    def copy(self):
        """Return a (shallow) copy of this `Struct` instance."""
        return Struct(self)        

WorkflowState = Enum(
                     "RUN",
                     "STOP",
                     "EXIT",
                     "RESUME")


class WorkflowStruct(ImmutableStruct):
    '''
    Struct representing the internal state of a workflow loop
    '''
    
    iter = 0
    
    state = WorkflowState.RUN
    
    def increment(self):
        self.iter += 1

    def reset(self):
        self.iter = 0
        self.state = WorkflowState.RUN

    def stop(self):
        self.state = WorkflowState.STOP
    
    def exit(self):
        self.state = WorkflowState.EXIT
    
    def resume(self):
        self.state = WorkflowState.RESUME
