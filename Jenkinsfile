pipeline {
    agent { dockerfile true }
    stages {
        stage('test') {
            steps {
                sh 'python --version'
                sh 'python -m pytest'
            }
        }
        stage('build') {
            steps {
                sh 'python super_dan_app/dataset/get_data.py'
                sh 'python super_dan_app/dataset/pre_processing.py'
                sh 'python -m training.training'
            }
        }
    }
}