from os.path import basename
from matplotlib import pyplot
import pandas

# Read the preprocessed storybooks CSV into a DataFrame
storybooks_csv_path = 'step1_2_storybooks.csv'
print(basename(__file__), f'storybooks_csv_path: {storybooks_csv_path}')
storybooks_dataframe = pandas.read_csv(storybooks_csv_path)

for label in storybooks_dataframe.columns[2:]:
    print(f'label: {label}')

    # Scatter
    pyplot.scatter(storybooks_dataframe['reading_level'], storybooks_dataframe[label], alpha=0.5)
    pyplot.xlabel('reading_level')
    pyplot.ylabel(label)
    pyplot.savefig(f'step1_4_{label}_scatter.png')
    pyplot.clf()

    # Histogram
    level_1 = storybooks_dataframe[storybooks_dataframe['reading_level'] == 1][label]
    level_2 = storybooks_dataframe[storybooks_dataframe['reading_level'] == 2][label]
    level_3 = storybooks_dataframe[storybooks_dataframe['reading_level'] == 3][label]
    level_4 = storybooks_dataframe[storybooks_dataframe['reading_level'] == 4][label]
    pyplot.hist(level_1, label='LEVEL1', alpha=0.5)
    pyplot.hist(level_2, label='LEVEL2', alpha=0.5)
    pyplot.hist(level_3, label='LEVEL3', alpha=0.5)
    pyplot.hist(level_4, label='LEVEL4', alpha=0.5)
    pyplot.xlabel(label)
    pyplot.legend()
    pyplot.savefig(f'step1_4_{label}_hist.png')
    pyplot.clf()