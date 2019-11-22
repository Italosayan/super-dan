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
                sh '. env/bin/activate'
                sh 'python -m pip install --user -r requirements.txt'
                sh 'python super_dan_app/dataset/get_data.py'
            }
        }
    }
}