
# python-findup

## Introduction

Find the first file matching a given pattern in the current directory or the
nearest ancestor directory.  This project is (roughly) a python version of
[node-findup-sync](https://github.com/cowboy/node-findup-sync).


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


