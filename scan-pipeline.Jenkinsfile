pipeline{


  agent {
    kubernetes {
      cloud 'openshift'
      label 'push-clair2grafeas'
      yaml '''
apiVersion: v1
kind: Pod
metadata:
  labels:
    worker: push-clair2grafeas
spec:
  containers:
    - name: jnlp
      image: registry.redhat.io/openshift4/ose-jenkins-agent-base:latest
      args: ["$(JENKINS_SECRET)", "$(JENKINS_NAME)"]
      workingDir: '/home/jenkins/agent'
    - name: push-clair2grafeas
      image: quay.io/kjanania/push-clair2grafeas:latest
      workingDir: '/home/jenkins/agent'
      command:
        - cat
      tty: true
'''
    }
  }

  stages {
    stage('clair-scan') {
      steps {
        container('push-clair2grafeas') {
          sh "echo test"
        }
      }
    }
  }
}
