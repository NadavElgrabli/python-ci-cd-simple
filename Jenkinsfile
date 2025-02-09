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
                    // Ensure the virtual environment is created in a correct directory
                    def venvDir = "${env.WORKSPACE}/venv"
                    sh "python3 -m venv ${venvDir}"  // Create virtual environment in the correct directory
                    sh "source ${venvDir}/bin/activate && pip install -r requirements.txt"  // Activate venv and install dependencies
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def venvDir = "${env.WORKSPACE}/venv"
                    sh "source ${venvDir}/bin/activate && python3 -m pytest"  // Activate venv and run tests
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
