import copy
import unittest

import yaml

from yamldifftool import filter_defaults

class TestYamlDiffTool(unittest.TestCase):

    def setUp(self):
        self.base_yaml = {
            'global': {
                'image': {
                    'tag': '8.2.2'
                },
                'ingress': {
                    'annotations': {
                        'nginx.ingress.kubernetes.io/ssl-redirect': 'true'
                    }
                }
            }
        }

    def test_filter_defaults_no_changes(self):
        user_yaml = copy.deepcopy(self.base_yaml)
        root_diff = {}
        filter_defaults(self.base_yaml, user_yaml, root_diff)
        self.assertEqual(root_diff, {})

    def test_filter_defaults_with_changes(self):
        user_yaml = copy.deepcopy(self.base_yaml)
        user_yaml['global']['image']['tag'] = '8.2.3'
        root_diff = {}
        filter_defaults(self.base_yaml, user_yaml, root_diff)
        expected_diff = {
            'global': {
                'image': {
                    'tag': '8.2.3'
                }
            }
        }
        self.assertEqual(expected_diff, root_diff)

    def test_filter_defaults_with_additional_keys(self):
        user_yaml = copy.deepcopy(self.base_yaml)
        user_yaml['global']['newKey'] = 'newValue'
        root_diff = {}
        filter_defaults(self.base_yaml, user_yaml, root_diff)
        expected_diff = {
            'global': {
                'newKey': 'newValue'
            }
        }
        self.assertEqual(root_diff, expected_diff)

    def test_filter_defaults_with_strict_mode(self):
        user_yaml = self.base_yaml.copy()
        user_yaml['global']['newKey'] = 'newValue'
        root_diff = {}
        filter_defaults(self.base_yaml, user_yaml, root_diff, strict=True)
        self.assertEqual(root_diff, {})

    def test_none_handling_in_base(self):
        base_yaml = yaml.safe_load("""
        global:
          identity:
            auth:
              operate:
                existingSecret:
          image:
            tag: 8.2.2
        """)
        user_yaml = yaml.safe_load("""
        global:
          identity:
            auth:
              operate:
                existingSecret:
                  name: nameofsecret
          image:
            tag: 8.3.2
        """)
        root_diff = {}
        filter_defaults(base_yaml, user_yaml, root_diff)
        self.assertEqual(root_diff, {'global': {'identity': {'auth': {'operate': {'existingSecret': {'name': 'nameofsecret'}}}}, 'image': {'tag': '8.3.2'}}})

if __name__ == '__main__':
    unittest.main()
