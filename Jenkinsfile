pipeline {
    agent any  // Runs on any available node (including master)
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/NadavElgrabli/python-ci-cd-simple.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv $WORKSPACE/venv  // Create virtual environment
                source $WORKSPACE/venv/bin/activate  // Activate venv (Linux)
                pip install -r requirements.txt  // Install dependencies
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                source $WORKSPACE/venv/bin/activate  // Activate venv (Linux)
                python3 -m pytest  // Run tests with Python3
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Deploying the application...'  // Placeholder for deployment
            }
        }
    }
}
