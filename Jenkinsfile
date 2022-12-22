@Library('caelum@refs/tags/v0.12.0') _

pipeline{
    agent{
        docker{
            image '169.254.149.20:6001/arch_python_git_ghost_opencv_baw:v1.46.0'
        }
    }
    environment{
        DEV_BBVIEW_TMP = '/var/tmp/bbview_tmp'
    }
    stages{
        stage('integrate'){
            steps{script{baw.integrate()}}
        }
        stage('setup'){
            steps{script{baw.setup()}}
        }
        stage('generate'){
            steps{
                sh 'baw --docken generate all'
            }
        }
        stage('test'){
            failFast true
            parallel{
                stage('doc'){
                    steps{
                        sh 'baw --docken test docs'
                    }
                }
                stage('fast'){
                    steps{
                        sh 'baw --docken test long'
                    }
                }
            }
        }
        stage('quality'){
            failFast true
            parallel{
                stage('lint'){
                    steps{
                        script{baw.lint()}
                    }
                }
                stage('format'){
                    steps{
                        script{baw.format()}
                    }
                }
            }
        }
        stage('pre-release'){
            when{not{branch 'master'}}
            steps{sh 'baw publish --pre'}
        }
        stage('all'){
            steps{
                sh 'baw --docken test all -n32'
            }
        }
        stage('release'){
            steps{
                script{
                    publish.release()
                    baw.rebase()
                }
            }
        }
    }
}
