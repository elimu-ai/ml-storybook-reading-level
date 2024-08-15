import os
import pandas
from pypmml import Model
from sklearn.metrics import mean_absolute_error

# Load Predictive Model Markup Language (PMML) model
model_pmml_path = '../step2_train/step2_2_model.pmml'
print(os.path.basename(__file__), 'model_pmml_path: {}'.format(model_pmml_path))
reading_level_model = Model.load(model_pmml_path)
print(os.path.basename(__file__), 'reading_level_model: {}'.format(reading_level_model))

# Load test data
storybooks_csv_path = 'step3_1_storybooks_test.csv'
print(os.path.basename(__file__), 'storybooks_csv_path: {}'.format(storybooks_csv_path))
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)
print(os.path.basename(__file__), 'storybooks_dataframe:\n{}'.format(storybooks_dataframe))

# Predict
storybook_features = ['id']
predictions = reading_level_model.predict(storybooks_dataframe[storybook_features])
print(os.path.basename(__file__), 'predictions:\n{}'.format(predictions))
print(os.path.basename(__file__), 'type(predictions):\n{}'.format(type(predictions)))

# Write the DataFrame to a CSV file
predictions.to_csv('step3_2_predictions.csv', index=False)

# Validate the model
val_y = storybooks_dataframe['reading_level']
val_predictions = predictions
mean_absolute_error = mean_absolute_error(val_y, val_predictions)
print(os.path.basename(__file__), 'mean_absolute_error: {}'.format(mean_absolute_error))

# Write the Mean Absolute Error (MAE) to a text file
with open('step3_2_mean_absolute_error.txt', 'w') as file:
    file.write(str(mean_absolute_error))
