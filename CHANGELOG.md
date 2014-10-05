

# 0.3.0

- findup.glob() now returns the path of the first pattern matched by
  glob.glob() in the current working directory (or a given dir) or the
  nearest ancestor dir.  Version 0.2.0 returned the directory containing
  the path.  In keeping with `node-findup-sync` this returns the matching
  path itself.
- change parameter name from `cwd` to `dirname` in findup.glob()
- remove unused parameter in `walkup` function.
- Change exception raised when `dirname` is not a directory to the more
  specific `ValueError`.

# 0.2.0

- findup.glob() now conforms to its documentation, by returning the directory
  containing the path that the glob pattern matches instead of the path itself.
- Argh!  How embarrassing!  This package could not be installed with pip,
  because it was missing the MANIFEST.in file that included the README.md file
  that setup.py uses.  This is now fixed, so `pip install findup` works.
