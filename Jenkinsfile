pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/AyhamAlkhatib03/Bankruptcy_Prediction.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh '''
                python3 -m venv $VENV_DIR
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install papermill jupyter pandas numpy matplotlib scikit-learn xgboost seaborn
                '''
            }
        }

        stage('Lint Notebook') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                pip install nbqa flake8
                nbqa flake8 Bankruptcy_Prediction.ipynb || echo "Linting completed with warnings."
                '''
            }
        }

        stage('Run Notebook') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                papermill Bankruptcy_Prediction.ipynb output.ipynb
                '''
            }
        }

        stage('Convert to HTML Report') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                jupyter nbconvert --to html output.ipynb
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'output.ipynb', onlyIfSuccessful: true
                archiveArtifacts artifacts: 'output.html', onlyIfSuccessful: true
            }
        }
    }
}
