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
                script {
                    if (isUnix()) {
                        sh '''
                        python3 -m venv venv  # Create virtual environment (Unix)
                        source venv/bin/activate  # Activate venv (Unix)
                        pip install -r requirements.txt  # Install dependencies
                        '''
                    } else {
                        bat '''
                        python -m venv venv  # Create virtual environment (Windows)
                        call venv\\Scripts\\activate  # Activate venv (Windows)
                        pip install -r requirements.txt  # Install dependencies
                        '''
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                        source venv/bin/activate  # Activate venv (Unix)
                        pytest  # Run tests (Unix)
                        '''
                    } else {
                        bat '''
                        call venv\\Scripts\\activate  # Activate venv (Windows)
                        pytest  # Run tests (Windows)
                        '''
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'echo Deploying the application...'  # Placeholder for deployment (Unix)
                    } else {
                        bat 'echo Deploying the application...'  # Placeholder for deployment (Windows)
                    }
                }
            }
        }
    }
}
