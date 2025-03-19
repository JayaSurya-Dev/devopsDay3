pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Installing dependencies..."'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Running Tests..."'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Starting Docker Container..."'
                sh 'docker-compose up -d'
            }
        }
    }
}
