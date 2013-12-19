from collector.base import DateTimeSinceEpoch

class EndTime(DateTimeSinceEpoch):
    def __init__(self):
        self.pluginName = __name__
        super(EndTime,self).__init__()
    def run(self,inputObject):
        #inputObject is a Flow Record at this point
        try:
            inputObject.end_time = str(self.getDateTime(inputObject.end_time))
            #print "end_time: %s"%inputObject.end_time
        except AttributeError:
            print "end_time empty"
        #no need to return anything since we are modding by reference