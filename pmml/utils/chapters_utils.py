from os.path import basename
import string

'''json
[
  {
    "image": {
      "id": 447
    },
    "sortOrder": 0,
    "id": 99,
        "storyBookParagraphs": [
      {
        "originalText": "Earth is the planet that we live on. Currently no other planet is known to contain life.",
        "sortOrder": 0,
        "id": 142
      }
    ]
  },
  {
    "image": {
      "id": 448
    },
    "sortOrder": 1,
    "id": 100,
    "storyBookParagraphs": [
      {
        "originalText": "The Earth is in danger because of global warming. Global warming is caused by too much carbon dioxide in the atmosphere. Carbon dioxide is a gas which traps heat in the Earth. Without it Earth's heat would flow out and Earth would freeze.",
        "sortOrder": 0,
        "id": 143
      }
    ]
  },
  {
    "image": {
      "id": 449
    },
    "sortOrder": 2,
    "id": 101,
    "storyBookParagraphs": [
      {
        "originalText": "The cars we drive create lots of carbon dioxide. We should walk more or ride a bicycle.",
        "sortOrder": 0,
        "id": 144
      }
    ]
  }
]
'''
def get_chapter_count(chapters_json):
    print(basename(__file__), 'get_chapter_count')
    chapter_count = len(chapters_json)
    print(basename(__file__), f'chapter_count: {chapter_count}')
    return chapter_count

def get_paragraph_count(chapters_json):
    print(basename(__file__), 'get_paragraph_count')
    paragraph_count = 0
    for chapter in chapters_json:
        print(basename(__file__), f'chapter["sortOrder"]: {chapter["sortOrder"]}')
        for paragraph in chapter["storyBookParagraphs"]:
            print(basename(__file__), f'paragraph: {paragraph}')
            paragraph_count += 1
    return paragraph_count

def get_word_count(chapters_json):
    print(basename(__file__), 'get_word_count')
    word_count = 0
    for chapter in chapters_json:
        print(basename(__file__), f'chapter["sortOrder"]: {chapter["sortOrder"]}')
        for paragraph in chapter["storyBookParagraphs"]:
            print(basename(__file__), f'paragraph: {paragraph}')
            words = paragraph["originalText"].split()
            print(basename(__file__), f'words: {words}')
            word_count += len(words)
    return word_count

def get_avg_sentence_length(chapters_json):
    """Calculate the average number of words per sentence across all paragraphs.
    
    Sentences are identified by ending punctuation (. ! ?). If a paragraph has
    words but no ending punctuation, it is treated as a single sentence.
    Returns 0.0 if there are no sentences.
    """
    print(basename(__file__), 'get_avg_sentence_length')
    total_words = 0
    total_sentences = 0
    sentence_endings = set('.!?')
    for chapter in chapters_json:
        print(basename(__file__), f'chapter["sortOrder"]: {chapter["sortOrder"]}')
        for paragraph in chapter["storyBookParagraphs"]:
            print(basename(__file__), f'paragraph: {paragraph}')
            text = paragraph["originalText"]
            words = text.split()
            word_count = len(words)
            total_words += word_count
            # Count sentence-ending punctuation
            sentence_count = sum(1 for char in text if char in sentence_endings)
            if sentence_count == 0 and word_count > 0:
                sentence_count = 1
            total_sentences += sentence_count
    if total_sentences == 0:
        return 0.0
    avg = total_words / total_sentences
    print(basename(__file__), f'avg_sentence_length: {avg}')
    return avg
