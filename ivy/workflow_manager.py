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

from getopt import getopt
import importlib
import types

from ivy.exceptions.exceptions import InvalidAttributeException
from ivy.context import ctx
from ivy.utils.utils import TYPE_MAP
from ivy.loop import Loop
from ivy import context
from ivy.utils.struct import Struct
from ivy.backend import SequentialBackend

PLUGINS_KEY = "plugins"
CONTEXT_PROVIDER_KEY = "context_provider"

class WorkflowManager(object):
    '''
    Manages the workflow process by loading the passed config and 
    parsing the passed arguments and then iterating thru the plugins.
    
    :param argv: arguments to use
    '''


    def __init__(self, argv):
        '''
        Constructor
        '''
        self._setup(argv)
        
    def _setup(self, argv):
        config = self._parseArgs(argv)
        
        if not config.has_key(PLUGINS_KEY):
            raise InvalidAttributeException("plugins definition is missing")
        
        if config.has_key(CONTEXT_PROVIDER_KEY):
            def getContextProviderWrapper():
                #todo load class not module
                clazz = config[CONTEXT_PROVIDER_KEY]
                moduleName = ".".join(clazz.split(".")[:-1])
                module = importlib.import_module(moduleName)
                return getattr(module, clazz.split(".")[-1])
            context.getContextProvider = getContextProviderWrapper
        
        if not isinstance(config[PLUGINS_KEY], Loop):
            config[PLUGINS_KEY] = Loop(config[PLUGINS_KEY])
            
        ctx().params = context._createImmutableCtx(**config)
        #just to maintain backward compatibility
        ctx().parameters = ctx().params
        ctx().plugins = ctx().params.plugins
        
    def _parseArgs(self, argv):
        if(argv is None or len(argv)<1):
            raise InvalidAttributeException()
        
        if isinstance(argv, dict):
            return Struct(**argv)
        else:
            config = loadConfigs(argv[-1])
        
        # overwrite parameters by command line options
        optlist, positional = getopt(argv, '', [name.replace('_', '-') + '=' for name in config.keys()])
        if len(positional) != 1:
            raise InvalidAttributeException('only one config file is allowed')
        for opt in optlist:
            if opt[0][:2] != '--':
                raise InvalidAttributeException('invalid option name: {:}'.format(opt[0]))
            elif not opt[0][2:].replace('-', '_') in config:
                raise InvalidAttributeException('unknown option: {:}'.format(opt[0][2:]))
            else:
                name = opt[0][2:].replace('-', '_')
                config[name] = TYPE_MAP[type(config[name]).__name__](opt[1])
                
        return config
        
        
    def launch(self):
        """
        Launches the workflow
        """
        
        ctx().timings = []
        executor = SequentialBackend(ctx())
        executor.run(ctx().params.plugins)
    

def loadConfigs(configs):
    """
    Loads key-value configurations from Python modules.
    
    :param configs: string or list of strings with absolute module declaration e.g. "ivy.config.base_config
    
    :return config: a :py:class:`Struct` instance with the config attributes
    """
    if configs is None:
        raise InvalidAttributeException('Invalid configuration passed')
    
    if not isinstance(configs, list):
        configs = [configs]
        
    if len(configs) < 1:
        raise InvalidAttributeException('Invalid configuration passed')
            
    args = {}
    for configName in configs:
        config = importlib.import_module(configName)
        
        attrs = []
        for name in dir(config):
            if not name.startswith("__"):
                attr = getattr(config, name)
                if not isinstance(attr, types.ModuleType):
                    attrs.append((name, attr) )
        
        args.update(attrs)
        
    return Struct(**args)
