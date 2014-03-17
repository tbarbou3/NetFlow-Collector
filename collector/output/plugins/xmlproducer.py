
from collector.base import PluginBase
from xml.dom.minidom import parseString
import utils.settings as Settings
import json
import dicttoxml



class Xmlout(PluginBase):
    def __init__(self):
        self.pluginName = "xmlProducer"
 
    def run(self,inputObject, filename):
        startPos = filename.rfind('/')
        if startPos < 0:
            startPos = 0
        else:
            startPos += 1
            
        endPos = filename.find('-')
        if endPos > -1:
            collection = filename[startPos:endPos]
        else:
           collection = filename
    
        r = self._fmt(inputObject, collection)
        f = open(filename,'w')
        f.write(r)
        f.close()
        
    def _fmt(self,inputObject,collection):
        r = {key:getattr(inputObject,key) for key in Settings.SETTINGS.getlist(Settings.SETTINGS.get("output","fieldNames"))}
        r['collection']=collection

        xml = dicttoxml.dicttoxml(r)
        dom = parseString(xml)
        #print(dom.toprettyxml())
        return xml
        #print("\n")
        #return dom.toprettyxml()
