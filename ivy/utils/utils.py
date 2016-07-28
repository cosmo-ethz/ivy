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
Created on Mar 5, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals

TYPE_MAP = {
    'bool': lambda x: boolify(x),
    'int': lambda x: int(x),
    'long': lambda x: long(x),
    'float': lambda x: float(x),
    'str': lambda x: x,
    'unicode': lambda x: x,
    'list': lambda x: x.split(','),
    'NoneType': lambda x: inferType(x)
    
}

def boolify(s):
    if s == 'True' or s == 'true':
            return True
    if s == 'False' or s == 'false':
            return False
    raise ValueError('Not Boolean Value!')

def listify(s):
    if(s.count(",")<=0):
        raise ValueError()
    
    x = s.split(",")
    l = []
    for e in x:
        l.append(inferType(e))
    return l

def inferType(var):
    '''guesses the str representation of the variables type'''
    var = str(var) #important if the parameters aren't strings...
    for caster in (boolify, int, long, float, listify):
            try:
                    return caster(var)
            except ValueError:
                    pass
    return var
    
class Enum(frozenset):
    """
    A generic enumeration class.  Inspired by:
    http://stackoverflow.com/questions/36932/whats-the-best-way-to-implement-an-enum-in-python/2182437#2182437
    with some more syntactic sugar added.

    An `Enum` class must be instanciated with a list of strings, that
    make the enumeration "label"::

      >>> Animal = Enum('CAT', 'DOG')

    Each label is available as an instance attribute, evaluating to
    itself::

      >>> Animal.DOG
      'DOG'

      >>> Animal.CAT == 'CAT'
      True

    As a consequence, you can test for presence of an enumeration
    label by string value::

      >>> 'DOG' in Animal
      True

    Finally, enumeration labels can also be iterated upon::

      >>> for a in Animal: print a
      DOG
      CAT
    """
    def __new__(cls, *args):
        return frozenset.__new__(cls, args)
    def __getattr__(self, name):
            if name in self:
                    return name
            else:
                    raise AttributeError("No '%s' in enumeration '%s'"
                                         % (name, self.__class__.__name__))
    def __setattr__(self, name, value):
            raise SyntaxError("Cannot assign enumeration values.")
    def __delattr__(self, name):
            raise SyntaxError("Cannot delete enumeration values.")


class ListIter(object):
    """
    Simple list iterator which can be pickled
    
    :param list: the list over which should be iterated
    """
    
    def __init__(self, list):
        self.list = list
        self.idx = 0
        
    def __iter__(self):
        return self
    
    def next(self):
        if(self.idx < len(self.list)):
            item = self.list[self.idx]
            self.idx += 1
            return item
        
        raise StopIteration