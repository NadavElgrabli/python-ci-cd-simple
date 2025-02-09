pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/NadavElgrabli/python-ci-cd-simple.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv venv  // Create virtual environment
                call venv\\Scripts\\activate  // Activate venv
                pip install -r requirements.txt  // Install dependencies
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate  // Activate venv
                pytest  // Run tests
                '''
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo Deploying the application...'  // Placeholder for deployment
            }
        }
    }
}
