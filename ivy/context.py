# Copyright 2013 ETHZ.ch Lukas Gamper <lukas.gamper@usystems.ch>
from ivy.exceptions.exceptions import InvalidLoopException
from ivy.utils.struct import WorkflowStruct

__all__ = ["ctx", "loopCtx"]

global_ctx = None

def ctx():
    """
    Returns the current global namespace context.
    
    :return: reference to the context module
    
    """
    global global_ctx
    if(global_ctx is None):
        global_ctx = _createCtx()
        
    return global_ctx

def register(loop):
    try:
        l = ctx()[loop]
        raise InvalidLoopException()
    except KeyError or AttributeError:
        ctx()[loop] = WorkflowStruct()

def loopCtx(loop):
    return ctx()[loop]

def _createCtx(**args):
    return getContextProvider().createContext(**args)

def _createImmutableCtx(**args):
    return getContextProvider().createImmutableContext(**args)

def getContextProvider():
    from ivy.context_provider import DefaultContextProvider
    return DefaultContextProvider

