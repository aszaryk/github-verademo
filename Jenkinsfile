pipeline {
    agent any

    environment {
        def mvnHome = tool 'Maven'
    }

    stages {

        stage ('----Pull----') {
            steps {
                git 'https://github.com/aszaryk/github-verademo.git'
            }
        }
        stage ('----Build----') {
            steps {
                sh "${mvnHome}/bin/mvn clean package"
            }
        }

        stage('--Security Tests--') {
            parallel {
                        stage('Agent-SCA') {
                            steps {
                                 withCredentials([string(credentialsId: 'SRCCLR_API_TOKEN', variable: 'SRCCLR_API_TOKEN')]) {
                                    sh '''
                                        curl -sSL https://download.sourceclear.com/ci.sh | sh
                                    '''
                                    }
                            }
                        }
                        stage('Veracode Static') {
                            steps {
                                withCredentials([usernamePassword(credentialsId: 'veracode-credentials',passwordVariable: 'veracode_key', usernameVariable: 'veracode_id')]){
                                     veracode applicationName: 'VeraDemo', createSandbox: true, criticality: 'Medium', fileNamePattern: '', replacementPattern: '', sandboxName: 'Integration Pipeline', scanExcludesPattern: '', scanIncludesPattern: '', scanName: 'pipeline-$buildnumber', waitForScan: true, timeout: 60, uploadExcludesPattern: '', uploadIncludesPattern: '**/**.war', useIDkey: true, vid: veracode_id, vkey: veracode_key, vpassword: '', vuser: ''
                                     }
                            }
                        }



            }
        }
    }
}