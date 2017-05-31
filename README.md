# Kanji\_to\_Romaji #
Formerly kana\_to\_romaji  
*Tries* to translate Kanji to Romaji with the help of [JMdict](http://www.edrdg.org/jmdict/edict_doc.html)  
Some typograhic characters are also translated since one of the original goals was to make the string printable in ascii  

## Installation ##
`git clone https://github.com/rcamba/kanji_to_romaji`  
Run `install.bat` or `python setup.py install --record installed_files.txt`  
`installed_files.txt` will keep track of location of copied files for uninstallation if neccessary  
Having [`simplejson`](https://pypi.python.org/pypi/simplejson/) installed will make the initial loading of json mappings be significantly faster


## Usage ##
`ktr.py` is a script included to be used in the command line provided you have your python's script folder in your environment variables  

\> ktr.py 友達に会いました  
tomodachi ni aimashita


Although Windows cmd doesn't seem to natively support unicode characters so you can use unicode escaped strings if you'd like...  
\> ktr.py \u53cb\u9054\u306b\u4f1a\u3044\u307e\u3057\u305f  
tomodachi ni aimashita


The more common usage will probably to be used in another program:  
```
from kanji_to_romaji import kanji_to_romaji  
print kanji_to_romaji(u"友達に会いました")  
```
Argument must be in **u**nicode  


## More examples ##
私は嬉: watashi wa ureshii  
更に向こうへ: sarani mukou e  
友達に会いました: tomodachi ni aimashita  
車には一人分の空きがあった: kuruma ni wa hitoribun no aki ga atta  
bl∞dy☆: bl dy

See `tests\test_kanji.py` for more examples  
**Note**: The particles は (ha/wa) or へ (he/e) won't always be translated properly. 
Same goes for some of the Kanji translations since there are multiple possible readings for some of them depending on the context.