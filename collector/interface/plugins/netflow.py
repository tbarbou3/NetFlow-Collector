import dpkt
from collector.base import PluginBase

class NetFlowV5(PluginBase):
    def __init__(self):
        self.pluginName = "NetFlowV5"
        super(NetFlowV5,self).__init__()

    def run(self,data):
        try:
            nf = dpkt.netflow.Netflow5(data)

            print "seq:%s, engine:%s"%(nf.flow_sequence,nf.engine_id)
            #we are not using the header portion of the NetFlow Flow, only the NetFlow records
            #    so we are just returning the array of NetFlow Records, which is an iterable
            return nf.data
        except dpkt.NeedData:
            #self.logger.error("Need Data Error")
            pass