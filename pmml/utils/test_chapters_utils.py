import chapters_utils
import json

def test_get_chapter_count_when_no_paragraphs():
    # Load JSON from string
    chapters_json = json.loads('[{"image":{"id":467},"sortOrder":0,"id":120,"storyBookParagraphs":[]},{"image":{"id":468},"sortOrder":1,"id":121,"storyBookParagraphs":[]},{"image":{"id":469},"sortOrder":2,"id":122,"storyBookParagraphs":[]},{"image":{"id":470},"sortOrder":3,"id":123,"storyBookParagraphs":[]},{"image":{"id":471},"sortOrder":4,"id":124,"storyBookParagraphs":[]},{"image":{"id":472},"sortOrder":5,"id":125,"storyBookParagraphs":[]},{"image":{"id":473},"sortOrder":6,"id":126,"storyBookParagraphs":[]},{"image":{"id":474},"sortOrder":7,"id":127,"storyBookParagraphs":[]},{"image":{"id":475},"sortOrder":8,"id":128,"storyBookParagraphs":[]},{"image":{"id":476},"sortOrder":9,"id":129,"storyBookParagraphs":[]},{"image":{"id":477},"sortOrder":10,"id":130,"storyBookParagraphs":[]},{"image":{"id":478},"sortOrder":11,"id":131,"storyBookParagraphs":[]},{"image":{"id":479},"sortOrder":12,"id":132,"storyBookParagraphs":[]},{"image":{"id":480},"sortOrder":13,"id":133,"storyBookParagraphs":[]},{"image":{"id":481},"sortOrder":14,"id":134,"storyBookParagraphs":[]},{"image":{"id":482},"sortOrder":15,"id":135,"storyBookParagraphs":[]},{"image":{"id":483},"sortOrder":16,"id":136,"storyBookParagraphs":[]},{"image":{"id":484},"sortOrder":17,"id":137,"storyBookParagraphs":[]},{"image":{"id":485},"sortOrder":18,"id":138,"storyBookParagraphs":[]},{"image":{"id":486},"sortOrder":19,"id":139,"storyBookParagraphs":[]},{"image":{"id":487},"sortOrder":20,"id":140,"storyBookParagraphs":[]},{"image":{"id":488},"sortOrder":21,"id":141,"storyBookParagraphs":[]},{"image":{"id":489},"sortOrder":22,"id":142,"storyBookParagraphs":[]},{"image":{"id":490},"sortOrder":23,"id":143,"storyBookParagraphs":[]},{"image":{"id":491},"sortOrder":24,"id":144,"storyBookParagraphs":[]},{"image":{"id":492},"sortOrder":25,"id":145,"storyBookParagraphs":[]},{"image":{"id":493},"sortOrder":26,"id":146,"storyBookParagraphs":[]}]')

    # Extract the number of chapters
    chapter_count = chapters_utils.get_chapter_count(chapters_json)

    assert chapter_count == 27

def test_get_chapter_count_when_single_paragraphs():
    # Load JSON from string
    chapters_json = json.loads('[{"image":{"id":447},"sortOrder":0,"id":99,"storyBookParagraphs":[{"originalText":"Earth is the planet that we live on. Currently no other planet is known to contain life.","sortOrder":0,"id":142}]},{"image":{"id":448},"sortOrder":1,"id":100,"storyBookParagraphs":[{"originalText":"The Earth is in danger because of global warming. Global warming is caused by too much carbon dioxide in the atmosphere. Carbon dioxide is a gas which traps heat in the Earth. Without it Earth\'s heat would flow out and Earth would freeze.","sortOrder":0,"id":143}]},{"image":{"id":449},"sortOrder":2,"id":101,"storyBookParagraphs":[{"originalText":"The cars we drive create lots of carbon dioxide. We should walk more or ride a bicycle.","sortOrder":0,"id":144}]}]')

    # Extract the number of chapters
    chapter_count = chapters_utils.get_chapter_count(chapters_json)

    assert chapter_count == 3
