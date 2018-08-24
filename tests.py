from unittest.mock import mock_open
import os
import unittest
from whois import WhoIs
from unittest.mock import patch


class WhoIsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("test_home_macs.txt", "w+") as f:
            f.write("192.168.1.1 EC:08:6B:4C:5G:FA TP_LINK \n")
            f.write("192.168.1.2 B8:17:EC:2F:6E:16 RASPBERRY_PI")
        with open("test_active_macs.txt", "w+") as f:
            f.write("192.168.1.1 EC:08:6B:4C:5G:FA\n")
            f.write("192.168.1.2 B8:17:EC:2F:6E:16")

    def setUp(self):
        home_macs_content = ("192.168.1.1 EC:08:6B:4C:5G:FA TP_LINK \n"
                             "192.168.1.2 B8:17:EC:2F:6E:16 RASPBERRY_PI")
        self.home_macs = {
            "EC:08:6B:4C:5G:FA": ["192.168.1.1", "TP_LINK", False],
            "B8:17:EC:2F:6E:16": ["192.168.1.2", "RASPBERRY_PI", False]}

        self.mock_open = mock_open(read_data=home_macs_content)

    @classmethod
    def tearDownClass(cls):
        os.remove("test_home_macs.txt")
        os.remove("test_active_macs.txt")

    def test_get_home_macs_should_return_dict(self):
        with patch('builtins.open', self.mock_open):
            home_macs = WhoIs()._get_home_macs()
            self.assertEqual(home_macs, self.home_macs)
