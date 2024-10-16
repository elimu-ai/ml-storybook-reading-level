from sklearn.metrics import accuracy_score, mean_absolute_error
import pandas
from os.path import basename

# Load the preprocessed test data CSV into a DataFrame
storybooks_csv_path = '../step1_prepare/step1_3_storybooks_test.csv'
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)
val_y = storybooks_dataframe['reading_level']

# Load Predicted values from step3_2_predictions.csv
val_predictions = pandas.read_csv('../step3_predict/step3_2_predictions.csv')

accuracy = accuracy_score(val_y, val_predictions)
print(basename(__file__), f'accuracy_score: {accuracy}')

mae = mean_absolute_error(val_y, val_predictions)
print(basename(__file__), f'accuracy_score: {mae}')

# Save the results to a file for the GitHub workflow to read
with open('Metrics_output.txt', 'w') as f:
    f.write(f'accuracy_score: {accuracy}\n')
    f.write(f'MAE: {mae}\n')
