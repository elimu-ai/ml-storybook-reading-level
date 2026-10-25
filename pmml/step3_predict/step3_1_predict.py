import os
import pandas
import pickle

# Read the preprocessed test data CSV into a DataFrame
storybooks_csv_path = '../step1_prepare/step1_3_storybooks_test.csv'
print(os.path.basename(__file__), 'storybooks_csv_path: {}'.format(storybooks_csv_path))
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)

# Load the saved model
print(os.path.basename(__file__), 'Loading model...')
with open('../step2_train/step2_1_model.pkl', 'rb') as file:
    reading_level_model = pickle.load(file)

# Select the prediction features (Updated to match features seen at fit time)
storybook_features = [
    'chapter_count', 
    'paragraph_count', 
    'word_count', 
    'flesch_kincaid_grade', 
    'lexile_score'
]

# Make predictions using the updated features array
print(os.path.basename(__file__), 'Making predictions...')
predictions_array = reading_level_model.predict(storybooks_dataframe[storybook_features])

# Print predictions structure or append them to check performance
storybooks_dataframe['predicted_reading_level'] = predictions_array
print(os.path.basename(__file__), f'Predictions complete! Sample output:\n{storybooks_dataframe.head()}')
