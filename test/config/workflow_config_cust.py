# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 5, 2014

author: jakeret
'''
from ivy.config import base_config

context_provider = "ivy.context_provider.PickleContextProvider"

ctx_file_name = "le_cxt.dump"

plugins = ["test.plugin.simple_plugin"]
