pipeline {
    agent { docker { image 'python:3.7.5' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'ls'
                sh 'pwd'
                sh  'python -m venv env'
                sh  'source env/bin/activate'
                sh 'pip install -r requirements.txt'
            }
            steps {
                sh 'python super_dan_app/dataset/get_data.py'
            }
        }
    }
}