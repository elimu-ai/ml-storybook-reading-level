import os

os.chdir('step1_prepare')
print(os.path.basename(__file__), 'os.getcwd(): {}'.format(os.getcwd()))
import step1_prepare.step1_1_download_data
import step1_prepare.step1_2_preprocess_data

os.chdir('../step2_train')
print(os.path.basename(__file__), 'os.getcwd(): {}'.format(os.getcwd()))
import step2_train.step2_1_train_model_pkl
import step2_train.step2_2_train_model_pmml

os.chdir('../step3_predict')
print(os.path.basename(__file__), 'os.getcwd(): {}'.format(os.getcwd()))
import step3_predict.step3_1_predict
import step3_predict.step3_2_validate
