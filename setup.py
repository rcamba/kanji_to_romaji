import os
import setuptools

PATH_TO_MODULE = os.path.dirname(__file__)

setuptools.setup(
    name='Kanji_to_Romaji',
    version='1.0',
    packages=['kanji_to_romaji', 'models', 'jp_mappings'],
    package_data={"jp_mappings": ["./*.json"]},
    url='https://github.com/rcamba/kanji_to_romaji',
    license='',
    author='Robert Camba',
    author_email='rcamba@users.noreply.github.com',
    description='Try to translate Kanji to Romaji.',
    extras_require={
        'fasterjson': ["simplejson>=3.10.0"],
    },
    scripts=['scripts/ktr.py']
)
