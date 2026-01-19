pipeline {
    agent {
        // Use a Docker agent with Python for any pre-build steps if needed
        // For this demo, we build the image directly; Docker socket is mounted to Jenkins
        label '' // default agent inside Jenkins container
    }

    environment {
        IMAGE_NAME = 'ml-model-api'
        IMAGE_TAG  = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Replace with your GitHub repo URL after you push
                git 'https://github.com/HarshPatial15/ml-jenkins-demo.git'
                branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Run Container') {
            steps {
                // Stop any existing container
                sh 'docker rm -f ${IMAGE_NAME} || true'
                // Run new container
                sh 'docker run -d --name ${IMAGE_NAME} -p 5000:5000 ${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }

        stage('Smoke Test') {
            steps {
                // Simple health check
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

