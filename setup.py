from distutils.core import setup

setup(
    name='Kanji_to_Romaji',
    version='1.0.0',
    packages=['kanji_to_romaji', 'kanji_to_romaji/models'],
    package_data={"kanji_to_romaji": ["jp_mappings/*.json"]},
    url='https://github.com/rcamba/kanji_to_romaji',
    license='Mozilla Public License Version 2.0',
    author='Robert Camba',
    author_email='rcamba@users.noreply.github.com',
    description='Try to translate Kanji to Romaji.',
    extras_require={
        'fasterjson': ["simplejson>=3.10.0"],
    },
    scripts=['scripts/ktr.py']
)
