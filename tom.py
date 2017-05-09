#!/usr/bin/env python
import sys
import entity_extractor
from collections import Counter

print('Loading function')


def to_list(entity):
    return entity[0]


if __name__ == '__main__':
    print(sys.argv)
    if sys.argv[1] != '-r':
        entities = entity_extractor.extract_entities_from_file(sys.argv[1])
        values = list(map(to_list, entities))
        z = Counter(values)
        print(z)
        for e in z:
            print(e.strip(),",",z.get(e))
    else:
        entities = entity_extractor.extract_entities_from_file(sys.argv[2])
        values = list(map(to_list, entities))
        # print(entities)
        # print("v ", values)
        for e in values:
            print(e)
