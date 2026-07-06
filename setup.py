# -*- coding: utf-8 -*-
"""Setup module."""
from setuptools import setup

def read_description() -> str:
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return '''TODO'''


setup(
    name='pixora',
    packages=['pixora'],
    version='0.1',
    description='TODO',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    author='Sepand Haghighi',
    author_email='me@sepand.tech',
    url='https://github.com/sepandhaghighi/pixora',
    download_url='https://github.com/sepandhaghighi/pixora/tarball/v0.1',
    keywords='TODO',
    project_urls={
        'Source': 'https://github.com/sepandhaghighi/pixora'
    },
    install_requires=[],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Terminals',
    ],
    license='MIT',
    entry_points={
            'console_scripts': [
                'pixora = pixora.cli:main',
            ]
    }
)
