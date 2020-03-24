import paramiko
from threading import Thread
from io import StringIO

class SSH:
    def __init__(self, websocket, kubernetesPod):
        self.websocket = websocket
        self.kubernetesPod = kubernetesPod
        self.cmd = ''
        self.res = ''
    
    def connect(self, host, path_to_keyFile, password=None, port=22, timeout=30, term='ansi', pty_width=80, pty_height=24):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            key = open(path_to_keyFile,'r').read()
            keyFile = StringIO(key)
            private_key = paramiko.RSAKey.from_private_key(keyFile)   
            print("about to establish SSH connection with: ", host)
            self.ssh_client.connect(username='root', hostname=host, port=port, pkey=private_key, timeout=timeout)


            transport = self.ssh_client.get_transport()
            self.channel = transport.open_session()
            self.channel.get_pty(term=term, width=pty_width, height=pty_height)
            self.channel.invoke_shell()


            print("Starting thread")      
            self.listening_thread = Thread(target=self.websocket_to_django)
            self.listening_thread.start()

        except  Exception as e: #don't print exception in production
            print(e)
            message = 'The connection faild...'
            self.websocket.send(message)
            self.websocket.close(3001)

    def resize_pty(self, cols, rows):
        self.channel.resize_pty(width=cols, height=rows)

    def websocket_to_django(self):
        try:
            while True:
                data = self.channel.recv(1024).decode('windows-1252') #UTF-8 was not decoding some bytes
                if not len(data):
                    self.close()
                    return
                self.res += data
                self.websocket.send(data)
        except  Exception as e: #don't print exception in production
            print("Exception in wesocket_to_django", e)
            self.close()

    def close(self):
        self.websocket.send('connection closed...')
        self.channel.close()
        self.ssh_client.close()
        self.websocket.close()
        self.kubernetesPod.deletePod()
    
        print("channel, ssh_client and websocket closed. Pod deleted")

    def shell(self, data):
        try:
            self.channel.send(data)
            if data == '\r':
                data = '\n'
            self.cmd += data
        except  Exception as e: #don't print exception in production
            print("exception in shell: ", e)
            self.websocket.send("Failed in sending data. Closing ssh connection\n\r")
            self.close()
