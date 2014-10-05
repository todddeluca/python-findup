

import os
import uuid

import findup

tests_dir = os.path.dirname(os.path.abspath(__file__))
proj_dir = os.path.dirname(tests_dir)

def test_findup():

    assert findup.glob('findup.py')
    assert findup.glob('*/setup.py')
    assert findup.glob('README*')

def test_glob_cwd():
    '''
    Test findup.glob using the current working directory
    '''
    os.chdir(tests_dir)
    assert findup.glob('test_findup.py') == os.path.abspath(os.path.join(tests_dir, 'test_findup.py'))
    assert findup.glob('README*') == os.path.abspath(os.path.join(proj_dir, 'README.md'))
    assert findup.glob(uuid.uuid4().hex) == None

def test_glob_dirname():
    '''
    Test findup.glob using dirname parameter
    '''
    os.chdir(proj_dir)
    assert findup.glob('test_findup.py', tests_dir) == os.path.abspath(os.path.join(tests_dir, 'test_findup.py'))
    assert findup.glob('README*', tests_dir) == os.path.abspath(os.path.join(proj_dir, 'README.md'))
    assert findup.glob(uuid.uuid4().hex, tests_dir) == None

