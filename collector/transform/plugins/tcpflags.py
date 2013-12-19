'''
Created on Nov 27, 2012

@author: rob
'''
from collector.base import PluginBase

class TcpFlags(PluginBase):
    def __init__(self):
        self.pluginName = __name__
        super(TcpFlags,self).__init__()
    def run(self,inputObject):
        for flag in inputObject.tcp_flags:
            #print "flag %s value %s"%(flag,inputObject.tcp_flags[flag])
            s = "tcp_flag_"+flag
            inputObject.__setattr__(s, inputObject.tcp_flags[flag])
            
            

