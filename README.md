# Basic logger creator
Designed to accomodate easy implemetation of logging behaviours for as 
many different scenarios as needed.

## Implementation
The implementer example instantiates LogMaker() as "logMaker",
outputting to the cwd path of the example document.
It uses 'logMaker.make' to assign an info log to self.log
which can then be used in-class simply as self.log.info( logItem )
or with added behaviour through a method, for example
'[instance].logInfo( "exampleLogRecord" )' console-prints the log item,
and adds the log item to an instance dictionary.