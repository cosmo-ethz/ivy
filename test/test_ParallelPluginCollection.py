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

 
"""
Tests for `ivy.plugin.parallel_plugin_collection ` module.
 
author: jakeret
"""
from __future__ import print_function, division, absolute_import, unicode_literals
 
import pytest
 
from ivy.plugin.parallel_plugin_collection import ParallelPluginCollection
from ivy import context
from ivy.workflow_manager import WorkflowManager
from ivy.context import ctx
from test.ctx_sensitive_test import ContextSensitiveTest
from test.plugin import range_map_plugin
from test.plugin import sum_reduce_plugin
from ivy.exceptions.exceptions import InvalidLoopException
from ivy.exceptions.exceptions import InvalidAttributeException
 
PLUGIN_NAME = "test.plugin.simple_square_plugin"
 
class TestParallelPluginCollection(ContextSensitiveTest):
  
    def test_setup(self):
        try:
            ParallelPluginCollection(None, "test.plugin.range_map_plugin")
            pytest.fail("No list provided")
        except InvalidLoopException:
            assert True
            
        try:
            ParallelPluginCollection([], None)
            pytest.fail("No map plugin provided")
        except InvalidAttributeException:
            assert True

    def test_sequential(self):
        ctx = context.ctx()
        ctx.timings = []
        ctx.params = context._createImmutableCtx(backend="sequential",
                                                 valuesMin = 1,
                                                 valuesMax = 10)
          
            
        mapPlugin = range_map_plugin.Plugin(ctx)
        pluginList = [PLUGIN_NAME]
        reducePlugin = sum_reduce_plugin.Plugin(ctx)
            
        parallelPluginCollection = ParallelPluginCollection(pluginList, mapPlugin, reducePlugin)
        parallelPluginCollection()
        assert ctx.valuesSum == 285
          
    def test_multiprocessing(self):
        ctx = context.ctx()
        ctx.timings = []
        ctx.params = context._createImmutableCtx(backend="multiprocessing",
                                                 cpu_count=8,
                                                 valuesMin = 1,
                                                 valuesMax = 10)
            
        mapPlugin = range_map_plugin.Plugin(ctx)
        pluginList = [PLUGIN_NAME]
        reducePlugin = sum_reduce_plugin.Plugin(ctx)
            
        parallelPluginCollection = ParallelPluginCollection(pluginList, mapPlugin, reducePlugin)
        parallelPluginCollection()
        assert ctx.valuesSum == 285
#     
    def test_parallel_workflow(self):
        args = ["--backend=multiprocessing",
                "--cpu-count=1",
                "test.config.workflow_config_parallel"]
          
        mgr = WorkflowManager(args)
        mgr.launch()
        assert ctx().valuesSum == 285

    
    def teardown(self):
        #tidy up
        print("tearing down " + __name__)
        pass
      
      
if __name__ == '__main__':
#     pytest.main()
    test = TestParallelPluginCollection()
    test.test_sequential()
    
