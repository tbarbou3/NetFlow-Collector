from collector.base import DecimalToDotIP

class DstAddr(DecimalToDotIP):
    def __init__(self):
        self.pluginName = __name__
        super(DstAddr,self).__init__()

    def run(self,inputObject):
        #inputObject is a Flow Record at this point
        inputObject.dst_addr = self.numIP2strIP(inputObject.dst_addr)
        #print "Dst Addr: %s"%inputObject.dst_addr
        #no need to return anything since we are modding by reference