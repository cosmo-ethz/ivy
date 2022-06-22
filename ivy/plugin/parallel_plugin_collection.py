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
        if isinstance(self.mapPlugin, str):
            mapPlugin = PluginFactory.createInstance(mapPlugin, self.ctx)
        
        ctxList = backendImpl.run(self.pluginList, mapPlugin)
       
        if self.reducePlugin is not None:
            reducePlugin = self.reducePlugin
            if isinstance(self.reducePlugin, str):
                reducePlugin = PluginFactory.createInstance(reducePlugin, self.ctx)
            
            reducePlugin.reduce(ctxList)
