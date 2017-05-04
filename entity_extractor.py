from __future__ import unicode_literals, print_function

from spacy.en import English
import sys


def extract_entities(text):
    nlp = English()
    entities = nlp(text).ents
    ents = [ents for ents in entities if ents.label_ in ["PERSON"]]
    return list(map(to_entity, ents))


def to_entity(entity):
    return entity.text, entity.label_


def debug(ents):
    for entity in ents:
        print(entity)
        # print(entity.text, entity.label_, [w.tag_ for w in entity])


if __name__ == '__main__':
    print(extract_entities(sys.argv[1]))
