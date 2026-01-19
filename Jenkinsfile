pipeline {
    agent {
        docker { 
            image 'docker:24.0.5' // Docker-enabled image 
            args '-v /var/run/docker.sock:/var/run/docker.sock' }// default agent inside Jenkins container
    }

    environment {
        IMAGE_NAME = 'ml-model-api'
        IMAGE_TAG  = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git(
                    url: 'https://github.com/HarshPatial15/ml-jenkins-demo.git',
                    branch: 'main'
                )
            }
        }

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
                sh 'curl -s http://localhost:5000/health | grep ok'
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
