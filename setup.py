from setuptools import setup, find_packages

import pathlib
try:
    this_directory = pathlib.Path(__file__).parent
    long_description = (this_directory / "README.md").read_text()
    long_description_content_type = 'text/markdown'
except:
    long_description = None
    long_description_content_type = None

setup(
    name='fleepit',
    version='5',
    py_modules=['fleepit'],
    description='Text seleciton keyboard layout switcher based on xclip / etc for X11 & wayland',
    url='https://git.pegasko.art/bitrate16/fleepit',
    author_email='pegasko@pegasko.art',
    license='Apache 2.0',
    keywords='keyboard layout shortcut layout-switcher',
    entry_points='''
        [console_scripts]
        fleepit=fleepit:main
    ''',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
)
