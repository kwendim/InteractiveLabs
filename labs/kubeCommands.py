from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
import yaml 
from kubernetes import client, config
import os
from kubernetes.client.rest import ApiException



class Kubernetes:
    def __init__(self, podName, deploymentPath, namespace = "default"):
        config.load_incluster_config()
        self.v1 = client.CoreV1Api()
        self.podName = podName
        self.namespace = namespace
        self.deploymentFilePath = deploymentPath
    
    def createPod(self):
        #this random name generation is temporary. Should be replaced with the name of the user, and lab
        import random
        import string
        randomized_podName = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        self.podName = self.podName + "-" + randomized_podName
    
        if not os.path.exists(self.deploymentFilePath): #replace the os.path with the workdir of django
            return "os path does not exist"
        
        with open(self.deploymentFilePath) as f:
            deploymentContent = yaml.safe_load(f)
            deploymentContent['metadata']['name'] = self.podName
        
            # k8s_apps_v1 = client.AppsV1Api()
            # resp = k8s_apps_v1.create_namespaced_deployment(
            #     body=dep, namespace="default")
            try:
                resp = self.v1.create_namespaced_pod(body=deploymentContent, namespace="default") #try catch here to check if the deployment name exists
                while True:
                    allPods = self.v1.list_pod_for_all_namespaces(watch=False)
                    
                    for item in allPods.items:
                        if item.metadata.name == self.podName and not item.status.pod_ip == None:
                            self.podIp = item.status.pod_ip
                            return item.status.pod_ip
            except ApiException as e:

                print("encountered error:", e)
                return "pod already exists"
            
    
    def deletePod(self):
        try:
            self.v1.delete_namespaced_pod(self.podName, self.namespace,grace_period_seconds=0)
            return "deleted successfully"
        except ApiException as e:
            print("Exception when calling CoreV1Api->delete_namespaced_pod: %s\n" % e)
            return "somefreaky error"

    


# if __name__ == '__main__':
#     pod = Kubernetes("studentno",os.path.join(os.path.dirname(__file__), "studentBaseImage2.yaml") )
#     # deleteReturn = pod.deletePod()
#     # print("delete: ", deleteReturn)
#     the_string = pod.createPod()
#     if the_string == "pod already exists":
#         the_string = pod.deletePod()
#         print(the_string)
#         the_string = pod.createPod()

#     print("the ip is ", the_string)
