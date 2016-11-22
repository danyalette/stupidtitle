import random as r
import words


def createTitle(articles=words.ARTICLES, nouns=words.NOUNS, prepositions=words.PREPOSITIONS):
    noun_count = r.choice([1,1,2,2,2,3])
    title_parts = []
    for i in range(noun_count):
        part = ''
        if i == noun_count - 1:
            title_parts.append(
                ' '.join([
                    r.choice(articles),
                    r.choice(nouns)
                ]).strip()
            )
        else:
            title_parts.append(
                ' '.join([
                    r.choice(articles),
                    r.choice(nouns),
                    r.choice(prepositions)
                ]).strip()
            )

    return ' '.join(title_parts).strip().title()