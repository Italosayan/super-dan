pipeline {
    agent { docker { image 'python:3.7.5' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'ls'
                sh 'pwd'
                sh 'python -m venv env'
                sh 'ls'
                sh '. env/bin/activate'
                sh 'python -m pip install -r requirements.txt --user --cache-dir /tmp/Super_Dan/master'
                sh 'python super_dan_app/dataset/get_data.py'
            }
        }
    }
}