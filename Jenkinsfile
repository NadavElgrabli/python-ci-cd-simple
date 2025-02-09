pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/python-ci-cd-project.git'  // Replace with your GitHub URL
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'  // Install pytest and other dependencies
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest'  // Run the tests using pytest
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying the application..."'  // Placeholder for deployment step
            }
        }
    }
}
