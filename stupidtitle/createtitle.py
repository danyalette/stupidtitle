import random as r
import words


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

        title_parts.append(' '.join(filter(None,part)))

    return ' '.join(title_parts).title()