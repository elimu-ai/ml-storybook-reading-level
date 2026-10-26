import json
from os.path import basename, dirname, abspath
import pandas
import sys
import textstat  # Library for calculating text complexity metrics

parent_dir = dirname(dirname(abspath(__file__)))
sys.path.append(parent_dir)
from utils import chapters_utils

# Read the original storybooks CSV into a DataFrame
storybooks_csv_path = 'step1_1_storybooks.csv'
print(basename(__file__), f'storybooks_csv_path: {storybooks_csv_path}')
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)

# Initialize new columns for text complexity metrics
storybooks_dataframe['chapter_count'] = 0
storybooks_dataframe['paragraph_count'] = 0
storybooks_dataframe['word_count'] = 0
storybooks_dataframe['flesch_kincaid_grade'] = 0.0
storybooks_dataframe['lexile_score'] = 0.0

for index in storybooks_dataframe.index:
    print(basename(__file__), f'index: {index}')
    chapters = storybooks_dataframe.loc[index]['chapters']
    chapters_json = json.loads(chapters)

    chapter_count = chapters_utils.get_chapter_count(chapters_json)
    storybooks_dataframe.loc[index, 'chapter_count'] = chapter_count

    paragraph_count = chapters_utils.get_paragraph_count(chapters_json)
    storybooks_dataframe.loc[index, 'paragraph_count'] = paragraph_count

    word_count = chapters_utils.get_word_count(chapters_json)
    storybooks_dataframe.loc[index, 'word_count'] = word_count

    # --- ADDED BLOCK: Calculate Flesch-Kincaid and Lexile ---
    # Extract raw text from the chapters JSON structure
    full_text = ""
    try:
        paragraphs = []
        for chapter in chapters_json:
            if 'paragraphs' in chapter:
                for paragraph in chapter['paragraphs']:
                    if 'words' in paragraph:
                        # Reconstruct text if paragraph contains a list of word objects
                        paragraphs.append(" ".join([w.get('text', '') for w in paragraph.get('words', [])]))
                    elif 'text' in paragraph:
                        # Direct text field extraction
                        paragraphs.append(paragraph['text'])
        full_text = " ".join(paragraphs)
    except Exception:
        full_text = ""        

    # Calculate metrics only if text is valid and words exist
    if full_text.strip() and word_count > 0:
        # Compute Flesch-Kincaid Grade Level
        fk_grade = textstat.flesch_kincaid_grade(full_text)
        
        # Approximate Lexile score based on the reading grade standard formula
        lexile = (fk_grade * 145) + 150
        if lexile < 0: 
            lexile = 0.0
    else:
        fk_grade = 0.0
        lexile = 0.0

    storybooks_dataframe.loc[index, 'flesch_kincaid_grade'] = fk_grade
    storybooks_dataframe.loc[index, 'lexile_score'] = lexile
    # -------------------------------------------------------------

print(basename(__file__), f'storybooks_dataframe (after extracting data from `chapters` column): \n{storybooks_dataframe}')

# Update the list of columns to include the newly extracted features
storybooks_dataframe = storybooks_dataframe[[
    'id', 'reading_level', 'chapter_count', 'paragraph_count', 'word_count', 
    'flesch_kincaid_grade', 'lexile_score'
]]
print(basename(__file__), f'storybooks_dataframe (after dropping unnecessary columns): \n{storybooks_dataframe}')

# Drop missing values
storybooks_dataframe = storybooks_dataframe.dropna()
print(basename(__file__), f'storybooks_dataframe (after dropping missing values): \n{storybooks_dataframe}')

# Extract number from reading level (e.g. 'LEVEL1' --> '1')
storybooks_dataframe['reading_level'] = storybooks_dataframe['reading_level'].str.extract('(\\d+)')
print(basename(__file__), f'storybooks_dataframe (after converting texts to numbers): \n{storybooks_dataframe}')

# Write the DataFrame to a CSV file
storybooks_dataframe.to_csv('step1_2_storybooks.csv', index=False)
