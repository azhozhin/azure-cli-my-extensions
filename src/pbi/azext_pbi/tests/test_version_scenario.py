import unittest

from azext_pbi.custom import pbi_version
from azext_pbi.version import VERSION


class VersionTest(unittest.TestCase):

    def test_version(self):
        actual = pbi_version()
        assert actual['version'] == VERSION
