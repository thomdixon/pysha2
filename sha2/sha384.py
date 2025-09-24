#!/usr/bin/env python
__author__ = "Thomas Dixon"
__license__ = "MIT"

from sha2.sha512 import sha512


def new(m: bytes | None = None) -> "sha384":
    return sha384(m)


class sha384(sha512):
    _h = (
        0xCBBB9D5DC1059ED8,
        0x629A292A367CD507,
        0x9159015A3070DD17,
        0x152FECD8F70E5939,
        0x67332667FFC00B31,
        0x8EB44A8768581511,
        0xDB0C2E0D64F98FA7,
        0x47B5481DBEFA4FA4,
    )
    _output_size = 6
    digest_size = 48
