from setuptools import setup, find_packages

setup(
    name='fleep',
    version='1',
    py_modules=['fleep'],
    description='keyboard layout switcher based on xclip & other things',
    url='https://git.pegasko.art/bitrate16/fleep',
    author_email='pegasko@pegasko.art',
    license='AGPL 3.0',
    keywords='keyboard layout shortcut layout-switcher',
    entry_points='''
        [console_scripts]
        fleep=fleep:main
    ''',
)
