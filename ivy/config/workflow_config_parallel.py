# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''

author: jakeret
'''
# from ivy.config import base_config
from ivy.plugin.parallel_plugin_collection import ParallelPluginCollection

backend = "sequential"
cpu_count=1
valuesMin = 1
valuesMax = 16

plugins = ParallelPluginCollection(["ivy.plugin.simple_square_plugin"], 
                                    "ivy.plugin.range_map_plugin",
                                    "ivy.plugin.sum_reduce_plugin")
