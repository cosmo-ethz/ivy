# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 18, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import
from ivy.plugin.base_plugin import BasePlugin
from ivy.loop import Loop
from ivy import context
from ivy.plugin.plugin_factory import PluginFactory
from ivy.exceptions.exceptions import InvalidAttributeException
from ivy import backend


class ParallelPluginCollection(BasePlugin):
    """
    Collection that allows for executing plugins in parallel by using
    a MapReduce aprach. The implementation therefore requires a
    list of plugins to execute, a map plugin creating the workload and 
    (optionally) a reduce plugin reducing the data from the parallel task exection
    
    :param pluginList: List of plugins (or a Loop) which should be executed in parallel
    :param mapPlugin: 
    :param reducePlugin: (optional)
    :param ctx: (optional) 
    """


    def __init__(self, pluginList, mapPlugin, reducePlugin=None, ctx=None, parallel=True):

        '''
        Constructor
        '''
        if ctx is None:
            ctx = context.ctx()
        self.ctx = ctx

        super(ParallelPluginCollection, self).__init__(self.ctx)
        
        if not isinstance(pluginList, Loop):
            pluginList = Loop(pluginList)
            
        self.pluginList = pluginList

        if mapPlugin is None:
            raise InvalidAttributeException("No map plugin provided")
        
        self.mapPlugin = mapPlugin
        self.reducePlugin = reducePlugin
        self.parallel = parallel
        

    def __str__(self):
        return "ParallelPluginCollection"
    
    def __call__(self):
        force = None
        if not self.parallel:
            force = "sequential"
            
        backendImpl = backend.create(self.ctx, force)
        
        mapPlugin = self.mapPlugin
        if isinstance(self.mapPlugin, basestring):
            mapPlugin = PluginFactory.createInstance(mapPlugin, self.ctx)
        
        ctxList = backendImpl.run(self.pluginList, mapPlugin)
       
        if self.reducePlugin is not None:
            reducePlugin = self.reducePlugin
            if isinstance(self.reducePlugin, basestring):
                reducePlugin = PluginFactory.createInstance(reducePlugin, self.ctx)
            
            reducePlugin.reduce(ctxList)
