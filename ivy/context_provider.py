# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 6, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals

from ivy.utils.struct import Struct
import pickle
from ivy.context import ctx
from ivy.utils.struct import ImmutableStruct


class DefaultContextProvider(object):
    """
    Default implementation of a context provider.
    Creates a simple mutable struct as ctx and doesn't
    persist the context.
    """
    
    @staticmethod
    def createContext(**args):
        """
        Returns a Struct
        """
        return Struct(**args)
    
    @staticmethod
    def createImmutableContext(**args):
        """
        Returns a Struct
        """
        return ImmutableStruct(**args)
    
    
    
    @staticmethod
    def storeContext():
        """
        Dummy method. Nothing is stored
        """
        pass
    
class PickleContextProvider(DefaultContextProvider):
    """
    Extends the DefaultContextProvider. 
    Persists the context to the disk by using pickle.
    Requires the attribute 'ctx_file_name' in the ctx 
    """
    
    @staticmethod
    def storeContext():
        """
        Writes the current ctx to the disk
        """
        fileName = ctx().ctx_file_name
        with open(fileName, "w") as ctxFile:
            pickle.dump(ctx(), ctxFile)
    
