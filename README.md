# pysha2

## License


This software is distributed under the 
[MIT License](https://choosealicense.com/licenses/mit/).

## About

pysha2 is a pure Python implementation of the FIPS 180-2 secure hash standard.
I originally wrote and published this on the web prior to the inclusion of 
`hashlib` into the Python standard library. Unfortunately, the original source 
was lost due to a hard drive failure. However, the library proved useful to 
some at the time (mainly due to the prevalence of Python 2.3 and 2.4), and so I 
was able to recover all but the unit tests (which I later rewrote).

Since then, Python 2 was deprecated and reached its end-of-life. Contributors
have since found this implementation useful as an educational tool, and have
given it a new life by updating it to Python 3.

## Usage

The library supports both the "old" Python 2 hash interface of the `md5` and
`sha` modules, as well as the "new" hash interface introduced by `hashlib`. 
This was intended to permit you to use `pysha2` as a drop-in replacement for 
either interface and make updating to SHA2 easier in legacy applications.

A quick example of hashing a string:

```python
import sha2

print sha2.sha256("Can you keep a secret?").hexdigest()
```

## Testing

To run the included unit tests:

```bash
python test_pysha2.py
```

in the current directory, or use `pytest`.
