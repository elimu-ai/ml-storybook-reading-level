from os.path import basename
import pandas
from sklearn.model_selection import train_test_split

# Read the preprocessed storybooks CSV into a DataFrame
storybooks_csv_path = 'step1_2_storybooks.csv'
print(basename(__file__), f'storybooks_csv_path: {storybooks_csv_path}')
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)

# Split the data into training and validation data
X = storybooks_dataframe[['id', 'chapter_count', 'paragraph_count']]
y = storybooks_dataframe[['reading_level']]
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=0)
print(basename(__file__), f'train_X: \n{train_X}')
print(basename(__file__), f'train_y: \n{train_y}')
print(basename(__file__), f'test_X: \n{test_X}')
print(basename(__file__), f'test_y: \n{test_y}')

# Write the DataFrames to CSV files
storybooks_dataframe_train = pandas.concat([train_X, train_y], axis=1)
storybooks_dataframe_train.to_csv('step1_3_storybooks_train.csv', index=False)
storybooks_dataframe_test = pandas.concat([test_X, test_y], axis=1)
storybooks_dataframe_test.to_csv('step1_3_storybooks_test.csv', index=False)
