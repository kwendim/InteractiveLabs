Setup made using minkube with the --vm-driver=kvm2

First apply the serviceaccount and then cluster role

    kubectl apply -f serviceAccount.yml
    kubectl apply -f clusterRoles.yml

Then apply the persistent volume claim to make persistent storage for the webhooks and database

    kubectl apply -f web-claim-pvc.yaml


Then the webserver/db deployment and the service to make it accessible externally 
    
    kubectl apply -f db-deployment.yaml    (for the time being, the database must first be deployed before the webserver is started)
    kubectl apply -f db-service.yaml
    kubectl apply -f web-deployment.yaml
    kubectl apply -f web-service.yaml


To get the external ip, you can run

    minikube service web --url

    

    For security related things, the webserver pod has all the access. Once done, the verbs in clusterrolebinding should be adjusted in accordance to the law of least privelege

    In addition, instead of using cluster roles, it may be possible to simply define roles which only apply to a certain namespace

    the token management for the pod should also be considered