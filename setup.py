"""
    Python canonical setup script.
"""

from os import path
from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='vuong_pupdb',
    packages=find_packages(),
    version='2.0',
    license='MIT',
    description='A simple file-based key-value database written in Python. Edited by Vuongpro',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/tuxmonk/pupdb',
    author='tuxmonk',
    author_email='30048080+tuxmonk@users.noreply.github.com',
    keywords=[
        'file-based', 'key-value-store', 'python', 'database', 'rest-api',
        'process-safe', 'cross-language'
    ],
    install_requires=[
        'filelock',
        'flask',
        'gunicorn'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    include_package_data=True
)