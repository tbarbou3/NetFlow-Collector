
from collector.base import PluginBase
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
import utils.settings as Settings
import json



class Kafka(PluginBase):
    def __init__(self):
        self.pluginName = "KafkaProducer"
        super(Kafka,self).__init__()
        #TODO: move kafka client config to config.ini
        #print(dir(kafkaproducer))
        self.myKafka = KafkaClient("192.168.100.124", 9092)
        self.producer = SimpleProducer(self.myKafka, "netflow", async=True)

    def run(self,inputObject):
        r = self._fmt(inputObject)
        self.producer.send_messages(r)
    def _fmt(self,inputObject):
        r = {key:getattr(inputObject,key) for key in Settings.SETTINGS.getlist(Settings.SETTINGS.get("csv","fieldNames"))}
        self.logger.debug("Sending: %s"%(json.dumps(r)))
        return json.dumps(r)
