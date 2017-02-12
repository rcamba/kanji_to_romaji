from distutils.core import setup
import os

PATH_TO_MODULE = os.path.dirname(__file__)

setup(
    name='Kana_to_Romaji',
    version='1.0',
    packages=['kana_to_romaji'],
    url='https://github.com/rcamba/kana_to_romaji',
    license='',
    author='Robert Camba',
    author_email='rcamba@users.noreply.github.com',
    description='Translate Kana to Romaji with some weak support for some Kanji.',
    data_files=[("jp_mappings", [os.path.join("jp_mappings", f)
                                 for f in os.listdir(os.path.join(PATH_TO_MODULE, "jp_mappings"))])]
)
