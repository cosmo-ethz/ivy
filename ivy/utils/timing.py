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
Created on Jul 15, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals
from collections import OrderedDict

class SimpleTiming(object):
    '''
    classdocs
    '''
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
    
    def __str__(self):
        return "{0!s:30}: {1:>7.3f}s".format(self.name, self.duration)
    
class TimingCollection(SimpleTiming):
    
    def __init__(self, parent):
        super(TimingCollection, self).__init__(parent, 0)
        self.timings = OrderedDict()
        

    def addTiming(self, timing):
        try:
            self.timings[timing.name].append(timing.duration)
        except KeyError:
            self.timings[timing.name] = [timing.duration]
        
    def __str__(self):
        s = ""
#         s+= "{0!s:30}: {1:>7.3f} s".format(self.name, self.duration)
        for name, durations in self.timings.items():
            s+= "   {0!s:30}({1}): mean:{2:>7.3f}s sum:{3:>7.3f}s min:{4:>7.3f}s max:{5:>7.3f}s\n".format(name,
                                                                                                         len(durations), 
                                                                                                          sum(durations)/len(durations), 
                                                                                                          sum(durations), 
                                                                                                          min(durations), 
                                                                                                          max(durations))
            
        return s
