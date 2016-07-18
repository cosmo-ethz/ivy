# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 5, 2014

author: jakeret
'''
from ivy.config import base_config
from ivy.loop import Loop

plugins = Loop(["test.plugin.simple_plugin",
                "test.plugin.simple_plugin"
                ])
