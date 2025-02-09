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
                script {
                    def venvDir = "${env.WORKSPACE}/venv"
                    // Create the virtual environment and activate it with bash
                    sh "python3 -m venv ${venvDir}"  // Create virtual environment
                    sh "bash -c '. ${venvDir}/bin/activate && pip install -r requirements.txt'"  // Activate venv and install dependencies
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def venvDir = "${env.WORKSPACE}/venv"
                    // Activate the virtual environment and run tests
                    sh "bash -c '. ${venvDir}/bin/activate && python3 -m pytest'"  // Activate venv and run tests
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Deploying the application...'  // Placeholder for deployment
            }
        }
    }
}
