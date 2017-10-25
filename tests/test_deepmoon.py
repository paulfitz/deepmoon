import deepmoon
from deepmoon.four_test_errors import errors as test_errors
import six
import unittest


class TestDeepMoon(unittest.TestCase):

    def tearDown(self):
        deepmoon.unconfigure()

    def test_error(self):
        # test that we can get strings and the first bunch are distinct
        errors = set()
        for i in range(0, 10):
            err = deepmoon.error()
            self.assertTrue(isinstance(err, six.string_types))
            self.assertNotIn(err, errors)
            errors.add(err)

    def test_full(self):
        # check that we get all errors and they repeat correctly
        deepmoon.configure(flavor='four_test_errors')
        errors = set([deepmoon.error() for _ in range(0, 4)])
        self.assertEqual(len(errors), len(test_errors))
        errors2 = set([deepmoon.error() for _ in range(0, 4)])
        self.assertEqual(len(errors2), len(test_errors))
        self.assertEqual(len(errors2 | errors), len(test_errors))
