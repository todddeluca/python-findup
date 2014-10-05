'''
'''

__version__ = '0.3.0'

import os
import glob as globmodule


def glob(pattern, dirname=None):
    '''
    Find the first path matching a given pattern within dirname or the nearest
    ancestor of dirname.  Walk up the directory tree, starting from
    `dirname` and return the first path found that matches the glob
    pattern, using glob.glob().  If no path is found, return None.

    :param pattern: a glob pattern that will be appended to (a normalized)
    dirname.  
    :param dirname: String.  A directory path.  Defaults to the current working
    directory.  This path will be "normalized" using os.path.expanduser and
    os.path.abspath.

    For example, findup.glob('.git') would find the path to the nearest '.git' 
    directory in the current working dir or above it.

    To find the root dir from anywhere within a git repository, do:

        os.path.dirname(findup.glob('.git'))

    Or more robustly:

        path = findup.glob('.git')
        git_root = None if path is None or os.path.dirname(path)

    Raises a ValueError if dirname is not the name of a directory.
    '''
    if dirname is None:
        normdn = normalize_path(os.getcwd())
    else:
        normdn = normalize_path(dirname)

    if not os.path.isdir(normdn):
        raise ValueError('Parameter dirname must be a directory path.', dirname)

    for d in walk_up(normdn):
        matches = globmodule.glob(os.path.join(d, pattern))
        if matches:
            return matches[0]

    return None


#####################
# AUXILIARY FUNCTIONS


def normalize_path(path, realpath=False):
    '''
    Convert path that possibly contains a user tilde and/or is a relative
    path into an absolute path.
    '''
    if realpath:
        return os.path.realpath(os.path.expanduser(path))
    else:
        return os.path.abspath(os.path.expanduser(path))


def walk_up(path):
    '''
    Yield path and every directory above path.
    Consider normalizing path, using `normalize_path(path)` first.

    Example:

        list(walk_up('/Users/td23/tmp')) -> 
        ['/Users/td23/tmp', '/Users/td23', '/Users', '/']
    '''
    curr_path = path
    while 1:
        yield curr_path
        curr_path, tail = os.path.split(curr_path)
        if not tail:
            break


