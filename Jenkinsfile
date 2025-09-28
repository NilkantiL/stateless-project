pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-assignment:latest ./app'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh """
                    cd app
                    pip install -r requirements.txt
                    pytest -q --junitxml=../reports/test-results.xml
                """
            }
            post {
                always {
                    junit 'reports/test-results.xml'
                }
            }
        }

        stage('Quick Smoketest') {
            steps {
                sh """
                    docker run -d --name test-container -p 8080:8080 devops-assignment:latest
                    sleep 5
                    curl -f http://localhost:8080/health
                """
            }
        }

    } // end stages

    post {
        always {
            sh 'docker stop test-container || true && docker rm test-container || true'
            echo "Pipeline finished"
        }
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline Failed'
        }
    }

} // end pipeline

