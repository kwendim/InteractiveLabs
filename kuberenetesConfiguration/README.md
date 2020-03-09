Setup made using minkube with the --vm-driver=kvm2

First apply the serviceaccount and then cluster role

    kubectl apply -f serviceAccount.yml
    kubectl apply -f clusterRoles.yml

Then the webserver/db deployment and the service to make it accessible externally 

    kubectl apply -f web-deployment.yaml
    kubectl apply -f web-service.yaml


To get the external ip, you can run

    minikube service web --url

    

    For security related things, the webserver pod has all the access. Once done, the verbs in clusterrolebinding should be adjusted in accordance to the law of least privelege

    In addition, instead of using cluster roles, it may be possible to simply define roles which only apply to a certain namespace

    the token management for the pod should also be considered