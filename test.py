#! /usr/bin/env python

import unittest
from sha2 import *

class TestSHA224(unittest.TestCase):
    def setUp(self):
        self.f = sha224

    def test_empty(self):
        self.assertEqual(self.f('').hexdigest(),
                         'd14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f')

    def test_less_than_block_length(self):
        self.assertEqual(self.f('abc').hexdigest(),
                         '23097d223405d8228642a477bda255b32aadbce4bda0b3f7e36c9da7')

    def test_block_length(self):
        self.assertEqual(self.f('a'*64).hexdigest(),
                         'a88cd5cde6d6fe9136a4e58b49167461ea95d388ca2bdb7afdc3cbf4')

    def test_several_blocks(self):
        self.assertEqual(self.f('a'*1000000).hexdigest(),
                         '20794655980c91d8bbb4c1ea97618a4bf03f42581948b2ee4ee7ad67')

class TestSHA256(unittest.TestCase):
    def setUp(self):
        self.f = sha256

    def test_empty(self):
        self.assertEqual(self.f('').hexdigest(),
                         'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')

    def test_less_than_block_length(self):
        self.assertEqual(self.f('abc').hexdigest(),
                         'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')

    def test_block_length(self):
        self.assertEqual(self.f('a'*64).hexdigest(),
                         'ffe054fe7ae0cb6dc65c3af9b61d5209f439851db43d0ba5997337df154668eb')

    def test_several_blocks(self):
        self.assertEqual(self.f('a'*1000000).hexdigest(),
                         'cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0')

class TestSHA384(unittest.TestCase):
    def setUp(self):
        self.f = sha384

    def test_empty(self):
        self.assertEqual(self.f('').hexdigest(),
                         '38b060a751ac96384cd9327eb1b1e36a21fdb71114be0743'+
                         '4c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b')

    def test_less_than_block_length(self):
        self.assertEqual(self.f('abc').hexdigest(),
                         'cb00753f45a35e8bb5a03d699ac65007272c32ab0eded163'+
                         '1a8b605a43ff5bed8086072ba1e7cc2358baeca134c825a7')

    def test_block_length(self):
        self.assertEqual(self.f('a'*128).hexdigest(),
                         'edb12730a366098b3b2beac75a3bef1b0969b15c48e2163c'+
                         '23d96994f8d1bef760c7e27f3c464d3829f56c0d53808b0b')

    def test_several_blocks(self):
        self.assertEqual(self.f('a'*1000000).hexdigest(),
                         '9d0e1809716474cb086e834e310a4a1ced149e9c00f24852'+
                         '7972cec5704c2a5b07b8b3dc38ecc4ebae97ddd87f3d8985')

class TestSHA512(unittest.TestCase):
    def setUp(self):
        self.f = sha512

    def test_empty(self):
        self.assertEqual(self.f('').hexdigest(),
                         'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce'+
                         '47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e')

    def test_less_than_block_length(self):
        self.assertEqual(self.f('abc').hexdigest(),
                         'ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a'+
                         '2192992a274fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f')

    def test_block_length(self):
        self.assertEqual(self.f('a'*128).hexdigest(),
                         'b73d1929aa615934e61a871596b3f3b33359f42b8175602e89f7e06e5f658a24'+
                         '3667807ed300314b95cacdd579f3e33abdfbe351909519a846d465c59582f321')

    def test_several_blocks(self):
        self.assertEqual(self.f('a'*1000000).hexdigest(),
                         'e718483d0ce769644e2e42c7bc15b4638e1f98b13b2044285632a803afa973eb'+
                         'de0ff244877ea60a4cb0432ce577c31beb009c5c2c49aa2e4eadb217ad8cc09b')

if __name__ == '__main__':
    sha224_suite = unittest.TestLoader().loadTestsFromTestCase(TestSHA224)
    sha256_suite = unittest.TestLoader().loadTestsFromTestCase(TestSHA256)
    sha384_suite = unittest.TestLoader().loadTestsFromTestCase(TestSHA384)
    sha512_suite = unittest.TestLoader().loadTestsFromTestCase(TestSHA512)

    all_tests = unittest.TestSuite([sha224_suite,
                                    sha256_suite, 
                                    sha384_suite,
                                    sha512_suite])

    unittest.TextTestRunner(verbosity=2).run(all_tests)
