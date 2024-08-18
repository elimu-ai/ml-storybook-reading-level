import pandas as pd
import json
import re
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
from sklearn.preprocessing import LabelEncoder
import subprocess
import download_nltk_data

# Call the function to ensure NLTK data is available
download_nltk_data.download_nltk_data()

# Select environment (TEST/PROD)
ENVIRONMENT = "PROD"

# Select language
# See https://github.com/elimu-ai/model/blob/main/src/main/java/ai/elimu/model/v2/enums/Language.java
LANGUAGE = "HIN"

RAW_DATA_DIR = "./env-" + ENVIRONMENT + "/lang-" + LANGUAGE + "/data"
print(f"RAW_DATA_DIR: {RAW_DATA_DIR}")

# Load the storybooks
storybooks_pd = pd.read_csv(RAW_DATA_DIR + "/storybooks.csv")
print(f"storybooks_pd: \n{storybooks_pd}")

#Each chapter details are stored in the chapters column of the dataframe in JSON format, hence extracting only paragraphs of the book.
def extract_chapters_text(chapters_json):
    try:
        chapters = json.loads(chapters_json)
        return ' '.join(paragraph['originalText'] for chapter in chapters for paragraph in chapter.get('storyBookParagraphs', []))
    except (TypeError, json.JSONDecodeError):
        return ''

#Now the 'combined_chapters_text' column contains all the chapter paragraphs
storybooks_pd['combined_chapters_text'] = storybooks_pd['chapters'].apply(extract_chapters_text)
print(f"storybooks_pd_new: \n{storybooks_pd}")

#Removing stop words
def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        stopwords = set(file.read().splitlines())
    return stopwords

RAW_HINDI_STOPWORDS = "./env-" + ENVIRONMENT + "/lang-" + LANGUAGE

# Define stopwords file path
stopwords_file_path = RAW_HINDI_STOPWORDS + "/hindi_stopwords.txt"
hindi_stopwords = load_stopwords(stopwords_file_path)

#Preprocess the data
def preprocess_text(text):
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    tokens = [word for word in tokens if word not in hindi_stopwords]
    # Join tokens back into a string
    return ' '.join(tokens)

# Apply preprocessing to each relevant column
storybooks_pd['preprocessed_title'] = storybooks_pd['title'].apply(preprocess_text)
storybooks_pd['preprocessed_description'] = storybooks_pd['description'].apply(preprocess_text)
storybooks_pd['preprocessed_combined_chapters_text'] = storybooks_pd['combined_chapters_text'].apply(preprocess_text)

# Vectorization using TF-IDF
tfidf_vectorizer = TfidfVectorizer()
title_vectors = tfidf_vectorizer.fit_transform(storybooks_pd['preprocessed_title'])
description_vectors = tfidf_vectorizer.fit_transform(storybooks_pd['preprocessed_description'])
chapters_vectors = tfidf_vectorizer.fit_transform(storybooks_pd['preprocessed_combined_chapters_text'])

# Combine features(Used for training the ML model)
combined_features = hstack([title_vectors, description_vectors, chapters_vectors])

#reading_level' is the target variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(storybooks_pd['reading_level'])