from os.path import basename

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
