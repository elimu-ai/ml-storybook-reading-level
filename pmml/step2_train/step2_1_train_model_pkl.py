import os
import pandas
import pickle
from sklearn.tree import DecisionTreeRegressor

# Read the preprocessed storybooks CSV into a DataFrame
storybooks_csv_path = '../step1_prepare/step1_2_storybooks.csv'
print(os.path.basename(__file__), 'storybooks_csv_path: {}'.format(storybooks_csv_path))
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)
print(os.path.basename(__file__), 'storybooks_dataframe:\n{}'.format(storybooks_dataframe))
print(os.path.basename(__file__), 'storybooks_dataframe.columns:\n{}'.format(storybooks_dataframe.columns))

# Select the prediction target
y = storybooks_dataframe['reading_level']
print(os.path.basename(__file__), 'y:\n{}'.format(y))

# Choose features
storybook_features = ['id']
print(os.path.basename(__file__), 'storybook_features: {}'.format(storybook_features))
X = storybooks_dataframe[storybook_features]
print(os.path.basename(__file__), 'X:\n{}'.format(X))

# Define model
reading_level_model = DecisionTreeRegressor(random_state=1)
print(os.path.basename(__file__), 'reading_level_model:\n{}'.format(reading_level_model))

# Fit model
reading_level_model.fit(X, y)

# Save model
with open('step2_1_model.pkl', 'wb') as file:
    pickle.dump(reading_level_model, file, protocol=5)
