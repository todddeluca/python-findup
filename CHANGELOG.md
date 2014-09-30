


# 0.2.0

- findup.glob() now conforms to its documentation, by returning the directory
  containing the path that the glob pattern matches instead of the path itself.
- Argh!  How embarrassing!  This package could not be installed with pip,
  because it was missing the MANIFEST.in file that included the README.md file
  that setup.py uses.  This is now fixed, so `pip install findup` works.
