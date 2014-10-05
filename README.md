
# python-findup


## Introduction

Find the first path matching a given pattern in the current working
directory (or a given directory) or the nearest ancestor directory.  This
project is (roughly) a python version of
[node-findup-sync](https://github.com/cowboy/node-findup-sync).

Why?  Applications, such as git, often use project configuration files found in
the current directory or an ancestor directory.  The `findup` modules allows an
application author to easily find these files or directories.


## Installation

The best way to install is probably to use pip:

    pip install findup

Or you can clone and install findup from github:

    git clone https://github.com/todddeluca/python-findup.git
    cd python-findup
    python setup.py install

## Usage

`pattern` is combined with the current working directory or an ancestor
directory and passed to `glob.glob` to see if the pattern matches.  If it does,
the first match is returned.  Pattern can contain some shell wildcard
characters, like `?` and `*`.  See the python `glob` module for more details.

    findup.glob(pattern)

To find the root dir of a git repository, when the current working directory is
somewhere within the repository:

    os.path.dirname(findup.glob('.git'))

Or more robustly, handling the case where the cwd is not within a git
repository:

    path = findup.glob('.git')
    git_root = None if path is None or os.path.dirname(path)

