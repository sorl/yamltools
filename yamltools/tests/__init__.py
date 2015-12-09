import unittest
from yamltools import yaml_to_json, json_to_yaml


simple_yaml =\
'''name: me
residence: home
'''

simple_json =\
'''{
    "name": "me",
    "residence": "home"
}'''

hash_yaml =\
'''names:
    first: a
    middle: b
    last: c
'''

hash_json =\
'''{
    "names": {
        "first": "a",
        "middle": "b",
        "last": "c"
    }
}'''


class TestYamlTools(unittest.TestCase):
    def test_y2j_simple(self):
        self.assertEqual(yaml_to_json(simple_yaml), simple_json)

    def test_y2j_hashorder(self):
        self.assertEqual(yaml_to_json(hash_yaml), hash_json)

    def test_j2y_simple(self):
        self.assertEqual(json_to_yaml(simple_json), simple_yaml)

    def test_j2y_hash(self):
        self.assertEqual(json_to_yaml(hash_json), hash_yaml)
