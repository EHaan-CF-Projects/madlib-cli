import re

INTRO = """
  +++++++++++++++++++++++++++++++++++++++++++
  +          **  CLI MADLIBS  **            +
  +          Welcome CLI MADLIBS!           +
  +  You will be asked to enter a series    +
  +  of words that will fill in a story.    +
  +++++++++++++++++++++++++++++++++++++++++++
"""

print(INTRO)


def get_story_template():
    """Function that retrieves the story template.
    """
    madlib_keywords = []
    with open('./assets/story_template', 'r') as rf:
        with open('./assets/user_madlib.txt', 'w') as wf:
            for line in rf:
                template_keywords = re.findall('{([^}]*)}', line)
                if template_keywords != ['']:
                    for keyword in template_keywords:
                        wf.write(keyword + '\n')

if __name__ == "__main__":
    get_story_template()
