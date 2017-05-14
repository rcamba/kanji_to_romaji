# Kanji\_to\_Romaji #
Formerly kana\_to\_romaji  
*Tries* to translate Kanji to Romaji with the help of [JMdict](http://www.edrdg.org/jmdict/edict_doc.html)

## Installation ##
`git clone https://github.com/rcamba/kanji_to_romaji`  
Run `install.bat` or `python setup.py install --record installed_files.txt`  
`installed_files.txt` will keep track of location of copied files for uninstallation if neccessary  
Having `simplejson` installed will make the initial loading of json mappings be significantly faster


## Usage ##
`ktr.py` is a script included to be used in the command line provided you have your python's script folder in your environment variables  

\> ktr.py 友達に会いました  
tomodachi ni aimashita


Although Windows cmd doesn't seem to natively support CJK characters so you can use unicode if you'd like...  
\> ktr.py \u53cb\u9054\u306b\u4f1a\u3044\u307e\u3057\u305f  
tomodachi ni aimashita


The more common usage will likely to be used in anoother programs:  
```
from kanji_to_romaji.kanji_to_romaji imnport kanji_to_romaji  
kanji_to_romaji(u"友達に会いました")  
```
Argument must be in **u**nicode  


## More examples ##
私は嬉: watashi wa ureshii  
更に向こうへ: sarani mukou e  
友達に会いました: tomodachi ni aimashita  
車には一人分の空きがあった: kuruma ni wa hitoribun no aki ga atta  

See `tests\test_kanji.py` for more examples  
**Note**: The particles は (ha/wa) or へ (he/e) won't always be translated properly. 
Same goes for some of the Kanji translations since there are multiple possible readings for some of them depending on the context.