========
Usage
========

To use Ivy workflow engine in a project::

	from ivy.workflow_manager import WorkflowManager
	args = ["--size-x=100",
		"--size-y=100", 
		"ufig.config.random"]
        
	mgr = WorkflowManager(args)
	mgr.launch()
    
alternatively ivy can also be used from the command line::

	$ ivy --size-x=100 --size-y=100 ufig.config.random
	
	
A configuration can range form very simple to arbitrarily complex. 

In the simplest case the configuration file would look something like::

	from ivy.config import base_config

	plugins = ["test.plugin.simple_plugin",
           	"test.plugin.simple_plugin"
                ]

Importing basic functionality from `base_config` and defining a list of plugins.


A slightly more complex use case would look something like::

	from ivy.config import base_config
	from ivy.loop import Loop
	from ivy.utils.stop_criteria import RangeStopCriteria

	context_provider = "ivy.context_provider.PickleContextProvider"
	ctx_file_name = "ivy_cxt.dump"

	plugins = Loop(["test.plugin.simple_plugin",
			Loop(["test.plugin.simple_plugin",
			      "test.plugin.simple_plugin"], 
			      stop=RangeStopCriteria(maxIter=5)),
			"test.plugin.simple_plugin"], 
			stop=RangeStopCriteria(maxIter=2))

	a=1.5
	b=["omega", "lambda", "gamma"]
	c=None

Configures the 'PickleContextProvider' as context provider which ensures that 
the context is persisted to the file "ivy_ctx.dump" after every execution of a plugin

The list of plugins consists of two nested loops. Each having two plugins. The inner lopp will be 
executed 5 times and the outer loop twice.

Furthermore the config defines the attributes 'a', 'b' and c where 'a' is a float and 'b' a list of strings
and c is a NoneType. The type of c will automatically be inferred from the given value from the command line.

Calling this config and overriding the attributes from the command line would look something like this::

	$ ivy --a=1.75 --b=zeta,beta,gamma --c=False package.subpackage.module