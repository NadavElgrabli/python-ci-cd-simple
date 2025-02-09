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
                python -m venv venv  // Create virtual environment
                call venv\\Scripts\\activate  // Activate venv
                pip install -r requirements.txt  // Install dependencies
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                call venv\\Scripts\\activate  // Activate venv
                python -m pytest  // Run tests with Python (instead of pytest command)
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
