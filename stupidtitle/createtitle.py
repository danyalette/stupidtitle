import random as r
import words
import re


def createTitle(
        articles=words.ARTICLES,
        nouns=words.NOUNS,
        prepositions=words.PREPOSITIONS,
        adjectives=words.ADJECTIVES):

    # water down lists
    articles = articles + ([''] * (len(articles)/2))
    adjectives = adjectives + ([''] * len(adjectives))

    noun_count = r.choice([1,1,2,2,2,3])
    title_parts = []
    for i in range(noun_count):
        part = [
            r.choice(articles),
            r.choice(adjectives),
            r.choice(nouns)
        ]
        if i < noun_count - 1:
            part.append(r.choice(prepositions))

        # filter empty strings
        part = filter(None, part)

        # convert article "a" to "an"
        if part[0] == "a" and re.search('[aeiou]', part[1][0]):
            part[0] = "an"

        title_parts.append(' '.join(part))

    return ' '.join(title_parts).title()