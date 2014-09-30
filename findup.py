'''
'''

__version__ = '0.2.0'

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
    if cwd and not os.path.isdir(cwd):
        raise Exception('cwd must be a directory path', cwd)

    if cwd is None:
        cwd = os.getcwd()

    for d in walk_up(cwd):
        matches = globmodule.glob(os.path.join(d, pattern))
        if matches:
            return d

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
    '''
    if realpath:
        curr_path = os.path.realpath(os.path.expanduser(path))
    else:
        curr_path = os.path.abspath(os.path.expanduser(path))

    while 1:
        yield curr_path
        curr_path, tail = os.path.split(curr_path)
        if not tail:
            break


