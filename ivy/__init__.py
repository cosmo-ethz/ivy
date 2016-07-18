__author__ = 'Joel Akeret'
__email__ = 'jakeret@phys.ethz.ch'
__version__ = '0.1.0'
__credits__ = 'ETH Zurich, Institute for Astronomy'

#register custom reduce method for type MethodType
import copy_reg
import types
def reduce_method(m):
    return (getattr, (m.__self__, m.__func__.__name__))

copy_reg.pickle(types.MethodType, reduce_method)

from ivy import context
from ivy.workflow_manager import WorkflowManager

from ivy.workflow_manager import loadConfigs

def execute(args):
    """
    Runs a workflow for the given arguments.
    :param args: list of arguments which should be passed to ivy. The last argument has to be the config
    
    :returns: the global_ctx
    """
    mgr = WorkflowManager(args)
    mgr.launch()
    return context.global_ctx