


import findup


def test_findup():

    assert findup.glob('findup.py')
    assert findup.glob('*/setup.py')
    assert findup.glob('README*')


