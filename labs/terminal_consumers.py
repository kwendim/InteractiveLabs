from channels.generic.websocket import WebsocketConsumer
import json
from labs.ssh import SSH
from labs.kubeCommands import Kubernetes

class TerminalConsumer(WebsocketConsumer):

    def connect(self):
        #TODO Maybe not accept a connection based on some requirements
        #containers should be spawned before the connection is established


        self.accept()

        #check the ip address of the device to be connected to
        path_to_keyFile = "privateKey.pem"
        pod = Kubernetes("studentno", "/code/kuberenetesConfiguration/studentBaseImage.yml" )

        ip_address = pod.createPod() #TODO make checks if the creation of Pod was successful 

        self.ssh = SSH(websocket=self, kubernetesPod = pod)
        self.ssh.connect(ip_address, path_to_keyFile, pod)


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
