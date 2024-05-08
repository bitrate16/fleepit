from setuptools import setup, find_packages

setup(
    name='fleepit',
    version='1',
    py_modules=['fleepit'],
    description='keyboard layout switcher based on xclip & other things',
    url='https://git.pegasko.art/bitrate16/fleepit',
    author_email='pegasko@pegasko.art',
    license='AGPL 3.0',
    keywords='keyboard layout shortcut layout-switcher',
    entry_points='''
        [console_scripts]
        fleepit=fleepit:main
    ''',
)
