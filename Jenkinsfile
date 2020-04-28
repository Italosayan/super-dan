pipeline {
    agent { dockerfile true}
    stages {
        stage('test') {
            steps {
                sh 'ls super_dan_app/dataset/queried_data'
                sh 'python --version'
                sh 'python -m pytest'
                sh 'python tests/day_2020-04-04_crimes_datatest.py'
                sh 'ls super_dan_app/dataset/queried_data'
            }
        }
        stage('build') {
            steps {
                sh 'python super_dan_app/dataset/get_data.py'
                sh 'ls super_dan_app/dataset/queried_data'
                sh 'python super_dan_app/dataset/pre_processing.py'
                sh 'python -m training.training'
            }
        }
    }
}