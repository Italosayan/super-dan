pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'ls'
                sh 'pwd'
                sh 'virtualenv venv --distribute'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'python super_dan_app/dataset/get_data.py'
            }
        }
    }
}