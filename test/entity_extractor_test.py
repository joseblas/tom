import unittest
import entity_extractor


class TestStringMethods(unittest.TestCase):
    def test_contains_no_people(self):
        sample = u"Let me say right away that the majority of the amendments are technical clarifications."
        ents = entity_extractor.extract_entities(sample)
        self.assertEqual(len(ents), 0, " Should be no people")

    def test_contains_one_person(self):
        sample = u"It would be most remiss of me not also to thank Lord Walker of Gestingthorpe for his distinguished "
        ents = entity_extractor.extract_entities(sample)
        self.assertEqual(len(ents), 1, " Should be one person")

    def test_contains_many_people(self):
        sample = u"It would be most remiss of me not also to thank Lord Walker of Gestingthorpe for his distinguished " \
                 u"chairmanship of the Select Committee that considered the petitions against the Bill in the Lords, "
        ents = entity_extractor.extract_entities(sample)
        self.assertEqual(len(ents), 2, " Should be one person")

    def test_contains_many_people_and_other_entities(self):
        sample = u"Let me say right away that the majority of the amendments are technical clarifications, " \
                 u"corrections and updated references. The Government accept all the amendments to the Bill " \
                 u"made by the Lords. I will provide some comment on the amendments of substance. Before I do so, " \
                 u"I would like to take the opportunity to thank the Lords for their scrutiny of the Bill. " \
                 u"I pay particular gratitude to Lord Ahmad of Wimbledon for having very skilfully steered the passage " \
                 u"of the Bill through the other place, and to my noble Friends Lord Viscount Younger and Baroness " \
                 u"Buscombe for their diligent work in assisting Lord Ahmad during the Lords stages of the Bill. " \
                 u"It would be most remiss of me not also to thank Lord Walker of Gestingthorpe for his distinguished " \
                 u"chairmanship of the Select Committee that considered the petitions against the Bill in the Lords, " \
                 u"and to thank the other members of the Committee."
        ents = entity_extractor.extract_entities(sample)
        self.assertEqual(len(ents), 7, " Should be one person")

    def test_contains_many_people_and_other_entities_and_cyrillic_entities(self):
        sample = u"Let me say right away that the majority of the amendments are technical clarifications, " \
                 u"corrections and updated references. The Government accept all the amendments to the Bill " \
                 u"made by the Lords. I will provide some comment on the amendments of substance. Before I do so, " \
                 u"I would like to take the opportunity to thank the Lords for their scrutiny of the Bill. " \
                 u"I pay particular gratitude to Lord Ahmad of Wimbledon for having very skilfully steered the passage " \
                 u"of the Bill through the other place, and to my noble Friends Lord Viscount Younger and Baroness " \
                 u"Buscombe for their diligent work in assisting Lord Ahmad during the Lords stages of the Bill. " \
                 u"It would be most remiss of me not also to thank Lord Walker of Gestingthorpe for his distinguished " \
                 u"chairmanship of the Select Committee that considered the petitions against the Bill in the Lords, " \
                 u"and to thank the other members of the Committee." \
                 u"Поздрави, Камен."
        # 'Best Regards, Kamen' in Bulgarian
        ents = entity_extractor.extract_entities(sample)
        self.assertEqual(len(ents), 7, " Should be one person")


if __name__ == '__main__':
    unittest.main()