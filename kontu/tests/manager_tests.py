import unittest

from kontu.manager import load_project


class ManagerTests(unittest.TestCase):

    def test_load_project_file(self):
        project = load_project('kontu/tests/test_project/kontu.json')
        self.assertEqual(project.name, 'Test Project')
        # With missing keys.
        self.assertRaises(ValueError, load_project, 'kontu/tests/test_project/invalid.json')


if __name__ == '__main__':
    unittest.main()
