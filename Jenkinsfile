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
                python3 -m venv venv  // Create virtual environment
                source venv/bin/activate  // Activate venv
                pip install -r requirements.txt  // Install dependencies
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate  // Activate venv
                python3 -m pytest  // Run tests with Python
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
