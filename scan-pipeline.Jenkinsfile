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
          some-label: some-label-value
      spec:
        containers:
        - name: busybox
          image: docker.io/lshulman/push-clair2grafeas:latest
          command:
          - cat
          tty: true
'''
    }
  }

  stages {
    stage('clair-scan') {
      steps {
        container('busybox') {
          sh "echo test"
        }
      }
    }
  }
}
