pipeline {
    agent { docker { image 'python:3.7.5' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'ls'
                sh 'pwd'
                sh 'python3 -m venv env'
                sh 'ls'
                sh 'source env/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'python super_dan_app/dataset/get_data.py'
            }
        }
    }
}