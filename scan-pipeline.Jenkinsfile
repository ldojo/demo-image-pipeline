pipeline{
  parameters {
    string(
      defaultValue: 'operators',
      description: 'The name of the project in Grafeas in which to push the CVE results to.',
      name: 'project',
      trim: true)
    string(
      name: 'image',
      description: 'Container image to scan.',
      trim: true)
    )
  }

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
    - name: push-clair2grafeas
      image: quay.io/kjanania/push-clair2grafeas:latest
      command:
        - cat
      tty: true
  imagePullSecrets:
    - name: jenkins-pull-secret
'''
    }
  }

  stages {
    stage('clair-scan') {
      steps {
        container('push-clair2grafeas') {
          sh "entrypoint ${params.project} ${params.image} http://clairsvc.default.svc.cluster.local:6060 " +
              "grafeas.default.svc.cluster.local:8080"
        }
      }
    }
  }
}