import json
from os.path import basename, dirname, abspath
import pandas
import sys

parent_dir = dirname(dirname(abspath(__file__)))
sys.path.append(parent_dir)
from utils import chapters_utils

# Read the original storybooks CSV into a DataFrame
storybooks_csv_path = 'step1_1_storybooks.csv'
print(basename(__file__), f'storybooks_csv_path: {storybooks_csv_path}')
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)

# For each row in the DataFrame, extract information from the JSON string stored in the `chapters` column
storybooks_dataframe['chapter_count'] = 0
storybooks_dataframe['paragraph_count'] = 0
for index in storybooks_dataframe.index:
    print(basename(__file__), f'index: {index}')
    chapters = storybooks_dataframe.loc[index]['chapters']
    chapters_json = json.loads(chapters)

    chapter_count = chapters_utils.get_chapter_count(chapters_json)
    storybooks_dataframe.loc[index, 'chapter_count'] = chapter_count

    paragraph_count = chapters_utils.get_paragraph_count(chapters_json)
    storybooks_dataframe.loc[index, 'paragraph_count'] = paragraph_count
print(basename(__file__), f'storybooks_dataframe (after extracting data from `chapters` column): \n{storybooks_dataframe}')

# Drop unnecessary columns
storybooks_dataframe = storybooks_dataframe[['id', 'reading_level', 'chapter_count', 'paragraph_count']]
print(basename(__file__), f'storybooks_dataframe (after dropping unnecessary columns): \n{storybooks_dataframe}')

# Drop missing values
storybooks_dataframe = storybooks_dataframe.dropna()
print(basename(__file__), f'storybooks_dataframe (after dropping missing values): \n{storybooks_dataframe}')

# Extract number from reading level (e.g. 'LEVEL1' --> '1')
storybooks_dataframe['reading_level'] = storybooks_dataframe['reading_level'].str.extract('(\\d+)')
print(basename(__file__), f'storybooks_dataframe (after converting texts to numbers): \n{storybooks_dataframe}')

# Write the DataFrame to a CSV file
storybooks_dataframe.to_csv('step1_2_storybooks.csv', index=False)
