from collector.base import PlugableBase

import utils.settings as Settings

class Context(PlugableBase):
    def __init__(self):
        self.stage = "context"
        super(Context,self).__init__()
        
    def run(self,inputObject):
        #HACK: this assumes 1 plugin for the interface
        #        this needs to be fixed
        for key in self.modInstances:
            return self.modInstances[key].run(inputObject)