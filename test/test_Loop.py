# Copyright (C) 2014 ETH Zurich, Institute for Astronomy

"""
Tests for `ivy.Loop` module.

author: jakeret
"""
from __future__ import print_function, division, absolute_import
import pytest

from ivy.loop import Loop
from ivy.exceptions.exceptions import InvalidLoopException
from test.plugin.simple_plugin import Plugin
from ivy.exceptions.exceptions import UnsupportedPluginTypeException
from ivy.context import loopCtx
from ivy.utils.stop_criteria import RangeStopCriteria
from test.ctx_sensitive_test import ContextSensitiveTest
from ivy.context import ctx

PLUGIN_NAME = "test.plugin.simple_plugin"


class TestLoop(ContextSensitiveTest):

    def setup(self):
        #prepare unit test. Load data etc
        pass

    def test_none(self):
        try:
            loop = Loop(None)
            assert False
        except InvalidLoopException:
            assert True
            
    def test_one_plugin(self):
        plugin = Plugin(ctx())
        loop = Loop(plugin)
        
        p = loop.next()
        assert p == plugin
        
        try:
            loop.next()
            assert False
        except StopIteration:
            assert True
        
    def test_plugin_instances(self):
        plugin1 = Plugin(ctx())
        plugin2 = Plugin(ctx())
        loop = Loop([plugin1, plugin2])
        
        p = loop.next()
        assert p == plugin1
        p = loop.next()
        assert p == plugin2
        
        try:
            loop.next()
            assert False
        except StopIteration:
            assert True
            
    def test_plugin_names(self):
        loop = Loop([PLUGIN_NAME, PLUGIN_NAME])
        
        p = loop.next()
        assert isinstance(p, Plugin)
        p = loop.next()
        assert isinstance(p, Plugin)
        
        try:
            loop.next()
            assert False
        except StopIteration:
            assert True
 
    def test_inner_loop(self):
        loop = Loop(
                    Loop([PLUGIN_NAME, 
                          PLUGIN_NAME])
                     )
        
        p = loop.next()
        assert isinstance(p, Plugin)
        p = loop.next()
        assert isinstance(p, Plugin)
        
        try:
            loop.next()
            assert False
        except StopIteration:
            assert True
 
    def test_complex_loop(self):
        loop = Loop([PLUGIN_NAME,
                    Loop([PLUGIN_NAME, 
                          PLUGIN_NAME]),
                     PLUGIN_NAME])

        p = loop.next()
        assert isinstance(p, Plugin)
        p = loop.next()
        assert isinstance(p, Plugin)
        p = loop.next()
        assert isinstance(p, Plugin)
        p = loop.next()
        assert isinstance(p, Plugin)
        
        try:
            loop.next()
            assert False
        except StopIteration:
            assert True

    def test_loop_iter(self):
        pList = [PLUGIN_NAME, PLUGIN_NAME]
        loop = Loop(pList)
        
        cnt = 0
        for p in loop:
            assert isinstance(p, Plugin)
            cnt += 1

        assert cnt == len(pList)

    def test_loop_max_iter(self):
        maxIter=3
        pList = [PLUGIN_NAME, PLUGIN_NAME]
        
        loop = Loop(pList, stop=RangeStopCriteria(maxIter=maxIter))
        
        cnt = 0
        for p in loop:
            assert isinstance(p, Plugin)
            cnt += 1

        assert cnt == len(pList)*maxIter

    def test_loop_max_iter_nested(self):
        maxIter=3
        pList = [Plugin(ctx()), Plugin(ctx())]
        
        loop = Loop(
                    Loop(pList, 
                         stop=RangeStopCriteria(maxIter=maxIter)),
                    stop=RangeStopCriteria(maxIter=maxIter))
        
        cnt = 0
        for p in loop:
            assert isinstance(p, Plugin)
            p()
            cnt += 1

        assert cnt == len(pList)*maxIter*maxIter

    def test_loop_ctx(self):
        loop = Loop(PLUGIN_NAME)
        ctx = loopCtx(loop)
        assert ctx is not None

    def test_unknown_plugin(self):
        plugin = "unknown.plugin.invalid"
        loop = Loop(plugin)
        try:
            loop.next()
            assert False
        except UnsupportedPluginTypeException as ex:
            print(ex)
            assert True
        
        plugin = {}
        loop = Loop(plugin)
        try:
            loop.next()
            assert False
        except UnsupportedPluginTypeException as ex:
            print(ex)
            assert True
        
    def teardown(self):
        #tidy up
        print("tearing down " + __name__)
        pass
    
    
if __name__ == '__main__':
#     test = TestLoop()
#     test.test_loop_max_iter_nested()
    pytest.main("-k TestLoop")