pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "salemghaleb"
        IMAGE_NAME = "${DOCKERHUB_USER}/myflaskapp:${BUILD_NUMBER}"
        CONTAINER_NAME = "myflaskcontainer"
        DOCKER_CREDENTIALS = "dockerhub-creds"
    }

    stages {

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: DOCKER_CREDENTIALS,
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh """
                        echo "${DOCKER_PASS}" | docker login -u "${DOCKER_USER}" --password-stdin
                    """
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    echo "Pushing image to Docker Hub..."
                    sh "docker push ${IMAGE_NAME}"
                }
            }
        }

        stage('Trigger ManifestUpdate') {
            steps {
                echo "Triggering update manifest job..."
                build job: 'updatemanifest',
                      parameters: [
                          string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)
                      ]
            }
        }      
    }

    post {
        success {
            echo "Pipeline executed successfully! 🎉"
        }
        failure {
            echo "Pipeline failed ❌"
        }
    }
}
