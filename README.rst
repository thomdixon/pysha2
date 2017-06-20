.. image:: https://travis-ci.org/thomdixon/pysha2.svg?branch=master
    :target: https://travis-ci.org/thomdixon/pysha2

======
pysha2
======

License
=======

This software is distributed under the 
`MIT License <https://choosealicense.com/licenses/mit/>`_.

About
=====

pysha2 is a pure Python implementation of the FIPS 180-2 secure hash
standard. I originally wrote and published this on the web prior to
the inclusion of ``hashlib`` into the Python standard
library. Unfortunately, the original source was lost due to a hard
drive failure. Fortunately, the library proved useful to some at the
time (due to the prevalence of Python 2.3 and 2.4), and so I was able
to recover all but the unit tests (which I later rewrote).

Usage
=====

The library supports both the "old" hash interface of ``md5`` and
``sha``, as well as the "new" hash interface introduced by
``hashlib``. This permits you to use pysha2 as a drop-in replacement
for either interface.

A quick example of hashing a string::

    import sha2

    print sha2.sha256('Can you keep a secret?').hexdigest()

Testing
=======

To run the included unit tests, execute::

    python test.py

in the current directory or run with ``nosetests``.
