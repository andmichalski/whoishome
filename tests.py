import os
import unittest
from unittest import mock
from unittest.mock import MagicMock, mock_open, patch

from whois import WhoIs


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
        with open('test_home_macs.txt', 'w+') as f:
            f.write(home_macs_content)
        active_macs_content = ("192.168.1.1 EC:08:6B:4C:5G:FA\n"
                               "192.168.1.2 B8:17:EC:2F:6E:16\n"
                               "192.168.1.100 235")

        with open('test_active_macs.txt', 'w+') as f:
            f.write(active_macs_content)

        self.home_macs = {
            "EC:08:6B:4C:5G:FA": ["192.168.1.1", "TP_LINK", False],
            "B8:17:EC:2F:6E:16": ["192.168.1.2", "RASPBERRY_PI", False]}

        self.active_macs = {"EC:08:6B:4C:5G:FA":"192.168.1.1",
                               "B8:17:EC:2F:6E:16":"192.168.1.2"}
        self.mock_open_home = mock_open(read_data=home_macs_content)
        self.mock_open_active = mock_open(read_data=active_macs_content)
import ipdb; ipdb.set_trace()

    @classmethod
    def tearDownClass(cls):
        os.remove("test_home_macs.txt")
        os.remove("test_active_macs.txt")

    def test_get_home_macs_should_return_dict(self):
        w = WhoIs('test_home_macs.txt', 'test_active_macs.txt')
        self.assertEqual(w.home_macs, self.home_macs)
        self.assertEqual(w.active_macs, self.active_macs)

    def test_compare_macs_should_return_null_value(self):
        w = WhoIs('test_home_macs.txt', 'test_active_macs.txt')
        new_macs = w.compare_macs()
        self.assertEqual(new_macs, [])

    def test_get_inmates_should_return_value(self):
        w = WhoIs('test_home_macs.txt', 'test_active_macs.txt')
        inmates = w.get_inmates()
        self.assertEqual(inmates, [('TP_LINK', False), ('RASPBERRY_PI', False)])

    def test_create_inmates_status_file_should_return_correct_text(self):
        w = WhoIs('test_home_macs.txt', 'test_active_macs.txt')
        w.compare_macs()
        text = w.create_inmates_status_file()
        expected_text = ("        NAME        |     IS_ACTIVE      \n"
        "-----------------------------------------\n"
        "      TP_LINK       |        True        \n"
        "    RASPBERRY_PI    |        True        \n")
        self.assertEqual(expected_text, text)



if __name__ == "__main__":
    unittest.main()
