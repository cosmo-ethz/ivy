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
Created on Mar 4, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals

from ivy import context
from ivy.context import loopCtx
from ivy.exceptions.exceptions import InvalidLoopException
from ivy.exceptions.exceptions import UnsupportedPluginTypeException
from ivy.plugin.base_plugin import BasePlugin
from ivy.plugin.plugin_factory import PluginFactory
from ivy.utils.stop_criteria import SimpleStopCriteria
from ivy.utils.struct import WorkflowState
from ivy.utils.utils import ListIter

class Loop(object):
    '''
    Implementation of a loop. 
    
    :param pluginList: List of plugin or inner :class:`Loop`
    :param stop: (optional) stop criteria
    '''
    
    _currentPlugin = None
    
    def __init__(self, pluginList, stop=None, ctx=None):

        if pluginList is None:
            raise InvalidLoopException("Plugin list is None")
        
        if not isinstance(pluginList, list):
            pluginList = [pluginList]
        
        self.pluginList = pluginList
        self._createIter()
        
        if stop is None:
            stop = self._createStopCriteria()
        
        stop.parent = self
        self._stopCriteria = stop
        context.register(self)
        if ctx is None:
            ctx = context.ctx()
        self.ctx = ctx
        
        
    def reset(self):
        """
        Resets the internal state of the loop
        """
        
        self.pluginListItr = ListIter(self.pluginList)
        loopCtx(self).reset()    
    
    def __iter__(self):
        return self
    
    def next(self):
        """
        Returns the next plugin. Allows for using a Loop as an iter
        """
        
        try:
            if(self._stopCriteria.isStop()):
                raise StopIteration
            
            if self._currentPlugin is None:
                self._currentPlugin = self.pluginListItr.next()
            
                plugin = self._currentPlugin
                if isinstance(plugin, BasePlugin):
                    self._currentPlugin = None
                    plugin.ctx = self.ctx
                    return plugin
                    
                if isinstance(plugin, basestring):
                    self._currentPlugin = None
                    return self._instantiate(plugin)
            
            if isinstance(self._currentPlugin, Loop):
                innerLoop = self._currentPlugin
                try:
                    plugin = innerLoop.next()
                    return plugin
                except StopIteration:
                    if(loopCtx(innerLoop).state == WorkflowState.EXIT):
                        raise StopIteration
                    #inner
                    loopCtx(innerLoop).reset()
                    self._currentPlugin = None
                    return self.next()
            else:
                raise UnsupportedPluginTypeException()
        except StopIteration:
            loopCtx(self).increment()
            self._createIter()

            if(self._stopCriteria.isStop()):
                raise StopIteration
            else:
                return self.next()
    
    def __call__(self):
        """
        Executes all the plugins sequentially in the loop
        """
        for plugin in self:
            plugin() 
    
    def  __setstate__(self, state):
        self.__dict__ = state
        context.register(self)
        
    def _createStopCriteria(self):
        return SimpleStopCriteria()
    

    def _instantiate(self, pluginName):
        return PluginFactory.createInstance(pluginName, self.ctx)

    def _loadIter(self):
        if self.pluginListItr is None:
            self._createIter()

    def _createIter(self):
        self.pluginListItr = ListIter(self.pluginList)


