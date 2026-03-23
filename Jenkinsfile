pipeline {
    agent any

    triggers {
        issueCommentTrigger('.*rerun this build.*')
    }

    stages {

        stage('Install') {
            steps {
                echo '[GUARDIAN] Installing dependencies...'
                sh 'pip3 install -r requirements.txt --break-system-packages'
            }
        }

        stage('Dependency Compatibility Tests') {
            steps {
                echo '[GUARDIAN] Running tests...'
                sh 'python3 -m pytest test_dependencies.py -v'
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
