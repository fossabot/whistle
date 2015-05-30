from setuptools import setup, find_packages

tolines = lambda c: filter(None, map(lambda s: s.strip(), c.split('\n')))

def read(filename, flt=None):
    with open(filename) as f:
        content = f.read().strip()
        return flt(content) if callable(flt) else content

def requirements_filter(c):
    install_requires = []
    for requirement in tolines(c):
        _pos = requirement.find('#egg=')
        if _pos != -1:
            requirement = requirement[_pos+5:].strip()
        _pos = requirement.find('#')
        if _pos != -1:
            requirement = requirement[0:_pos].strip()
        if len(requirement):
            install_requires.append(requirement)
    return install_requires

version = read('version.txt')

setup(
name = 'edgy.event',
description = 'Event dispatcher',
license = 'Apache License, Version 2.0',
namespace_packages = [u'edgy'],
    version = version,
    long_description = read('README.rst'),
    classifiers = read('classifiers.txt', tolines),
    packages = find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data = True,
    install_requires = read('requirements.txt', requirements_filter),
)
