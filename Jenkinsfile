pipeline {
    agent any  // Runs on any available node (including master)
    
    environment {
        VENV = 'venv'
    }
    
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
                        // For Linux-based agents
                        sh '''
                        python3 -m venv venv  # Create virtual environment
                        source venv/bin/activate  # Activate venv
                        pip install -r requirements.txt  # Install dependencies
                        '''
                    } else {
                        // For Windows-based agents
                        bat '''
                        python -m venv venv  // Create virtual environment
                        call venv\\Scripts\\activate  // Activate venv
                        pip install -r requirements.txt  // Install dependencies
                        '''
                    }
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        // For Linux-based agents
                        sh '''
                        source venv/bin/activate  # Activate venv
                        pytest  # Run tests
                        '''
                    } else {
                        // For Windows-based agents
                        bat '''
                        call venv\\Scripts\\activate  // Activate venv
                        pytest  // Run tests
                        '''
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (isUnix()) {
                        // For Linux-based agents
                        sh 'echo Deploying the application...'
                    } else {
                        // For Windows-based agents
                        bat 'echo Deploying the application...'
                    }
                }
            }
        }
    }
}
