pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'ls'
                sh 'pwd'
                sh 'python -m venv env'
                sh 'source env/bin/activate'
                sh 'pip install -r requirements'
            }
        }
    }
}