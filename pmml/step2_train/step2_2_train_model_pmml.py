import os
import pandas
from sklearn.tree import DecisionTreeRegressor
from sklearn2pmml import PMMLPipeline, sklearn2pmml

# Read the preprocessed training data CSV into a DataFrame
storybooks_csv_path = '../step1_prepare/step1_3_storybooks_train.csv'
print(os.path.basename(__file__), 'storybooks_csv_path: {}'.format(storybooks_csv_path))
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)
print(os.path.basename(__file__), 'storybooks_dataframe:\n{}'.format(storybooks_dataframe))
print(os.path.basename(__file__), 'storybooks_dataframe.columns:\n{}'.format(storybooks_dataframe.columns))

# Select the prediction target
y = storybooks_dataframe[['reading_level']]
print(os.path.basename(__file__), 'type(y): {}'.format(type(y)))
print(os.path.basename(__file__), 'y:\n{}'.format(y))

# Choose features
X = storybooks_dataframe[['chapter_count', 'paragraph_count', 'word_count']]
print(os.path.basename(__file__), 'type(X): {}'.format(type(X)))
print(os.path.basename(__file__), 'X:\n{}'.format(X))

# Define model
print(os.path.basename(__file__), 'Defining model...')
reading_level_model = PMMLPipeline([('regressor', DecisionTreeRegressor(random_state=1))])
print(os.path.basename(__file__), 'reading_level_model: {}'.format(reading_level_model))

# Fit model
print(os.path.basename(__file__), 'Fitting model...')
reading_level_model.fit(X, y)

# Save model
print(os.path.basename(__file__), 'Saving model...')
sklearn2pmml(reading_level_model, 'step2_2_model.pmml')
