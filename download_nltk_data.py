import nltk

# Download required NLTK data
def download_nltk_data():
    nltk.download('punkt')  # Add other NLTK data downloads as needed
    nltk.download('punkt_tab')

if __name__ == "__main__":
    download_nltk_data()