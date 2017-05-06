from distutils.core import setup
import os

PATH_TO_MODULE = os.path.dirname(__file__)

setup(
    name='Kana_to_Romaji',
    version='1.0',
    packages=['kana_to_romaji', 'models', 'jp_mappings'],
    package_data={"jp_mappings": ["./*.json"]},
    url='https://github.com/rcamba/kana_to_romaji',
    license='',
    author='Robert Camba',
    author_email='rcamba@users.noreply.github.com',
    description='Translate Kana to Romaji with some weak support for some Kanji.',
    extras_require={
        'fasterjson': ["simplejson>=3.10.0"],
    }
)
