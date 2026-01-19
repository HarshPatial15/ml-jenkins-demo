pipeline {
    agent any

    environment {
        IMAGE_NAME = 'ml-model-api'
        IMAGE_TAG  = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f ${IMAGE_NAME} || true'
                sh 'docker run -d --name ${IMAGE_NAME} -p 5000:5000 ${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }

        stage('Smoke Test') {
    steps {
        sh '''
          sleep 5
          curl -s http://localhost:5000/health | grep '"status":"ok"'
        '''
    }
}


    }

    post {
        success {
            echo 'Pipeline completed: model trained, image built, API deployed.'
        }
        failure {
            echo 'Pipeline failed. Check console logs.'
        }
    }
}
