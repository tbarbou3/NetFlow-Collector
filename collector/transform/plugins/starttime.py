from collector.base import DateTimeSinceEpoch

class StartTime(DateTimeSinceEpoch):
    def __init__(self):
        self.pluginName = __name__
        super(StartTime,self).__init__()
    def run(self,inputObject):
        #inputObject is a Flow Record at this point
        try:
            inputObject.start_time = str(self.getDateTime(inputObject.start_time))
            #print "start_time: %s"%inputObject.start_time
        except AttributeError:
            print "start_time empty"
        #no need to return anything since we are modding by reference