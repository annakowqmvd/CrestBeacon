# test_crestbeacon.py
"""
Tests for CrestBeacon module.
"""

import unittest
from crestbeacon import CrestBeacon

class TestCrestBeacon(unittest.TestCase):
    """Test cases for CrestBeacon class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrestBeacon()
        self.assertIsInstance(instance, CrestBeacon)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrestBeacon()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
