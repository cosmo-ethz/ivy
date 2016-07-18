# Copyright (C) 2014 ETH Zurich, Institute for Astronomy

'''
Created on Jan 12, 2014
@author: Joel Akeret

'''
from __future__ import print_function, division, absolute_import, unicode_literals

from collections import OrderedDict
from ivy.utils.timing import TimingCollection

from ivy.plugin.base_plugin import BasePlugin
from ivy.plugin.parallel_plugin_collection import ParallelPluginCollection


class Plugin(BasePlugin):
    """
    Show statistics of time.
    """
    def __call__(self):
        keyword = ParallelPluginCollection([], 0, None).__str__()
        
        total = sum((timing.duration for timing in self.ctx.timings if timing.name is not keyword))
        print("== Ivy run took: {0:>7.3f} s ===".format(total))
        timing_map = self._reorder_timings(self.ctx.timings)
                
        for timing in timing_map.values():
            print(self._join_timings(timing))
    
    def _reorder_timings(self, timings):
        timing_map = OrderedDict()
        keyword = ParallelPluginCollection([], 0, None).__str__()
        for timing in timings:
            if timing.name is not keyword:
                try:
                    timing_map[timing.name].addTiming(timing)
                except KeyError:
                    timing_map[timing.name] = TimingCollection(timing.name)
                    timing_map[timing.name].duration = timing.duration
                    timing_map[timing.name].addTiming(timing)
        return timing_map
    
    def _join_timings(self, timing):
        s = ""
        if(len(timing.timings.values()[0])==1):
            s+= "{0!s:30}: {1:>7.3f} s".format(timing.name, timing.duration)
        else:    
            summary_list = []
            for name, durations in timing.timings.items():
                summary_list.append("{0!s:24}({1:>4d}): {3:>7.3f} s (mean: {2:>7.5f}s min: {4:>7.5f}s max: {5:>7.5f}s)".format(name,
                                                                                                             len(durations), 
                                                                                                              sum(durations)/len(durations), 
                                                                                                              sum(durations), 
                                                                                                              min(durations), 
                                                                                                              max(durations)))
            s += "\n".join(summary_list)
        return s

    def __str__(self):
        return "stat"
