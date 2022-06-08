pipeline {
agent any
stages {
// stage('Print Env Details node') {
// steps {
// sh 'which node'
// sh 'node -v'
// sh 'which npm'
// sh 'npm -v'
// }
// }
// stage('Switch to Target Branch') {
// steps {
// echo "Switching to branch: master"
// git credentialsId: '62786928-4f0d-40bb-9a95-1b5deae0a654', url: 'https://github.com/prashant4875/CARTS.git'
// sh 'git checkout tags/2022.05.25.124'



// }
// }

stage ('Generate Version for RELEASE'){
            steps {
             script {
                 def now = new Date()
                 time = now.format("yyyy.MM.dd.H.m", TimeZone.getTimeZone('UTC'))
                 sh "echo ${time} > version"
                 tag = readFile('version').trim()
             }
             }
             }	
// stage ('Git tag'){
//     steps{
//         withCredentials([gitUsernamePassword(credentialsId: 'git-access', gitToolName: 'Default')]) {
//         sh "git tag ${tag}"
//         sh "git push origin ${tag}"
//         }
//     }
// }

// stage('Delete wm dependency in package.json file') {
//             steps {
//                 sh '''sed -i '/"serverless-aws-documentation"/d' package.json '''
//             }
//         }





// stage('Install depenedencies') {
// steps {
// script {
// echo "NPM Install dependencies"
// // sh 'aws codeartifact login --tool npm --repository ocs-angular-lib --domain ocs-csd-se-domain --domain-owner 062209676060 --region us-east-1'
// sh 'npm install'
// //sh 'chmod 777 prebuild.sh postbuild.sh'
// // sh 'pwd && ls -lth'
// //sh 'sh prebuild.sh'
// }
// }
// }
// stage('React Build') {
// steps {
// echo "NPM angular build"
// // sh 'aws codeartifact login --tool npm --repository ocs-angular-lib --domain ocs-csd-se-domain --domain-owner 062209676060 --region us-east-1'
// sh 'npm run build'
// }
// }



// stage('Push content to S3 Bucket') {
//     steps {
//     withAWS(credentials: 'AWS-DEV', region: 'ap-southeast-2') {
//     // echo "Push the content to S3 Bucket"
//     // // sh "mv electron/release/OCS-ResourceCenter-win.exe electron/release/'${tag}'-OCS-ResourceCenter-win32-x64.exe"
//     // // sh "aws s3 cp electron/release/'${tag}'-OCS-ResourceCenter-win32-x64.exe s3://csd-planning-ui-build/sit1/"
//     // // sh "aws s3 sync electron/dist/assets/images/ s3://csd-ui-rc-images/sit1/dist/assets/images/ --delete"
//     // sh "aws s3 rm s3://ocsd-bucket-demo-pipeline/ --recursive"
//     sh "aws s3 sync dist/ s3://ocsd-bucket-demo-pipeline/ --delete"
//     // sh "aws s3 sync package.json s3://ocsd-bucket-demo-pipeline/"
//     // sh "aws cloudformation create-stack --stack-name cft-jenkins --template-body file://aws.yaml --region 'ap-southeast-2'"

// }
// }
// }


}

}