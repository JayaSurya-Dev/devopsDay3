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
                sh 'echo Installing dependencies...'
                sh '/usr/bin/python3 -m pip install --upgrade pip'
                sh '/usr/bin/python3 -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover tests'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
