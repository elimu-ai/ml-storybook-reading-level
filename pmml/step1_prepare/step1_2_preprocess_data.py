import os
import pandas

# Read the original storybooks CSV into a DataFrame
storybooks_csv_path = 'step1_1_storybooks.csv'
print(os.path.basename(__file__), 'storybooks_csv_path: {}'.format(storybooks_csv_path))
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)

# Drop unnecessary columns
storybooks_dataframe = storybooks_dataframe[['id', 'reading_level']]
print(os.path.basename(__file__), 'storybooks_dataframe (after dropping unnecessary columns):\n{}'.format(storybooks_dataframe))

# Drop missing values
storybooks_dataframe = storybooks_dataframe.dropna()
print(os.path.basename(__file__), 'storybooks_dataframe (after dropping missing values):\n{}'.format(storybooks_dataframe))

# Extract number from reading level (e.g. 'LEVEL1' --> '1')
storybooks_dataframe['reading_level'] = storybooks_dataframe['reading_level'].str.extract('(\\d+)')
print(os.path.basename(__file__), 'storybooks_dataframe (after converting texts to numbers):\n{}'.format(storybooks_dataframe))

# Write the DataFrame to a CSV file
storybooks_dataframe.to_csv('step1_2_storybooks.csv', index=False)
