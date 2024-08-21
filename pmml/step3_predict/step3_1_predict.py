import os
import pandas
import pickle

# Load model
model_pkl_path = '../step2_train/step2_1_model.pkl'
print(os.path.basename(__file__), 'model_pkl_path: {}'.format(model_pkl_path))
with open(model_pkl_path, 'rb') as file:
    reading_level_model = pickle.load(file)
print(os.path.basename(__file__), 'reading_level_model: {}'.format(reading_level_model))

# Read the preprocessed training data CSV into a DataFrame
storybooks_csv_path = '../step1_prepare/step1_3_storybooks_test.csv'
print(os.path.basename(__file__), 'storybooks_csv_path: {}'.format(storybooks_csv_path))
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)
print(os.path.basename(__file__), 'storybooks_dataframe:\n{}'.format(storybooks_dataframe))

# Predict
storybook_features = ['chapter_count', 'paragraph_count', 'word_count']
predictions_array = reading_level_model.predict(storybooks_dataframe[storybook_features])
print(os.path.basename(__file__), 'predictions_array:\n{}'.format(predictions_array))
print(os.path.basename(__file__), 'type(predictions_array):\n{}'.format(type(predictions_array)))

# Convert from N-dimensional array to DataFrame
predictions_dataframe = pandas.DataFrame(predictions_array, columns=['reading_level'])
print(os.path.basename(__file__), 'predictions_dataframe:\n{}'.format(predictions_dataframe))
print(os.path.basename(__file__), 'type(predictions_dataframe):\n{}'.format(type(predictions_dataframe)))

# Write the DataFrame to a CSV file
predictions_dataframe.to_csv('step3_1_predictions.csv', index=False)
