pipeline {
    agent any

    triggers {
        issueCommentTrigger('.*rerun this build.*')
    }

    stages {

        stage('Install') {
            steps {
                echo '[GUARDIAN] Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo '[GUARDIAN] Running tests...'
                sh 'python -m pytest test_app.py -v'
            }
        }

        stage('Done') {
            steps {
                echo '[GUARDIAN] Build complete!'
            }
        }

    }

    post {
        success {
            echo '[GUARDIAN] ✅ Build PASSED — safe to merge PR'
        }
        failure {
            echo '[GUARDIAN] ❌ Build FAILED — RAG will suggest fix'
        }
    }
}
