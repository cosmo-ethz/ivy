# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

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
