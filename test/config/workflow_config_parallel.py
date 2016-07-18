# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 5, 2014

author: jakeret
'''
# from ivy.config import base_config
from ivy.plugin.parallel_plugin_collection import ParallelPluginCollection

backend = "sequential"
cpu_count = 1
valuesMin = 1
valuesMax = 10

plugins = ["test.plugin.simple_plugin",
           ParallelPluginCollection(
                                    ["test.plugin.simple_square_plugin"], 
                                    "test.plugin.range_map_plugin",
                                    "test.plugin.sum_reduce_plugin"),
            "test.plugin.simple_plugin"
            ]

