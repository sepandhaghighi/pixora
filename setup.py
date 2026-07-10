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
        return '''Pixora is a lightweight Python library and command-line tool for converting ordinary images into retro-style pixel art.
        Built on top of Pillow, it provides a simple API for pixelizing images with customizable pixel sizes while supporting both file paths
        and in-memory objects. Whether you are creating game assets, generating pixelated avatars, or adding a nostalgic visual effect to your images,
        Pixora offers a fast, and easy-to-use solution for both scripts and terminal workflows.'''


setup(
    name='pixora',
    packages=['pixora'],
    version='0.1',
    description='Pixora: A Python Library for Pixel Art Conversion',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    author='Sepand Haghighi',
    author_email='me@sepand.tech',
    url='https://github.com/sepandhaghighi/pixora',
    download_url='https://github.com/sepandhaghighi/pixora/tarball/v0.1',
    keywords='pixel art pixel-art pixelate image-processing pillow PIL graphics',
    project_urls={
        'Source': 'https://github.com/sepandhaghighi/pixora'
    },
    install_requires=[],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
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
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
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
