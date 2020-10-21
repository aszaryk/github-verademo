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
                        stage('Veracode Pipeline'){
                            steps {
                                - sh 'curl -O https://downloads.veracode.com/securityscan/pipeline-scan-LATEST.zip'
                                - sh 'unzip pipeline-scan-LATEST.zip pipeline-scan.jar'
                                - sh 'java -jar pipeline-scan.jar \
                                --veracode_api_id "${veracode_id}" \
                                --veracode_api_key "${veracode_key}" \
                                --file "build/libs/sample.jar" \
                                --fail_on_severity="Very High, High" \
                                --fail_on_cwe="80" \
                                --baseline_file "${CI_BASELINE_PATH}" \
                                --timeout "${CI_TIMEOUT}" \
                                --project_name "GitHub VeraDemo" \
                                --project_url "${env.GIT_URL}" \
                                --project_ref "${env.GIT_COMMIT}"' \
                            }
                        }
                        stage('Veracode Policy Scan') {
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