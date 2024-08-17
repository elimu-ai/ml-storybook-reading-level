import os
import pandas

# Read the storybooks CSV into a DataFrame
storybooks_csv_url = ('https://raw.githubusercontent.com/elimu-ai/webapp/main/src/main/resources/db/content_PROD'
                          '/hin/storybooks.csv')
print(os.path.basename(__file__), 'storybooks_csv_url: {}'.format(storybooks_csv_url))
storybooks_dataframe = pandas.read_csv(storybooks_csv_url)
print(os.path.basename(__file__), 'storybooks_dataframe:\n{}'.format(storybooks_dataframe))

# Write the DataFrame to a CSV file
storybooks_dataframe.to_csv('step1_1_storybooks.csv', index=False)
