import utils.settings as Settings
from collector.base import PluginBase
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

class WebSocket(PluginBase):
    def __init__(self):
        server = pywsgi.WSGIServer(("", 8000), self.websocket_app,
            handler_class=WebSocketHandler)
        server.start()
        
    def run(self,inputObject):
        self.sock.send(inputObject)
    
    def websocket_app(self, environ, start_response):
        #need to hold the socket open....
        self.sock = environ["wsgi.websocket"]
        while True:
            pass
