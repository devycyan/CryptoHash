# test_cryptohash.py
"""
Tests for CryptoHash module.
"""

import unittest
from cryptohash import CryptoHash

class TestCryptoHash(unittest.TestCase):
    """Test cases for CryptoHash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoHash()
        self.assertIsInstance(instance, CryptoHash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoHash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
