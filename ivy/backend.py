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
from __future__ import print_function, division, absolute_import, unicode_literals
from multiprocessing import Pool
import time
from ivy.context import getContextProvider
from ivy.utils.timing import SimpleTiming
from ivy.utils.timing import TimingCollection

class SimpleMapPlugin(object):
    
    def __init__(self, ctx):
        self.ctx = ctx
        
    def getWorkload(self):
        return [self.ctx]
    


class SequentialBackend(object):
    """
    Simple implementation of a backend executing the plugins in a sequential order
    """
    
    def __init__(self, ctx):
        self.ctx = ctx
    
    def run(self, loop, mapPlugin=None):
        if mapPlugin is None: mapPlugin=SimpleMapPlugin(self.ctx)
        
    loop_exe = []
        for workload in mapPlugin.getWorkload():
            loop_exe.append(LoopWrapper(loop)(workload))
        return loop_exe

class MultiprocessingBackend(object):
    """
    Backend based on Python's multiprocessing. 
    Will instantiate a multiprocessing pool with ``ctx.params.cpu_count`` processes.
    """
    
    def __init__(self, ctx):
        self.ctx = ctx
    
    def run(self, loop, mapPlugin):
        pool = Pool(self.ctx.params.cpu_count)
        try:
            ctxList = pool.map(LoopWrapper(loop, True), mapPlugin.getWorkload())
            timingCollection = TimingCollection(str(loop))
            for ctx in ctxList:
                for timing in ctx.timings:
                    timingCollection.addTiming(timing)
            self.ctx.timings.append(timingCollection)
            return ctxList
        finally:
            pool.close()
        
class IpClusterBackend(object):
    """
    Backend based on IPython cluster. 
    Will distribute the workload among the available engines.
    """
    
    def __init__(self, ctx):
        self.ctx = ctx
    
    def run(self, loop, mapPlugin):
        from IPython import parallel

        client = parallel.Client()
        view = client.load_balanced_view()
        try:
            return view.map_sync(LoopWrapper(loop), mapPlugin.getWorkload())
        finally:
            pass
#             view.close()

class JoblibBackend(object):
    """
    Backend based on the joblib package 
    Will instantiate a multiprocessing pool with ``ctx.params.cpu_count`` processes.
    """
    
    def __init__(self, ctx):
        self.ctx = ctx
    
    def run(self, loop, mapPlugin):
        import joblib
        with joblib.Parallel(n_jobs=self.ctx.params.cpu_count) as parallel:
            ctxList = parallel(joblib.delayed(LoopWrapper(loop, True), False)(ctx) for ctx in mapPlugin.getWorkload())
            timingCollection = TimingCollection(str(loop))
            for ctx in ctxList:
                for timing in ctx.timings:
                    timingCollection.addTiming(timing)
            self.ctx.timings.append(timingCollection)
            return ctxList
        


class LoopWrapper(object):
    """
    Callable wrapper for the loop execution
    """
    def __init__(self, loop, parallel=False):
        self.loop = loop
        self.parallel = parallel
    
    def __call__(self, ctx):
#         print("working pid:%s" %(os.getpid()))
        if self.parallel: ctx.timings = []
        self.loop.ctx = ctx
        for plugin in self.loop:
            start = time.time()
#             print("(%s, '%s'),"%(time.time(), plugin))
            plugin()
#             time.sleep(5)
            ctx.timings.append(SimpleTiming(str(plugin), time.time() - start))
                
            getContextProvider().storeContext()

#         self.loop()
        self.loop.reset()
        return ctx
            

BACKEND_NAME_MAP = {"sequential": SequentialBackend,
                    "multiprocessing": MultiprocessingBackend,
                    "ipcluster": IpClusterBackend,
                    "joblib": JoblibBackend,
                    }

def create(ctx, force=None):
    '''
    Simple factory instantiating backends for the given name in ``ctx.params.backend``
    '''
    backend_name = ctx.params.backend if force is None else force
    return BACKEND_NAME_MAP[backend_name](ctx)
