from LogMaker import LogMaker

import os

class LogImplementer():
    '''
    This implementer example instantiates LogMaker() as "logMaker",
    outputting to the cwd path of the example document.
    It uses 'logMaker.make' to assign an info log to self.log
    which can then be used in-class as self.log.info( logItem )
    or with added behaviour through a method, for example
    '[instance].logInfo( "exampleLogRecord" )' console-prints the log item,
    and adds the log item to an instance dictionary.
    '''
    
    def __init__(self):
        
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        logMaker = LogMaker( os.getcwd() )
        
        newLogName = "honks"
        newLogLevel = "info"
        self.log = logMaker.make( newLogName, newLogLevel )
        
        self.infoList = []
    
    
    def logInfo( self, item ):
        ''' add behaviour to run when logging'''
        
        self.log.info( f"{item}" )
        self.infoList.append( item )
        print( f"logged info:\n{item}" )
    
    
    def egAction( self ):
        
        def getHonk(): return "HONK!"
        
        self.log.info( f"1: {getHonk()}" ) # won't print to console
        self.logInfo( f"1: {getHonk()} 2:{getHonk()}" )  # prints


honk = LogImplementer()
print(honk.__doc__)
honk.logInfo( "external Honk Honk" )
honk.egAction()

print('''
    generated the following log records:
    
    [ 2022-07-29 23:56:55,967 ][ INFO ] external Honk Honk
    [ 2022-07-29 23:56:55,967 ][ INFO ] 1: HONK!
    [ 2022-07-29 23:56:55,968 ][ INFO ] 1: HONK! 2:HONK!
    
    ''')
