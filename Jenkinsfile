pipeline {
    agent { label 'windows-agent' } // Specifies your Windows node label

    stages {
        stage('Checkout') {
            steps {
                // Pulls the code from your GitHub repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest --verbose
                '''
            }
        }
    }
}
