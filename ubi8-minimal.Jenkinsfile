pipeline {
  agent {
    node {
      label 'maven'
    }
  }

  stages {
    stage('Environment settings') {
      steps {
        script {
          openshift.withCluster() {
            def bc = openshift.selector('buildconfig/citi-ubi8-minimal')
            def build = bc.startBuild()
            timeout(10) {
              build.logs('-f')
              }
            }
          }
        }
      }
    }
  }
}