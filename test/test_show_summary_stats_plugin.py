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
