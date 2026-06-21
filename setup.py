from setuptools import setup, find_packages

setup(
    name='flask-rollbar',
    version='0.1.0',
    description='Rollbar integration for Flask',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/psykzz/flask-rollbar',
    author='Matt Smith',
    author_email='matt.daemon660@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['flask>=3.0', 'rollbar', 'blinker'],
    license='MIT',
    zip_safe=False,
    keywords='rollbar flask',
    python_requires='>=3.9',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: Flask',
    ],
)