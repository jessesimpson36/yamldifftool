import copy
import unittest
from yamldifftool import filter_defaults

class TestYamlDiffTool(unittest.TestCase):

    def setUp(self):
        self.base_yaml = {
            'global': {
                'elasticsearch': {
                    'prefix': 'zeebe-re'
                },
                'identity': {
                    'auth': {
                        'webModeler': {
                            'redirectUrl': 'http://localhost:8084'
                        }
                    }
                },
                'image': {
                    'tag': '8.2.2'
                },
                'ingress': {
                    'annotations': {
                        'nginx.ingress.kubernetes.io/ssl-redirect': 'true'
                    }
                },
                'zeebePort': 265
            },
            'zeebe': {
                'env': [
                    {'name': 'ZEEBE_BROKER_DATA_SNAPSHOTPERIOD', 'value': '5m'},
                    {'name': 'ZEEBE_BROKER_DATA_DISKUSAGECOMMANDWATERMARK', 'value': '0.85'},
                    {'name': 'ZEEBE_BROKER_DATA_DISKUSAGEREPLICATIONWATERMARK', 'value': '0.87'}
                ]
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

if __name__ == '__main__':
    unittest.main()
