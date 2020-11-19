pipeline{
  parameters {
    string(
      defaultValue: 'operators',
      description: 'The name of the project in Grafeas in which to push the CVE results to.',
      name: 'project',
      trim: true
    )
    string(
      name: 'image',
      description: 'Container image to scan.',
      trim: true
    )
    string(
      name: 'clair',
      description: 'URL of the Clair instance to use for image scanning',
      trim: true,
      defaultValue: 'http://clairsvc:6060'
    )
    string(
      name: 'grafeas',
      description: 'Hostname and port of the Grafeas instance',
      trim: true,
      defaultValue: 'grafeas:8080'
    )
    string(
      name: 'operatorCatalogHost',
      description: 'Location of the Operator Catalog API service',
      trim: true,
      defaultValue: 'http://operator-pipeline-api:8080'
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
      workingDir: '/home/jenkins/agent'
    - name: push-clair2grafeas
      image: quay.io/kjanania/push-clair2grafeas:latest
      workingDir: '/home/jenkins/agent'
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
          sh "echo test"
//          sh "entrypoint ${params.project} ${params.image} ${params.clair} ${params.grafeas} ${params.operatorCatalogHost}"
        }
      }
    }
  }
}
