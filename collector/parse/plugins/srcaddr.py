from collector.base import DecimalToDotIP

class SrcAddr(DecimalToDotIP):
    def __init__(self):
        self.pluginName = __name__
        super(SrcAddr,self).__init__()
    def run(self,inputObject):
        #inputObject is a Flow Record at this point
        inputObject.src_addr = self.numIP2strIP(inputObject.src_addr)
        #print "Src Addr: %s"%inputObject.src_addr
        #no need to return anything since we are modding by reference