#!/usr/bin/env python
import sys
import entity_extractor
from collections import Counter


def to_list(entity):
    return (entity[0],entity[1])


if __name__ == '__main__':
    if sys.argv[1] != '-r':
        entities = entity_extractor.extract_entities_from_file(sys.argv[1])
        values = list(map(to_list, entities))
        z = Counter(values)
        for e in z:
            print("".join(e[0].splitlines()).strip(),",", e[1].strip(),",",z.get(e))
    else:
        entities = entity_extractor.extract_entities_from_file(sys.argv[2])
        values = list(map(to_list, entities))
        print(entities)
        print("v ", values)
        for e in values:
            print(e)
