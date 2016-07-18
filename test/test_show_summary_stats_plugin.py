# Copyright (C) 2014 ETH Zurich, Institute for Astronomy

'''
Created on Jan 12, 2015

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals

from ivy.plugin import show_summary_stats
from ivy.utils.struct import Struct
from ivy.utils.timing import SimpleTiming
from ivy.utils.timing import TimingCollection

class TestShowSummaryStatsPlugin(object):
    
    def test_join_timings_one_element(self):
        ctx = Struct()
        timing = SimpleTiming("Test", 100)
        timings= TimingCollection(timing.name)
        timings.duration = timing.duration
        timings.addTiming(timing)
        
        plugin = show_summary_stats.Plugin(ctx)
        str_timing = plugin._join_timings(timings)
        
        assert str_timing == "Test                          : 100.000 s"
        
    def test_join_timings_two_element(self):
        ctx = Struct()
        timing = SimpleTiming("Test", 100)
        timings= TimingCollection(timing.name)
        timings.duration = timing.duration
        timings.addTiming(timing)
        timings.addTiming(timing)
        
        plugin = show_summary_stats.Plugin(ctx)
        str_timing = plugin._join_timings(timings)
        
        assert str_timing == "Test                    (   2): 200.000 s (mean: 100.00000s min: 100.00000s max: 100.00000s)"
        
    def test_reorder_timings(self):
        ctx = Struct()
        timing = SimpleTiming("Test", 100)
        timings = [timing]
        
        plugin = show_summary_stats.Plugin(ctx)
        timing_map = plugin._reorder_timings(timings)
        
        assert timing_map is not None
        assert timing_map["Test"] is not None
        
        timings.append(timing)
        timing_map = plugin._reorder_timings(timings)
        
        assert timing_map is not None
        assert timing_map["Test"] is not None
        assert isinstance(timing_map["Test"], TimingCollection)
        assert len(timing_map["Test"].timings["Test"]) == 2
