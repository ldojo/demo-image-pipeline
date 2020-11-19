pipeline {
    agent any

    stages {
        stage('Scan') {
            steps {
                script 
                {
                    if (params.IMAGE_URL == '') { // and/or whatever condition you want
                        currentBuild.result = 'ABORTED'
                        error('params.IMAGE_URL not set')
                    }
                }
                echo "scanning image ${params.IMAGE_URL}"
                sleep 5
                sh "curl -X POST -G --data-urlencode \"image=${params.IMAGE_URL}\" --data-urlencode \"status=SCANNED\" http://operator-pipeline-api-operator-pipeline.apps.ilab-ctigtdc21d.ecs.dyn.nsroot.net/images/status/"
                }
        }
        stage('TDLC Maintenance'){
            steps {
                sleep 5
            }
        }
        stage('Eng Tests'){
            steps {
                sleep 5
            }
        }
        stage('Promotion'){
            steps {
                sh   """
                        #!/bin/bash
     
                        set -x
                        set
                        echo "promoting ${params.IMAGE_URL}"
                        echo "using EAR_AUTHS ${params.EAR_AUTHS}"
                        echo "${params.EAR_AUTHS}" > auths.json
                        curl -G --data-urlencode "sourceImage=$IMAGE_URL" http://operator-pipeline-api:8080/imagePromotionTargets > promotions
                        echo "operator-pipeline-api service returned these image promotions:"
                        cat promotions
                        cat promotions | sed "s,\\(.*\\) \\(.*\\),oc image mirror --insecure=true --registry-config=auths.json \\1 \\2," > promotions.sh
                        echo "executing promotion script: "
                        cat promotions.sh
                        bash promotions.sh
     
                     """
            }
        }
    }
}

