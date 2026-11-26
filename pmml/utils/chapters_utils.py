from os.path import basename
import re
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

# Sentence-ending punctuation: Latin (. ! ?) and the Devanagari danda (\u0964)
SENTENCE_SPLIT_PATTERN = re.compile(r'[.!?\u0964]+')

def get_sentence_count(chapters_json):
    print(basename(__file__), 'get_sentence_count')
    sentence_count = 0
    for chapter in chapters_json:
        for paragraph in chapter["storyBookParagraphs"]:
            # Count the non-empty pieces between sentence-ending punctuation marks
            pieces = SENTENCE_SPLIT_PATTERN.split(paragraph["originalText"])
            sentence_count += sum(1 for piece in pieces if piece.strip())
    print(basename(__file__), f'sentence_count: {sentence_count}')
    return sentence_count

def get_avg_sentence_length(chapters_json):
    print(basename(__file__), 'get_avg_sentence_length')
    sentence_count = get_sentence_count(chapters_json)
    if sentence_count == 0:
        return 0
    avg_sentence_length = get_word_count(chapters_json) / sentence_count
    print(basename(__file__), f'avg_sentence_length: {avg_sentence_length}')
    return avg_sentence_length
