import unittest
import entity_extractor
import codecs


class EntityExtractorGoldStandard(unittest.TestCase):
    def test_gold_standard_measure(self):
        ents = entity_extractor.extract_entities_from_file("Lee Valley Regional Park (Amendment) 2017-02-22.txt")
        entities = list(map(to_text, list(set(ents))))
        with codecs.open("./test/gold_standard_leevalley.csv", "r", "utf-8") as f:
            mp = list(map(lambda line: line.strip() in entities, f))
        precision = len(list(filter(lambda data: data == True, mp))) / len(mp)
        recall = len(list(filter(lambda data: data == True, mp))) / len(entities)
        print("Precision: ", precision, len(list(filter(lambda data: data == True, mp))) , len(mp))
        print("recall: ", recall, len(list(filter(lambda data: data == True, mp))) , len(entities))
        print("Balanced F1: ", (2 * precision * recall)/(precision+recall))


def to_text(entity):
    return entity[0]


if __name__ == '__main__':
    unittest.main()