from setuptools import setup, find_packages
import re

PYPI_RST_FILTERS = (
    # Replace code-blocks
    (r'\.\.\s? code-block::\s*(\w|\+)+', '::'),
    # Remove all badges
    (r'\.\. image:: .*', ''),
    (r'    :target: .*', ''),
    (r'    :alt: .*', ''),
)


def rst(filename):
    '''
    Load rst file and sanitize it for PyPI.
    Remove unsupported github tags:
     - code-block directive
     - all badges
    '''
    content = open(filename).read()
    for regex, replacement in PYPI_RST_FILTERS:
        content = re.sub(regex, replacement, content)
    return content


long_description = '\n'.join((
    rst('README.md'),
    rst('CHANGELOG.md'),
    ''
))

setup(
    name='flask-rollbar',
    version='0.0.1',
    description='A simple implemntation of rollbar for flask',
    long_description=open('README.md').read(),
    url='https://github.com/psykzz/flask_rollbar',
    author='Matt Smith',
    author_email='matt.daemon660@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['flask', 'rollbar', 'blinker'],
    tests_require=['nose'],
    extras_require={
        'test': ['nosetests'],
    },
    license='MIT',
    use_2to3=True,
    zip_safe=False,
    keywords='rollbar',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: pypy',
    ],
)
