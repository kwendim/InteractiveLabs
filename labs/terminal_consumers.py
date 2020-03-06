from channels.generic.websocket import WebsocketConsumer
import json
from labs.ssh import SSH

class TerminalConsumer(WebsocketConsumer):

    def connect(self):
        #Maybe not accept a connection based on some requirements
        # containers should be spawned before the connection is established


        self.accept()
        self.ssh = SSH(websocket=self)

        #check the ip address of the device to be connected to
        path_to_keyFile = "privateKey.pem"
        ip_address = "172.18.0.2" 

        self.ssh.connect(ip_address, path_to_keyFile)


    def disconnect(self, close_code):
        print("consumer done!")
        try:
            if close_code == 3001:
                pass
            else:
                self.ssh.close()
        except:
            pass
        finally:
            print("disconnecting socket")

    def receive(self, text_data):
        self.ssh.shell(text_data)
