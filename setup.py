from distutils.core import setup
from os import path
from io import open

path_to_this_file = path.abspath(path.dirname(__file__))
try:
    with open(path.join(path_to_this_file, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except IOError:
    long_description = ""

setup(
    name='Kanji_to_Romaji',
    version='1.0.0',
    packages=['kanji_to_romaji', 'kanji_to_romaji/models'],
    package_data={'kanji_to_romaji': ['jp_mappings/*.json']},
    url='https://github.com/rcamba/kanji_to_romaji',
    license='Mozilla Public License Version 2.0',
    author='Robert Camba',
    author_email='rcamba@users.noreply.github.com',
    description='Try to translate Kanji to Romaji.',
    extras_require={
        'fasterjson': ['simplejson>=3.10.0'],
    },
    scripts=['scripts/ktr.py'],
    long_description=long_description
)
