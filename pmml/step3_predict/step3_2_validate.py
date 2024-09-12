from os.path import basename
import pandas
from pypmml import Model
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score

# Load Predictive Model Markup Language (PMML) model
model_pmml_path = '../step2_train/step2_2_model.pmml'
print(basename(__file__), f'model_pmml_path: {model_pmml_path}')
reading_level_model = Model.load(model_pmml_path)
print(basename(__file__), f'reading_level_model: {reading_level_model}')

# Read the preprocessed test data CSV into a DataFrame
storybooks_csv_path = '../step1_prepare/step1_3_storybooks_test.csv'
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)
print(basename(__file__), f'storybooks_dataframe:  \n{storybooks_dataframe}')

# Predict
storybook_features = ['chapter_count', 'paragraph_count', 'word_count']
predictions = reading_level_model.predict(storybooks_dataframe[storybook_features])
print(basename(__file__), f'predictions:  \n{predictions}')
print(basename(__file__), f'type(predictions):  \n{type(predictions)}')

# Write the DataFrame to a CSV file
predictions.to_csv('step3_2_predictions.csv', index=False)

# Validate the model
val_y = storybooks_dataframe['reading_level']
val_predictions = predictions
mean_absolute_error = mean_absolute_error(val_y, val_predictions)
print(basename(__file__), f'mean_absolute_error: {mean_absolute_error}')

# Write the Mean Absolute Error (MAE) to a text file
with open('step3_2_mean_absolute_error.txt', 'w') as file:
    file.write(str(mean_absolute_error))

# Calculate the accuracy score
accuracy_score = accuracy_score(val_y, val_predictions)
print(basename(__file__), f'accuracy_score: {accuracy_score}')

# Write the accuracy score to a text file
with open('step3_2_accuracy_score.txt', 'w') as file:
    file.write(str(accuracy_score))
