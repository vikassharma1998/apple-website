#!groovy
pipeline {
    agent any

    stages {
        stage('Checkout code') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Django server') {
            steps {
                sh 'python3 manage.py runserver'
            }
        }
    }
}
