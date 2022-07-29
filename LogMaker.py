import sys
sys.dont_write_bytecode = True

import os
import datetime
import logging

class LogMaker():
    ''' basic logger creator '''
    
    def __init__(self, workDir ):
        
        self.logDir = f"{workDir}\\_logs"
        if not os.path.exists( self.logDir ): os.makedirs( self.logDir )
    
    def make( self, logName, logLevel ):
        
        log = logging.getLogger(logName)
        path = f"{self.logDir}\\{self.dtStamp()}_{logName}.log"
        handler = logging.FileHandler( path, 'w', 'utf-8' )
        handler.setFormatter( 
            logging.Formatter(""
                + "[ %(asctime)s ]"
                + "[ %(levelname)s ] "
                + "%(message)s"
                )
            )
        log.addHandler( handler )
        match logLevel:
            case "info" : log.setLevel( logging.INFO )
            case "debug" : log.setLevel( logging.DEBUG )
            case "warning" : log.setLevel( logging.WARNING )
            case "error" : log.setLevel( logging.ERROR )
            case _ : log.setLevel( logging.DEBUG )
            
        return log
    
    def dtStamp( self ):
        datetimenow = datetime.datetime.now()
        return datetimenow.strftime("%y%m%d_%H%M%S%f")

