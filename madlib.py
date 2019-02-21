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


def get_story_keywords():
    """Function that retrieves the story template.
    """
    madlib_keywords = []
    with open('./assets/story_template', 'r') as rf:
        with open('./assets/madlib_keywords.txt', 'w') as wf:
            for line in rf:
                template_keywords = re.findall('{([^}]*)}', line)
                if template_keywords != ['']:
                    for keyword in template_keywords:
                        wf.write(keyword + '\n')


def get_user_words():
    """Function that asks for the user to enter silly words.
    """
    with open('.assets/madlib_keywords', 'r') as rf:
        with open('.assets/story_template', 'w') as wf:
            for line in rf:
                user_word = input('Enter %s : ' % line)
                re.sub('{([^}]*)}', user_word, str)


if __name__ == "__main__":
    get_story_keywords()
    get_user_words()
