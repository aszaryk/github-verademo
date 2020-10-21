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

                        stage('Agent-SCA') {
                            steps {
                                 withCredentials([string(credentialsId: 'SRCCLR_API_TOKEN', variable: 'SRCCLR_API_TOKEN')]) {
                                    sh '''
                                        curl -sSL https://download.sourceclear.com/ci.sh | sh -s -- scan --update-advisor
                                    '''
                                    }
                            }
                        }
                        stage('Veracode Pipeline'){
                            steps {
                                withCredentials([usernamePassword(credentialsId: 'veracode-credentials', passwordVariable: 'veracode_key', usernameVariable: 'veracode_id')]) {
                                   sh '''
                                      curl -s -O https://downloads.veracode.com/securityscan/pipeline-scan-LATEST.zip
                                      unzip -o pipeline-scan-LATEST.zip pipeline-scan.jar
                                      java -jar pipeline-scan.jar -vid $veracode_id -vkey $veracode_key -f ./target/verademo.war --fail_on_severity="Very High, High" --project_name "GitHub Verademo"
                                   '''
                                }
                            }
                        }
                        stage('Veracode Policy Scan') {
                            steps {
                                withCredentials([usernamePassword(credentialsId: 'veracode-credentials',passwordVariable: 'veracode_key', usernameVariable: 'veracode_id')]){
                                     veracode applicationName: 'VeraDemo', createSandbox: true, criticality: 'Medium', fileNamePattern: '', replacementPattern: '', sandboxName: 'Integration Pipeline', scanExcludesPattern: '', scanIncludesPattern: '', scanName: 'pipeline-$buildnumber', uploadExcludesPattern: '', uploadIncludesPattern: '**/**.war', useIDkey: true, vid: veracode_id, vkey: veracode_key, vpassword: '', vuser: ''
                                     }
                            }
                        }

    }
}