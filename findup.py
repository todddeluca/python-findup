'''
'''

__version__ = '0.1.0'

import os
import glob as globmodule


def glob(pattern, cwd=None):
    '''
    Start walking up the directory tree from the current working directory
    (including the cwd) and return the first directory found that matches the
    glob pattern, using glob.glob().  If no directory is found, return None.

    :param cwd: Defaults to the current working directory.  Use this to start
    searching from a different directory.
    '''
    path = cwd if cwd is not None else os.getcwd()

    for d in walk_up(path):
        matches = globmodule.glob(os.path.join(d, pattern))
        if matches:
            return matches[0]

    return None


#####################
# AUXILIARY FUNCTIONS

def walk_up(path, realpath=False):
    '''
    First normalize path using os.path.expanduser, then os.path.abspath
    (default) or os.path.realpath (if realpath is True).  Then yield path and
    every directory above path.

    Example:

        list(walk_up('~/tmp/./')) -> 
        ['/Users/td23/tmp', '/Users/td23', '/Users', '/']

    path: Should be a directory.
    '''
    if realpath:
        curdir = os.path.realpath(os.path.expanduser(path))
    else:
        curdir = os.path.abspath(os.path.expanduser(path))

    while 1:
        yield curdir
        curdir, tail = os.path.split(curdir)
        if not tail:
            break


