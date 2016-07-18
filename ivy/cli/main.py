# Copyright (c) 2013 ETH Zurich, Institute for Astronomy

'''
Main executable to run ivy from CLI.

author: L. Gamper, J. Akeret

'''
import sys
from ivy.workflow_manager import WorkflowManager

def run():
    """
    Called by the entry point script. Delegating call to main()
    """
    _main(*sys.argv[1:])

def _main(*argv):
    
    if(argv is None or len(argv)<1):
        _usage()
        return
    argv = list(argv)
    mgr = WorkflowManager(argv)
    mgr.launch()

def _usage():
    """
    Return usage of the main ivy call and an example.
    """
    
    usage = """
    **Ivy workflow engine**
    Copyright (c) 2014 ETH Zurich, Institute for Astronomy
    
    Usage:
    ivy [arguments] configuration
    
    Only arguments already preconfigured in the given configuration will be accepted.
    Note: Dashed '-' will be converted into underlines '_' for all the arguments
    
    example:
    - ivy --size-x=100 --size-y=100 ufig.config.random
    """
    print usage
    
if __name__ == "__main__":
    _main(*sys.argv[1:])
