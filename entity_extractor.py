from __future__ import unicode_literals, print_function

from spacy.en import English
import sys
import codecs

def extract_entities_from_file(path):
    return extract_entities(read_file(path))


def extract_entities(text):
    nlp = English()
    entities = nlp(text).ents
    ents = [ents for ents in entities if ents.label_ in ["PERSON", "ORG", "LOC", "EVENT"]]
    return list(map(to_entity, ents))


def to_entity(entity):
    return entity.text.strip(), entity.label_


def read_file(path):
    file_content = codecs.open(path, "r", "utf-8")
    content = file_content.read()
    file_content.close()
    return content


if __name__ == '__main__':
    print(sys.argv)
    if sys.argv[1] == '-f':
        file = sys.argv[2]
        print(extract_entities(read_file(file)))
    else:
        print(extract_entities(sys.argv[1]))
