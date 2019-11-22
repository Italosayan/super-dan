pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'ls'
                sh 'pwd'
                sh 'pip install -r requirements'
                sh 'python super_dan_app/dataset/get_data.py'
            }
        }
    }
}