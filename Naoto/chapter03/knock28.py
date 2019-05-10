'''
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
'''
import re

from knock25 import template_extract
from knock26 import Highlight_markup_removal
from knock27 import Highlight_markup_removal