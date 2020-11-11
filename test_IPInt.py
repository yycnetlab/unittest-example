#!/usr/bin/env python3

import unittest
import IPInt


class TestIPInt(unittest.TestCase):
    def test_edges(self):
        """Test at the very limit of acceptable values."""

        # Test lower limit:
        self.assertEqual(IPInt.IP_to_Int("0.0.0.0"), 0)
        self.assertEqual(IPInt.Int_to_IP(0), "0.0.0.0")

        # Test upper limit:
        self.assertEqual(IPInt.IP_to_Int("255.255.255.255"), (2**32)-1)
        self.assertEqual(IPInt.Int_to_IP((2**32)-1), "255.255.255.255")

    def test_beyond_edge(self):
        """Test passing in values beyond the acceptable range."""

        # Test below the lower limit:
        self.assertRaises(ValueError, IPInt.IP_to_Int, "0.0.0.-1")
        self.assertRaises(ValueError, IPInt.Int_to_IP, -1)

        # Test above the upper limit:
        self.assertRaises(ValueError, IPInt.IP_to_Int, "255.255.255.256")
        self.assertRaises(ValueError, IPInt.Int_to_IP, 2**32)

    def test_types(self):
        """Test passing in bad types."""

        # Pass in a float when a string is expected:
        self.assertRaises(TypeError, IPInt.IP_to_Int, 1.0)

        # Pass in a float when an integer is expected:
        self.assertRaises(TypeError, IPInt.Int_to_IP, 1.0)

        # Pass in a bool:
        self.assertRaises(TypeError, IPInt.IP_to_Int, True)
        self.assertRaises(TypeError, IPInt.Int_to_IP, True)

        # Pass in a complex number:
        self.assertRaises(TypeError, IPInt.IP_to_Int, 1j)
        self.assertRaises(TypeError, IPInt.Int_to_IP, 1j)

    def test_bad_data(self):
        """Test passing in ludicrous data."""

        # pass in a malformed IP strings:
        self.assertRaises(ValueError, IPInt.IP_to_Int, "1...4")
        self.assertRaises(ValueError, IPInt.IP_to_Int, ".1.2.3.4")
        self.assertRaises(ValueError, IPInt.IP_to_Int, "1.2.3.4.")
        self.assertRaises(ValueError, IPInt.IP_to_Int, ".2.3.4")
        self.assertRaises(ValueError, IPInt.IP_to_Int, "1.2.3.")
        self.assertRaises(ValueError, IPInt.IP_to_Int, "1,2,3,4")
        self.assertRaises(ValueError, IPInt.IP_to_Int, "0x01abcdef")
