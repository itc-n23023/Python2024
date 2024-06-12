#!/usr/bin/env python3
# mapIt.py - コマンドライン引数またはクリップボードに指定した住所の地図を開く

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # コマンドラインから住所を取得する
    address = ' '.join(sys.argv[1:])
else:
    # クリップボードから住所を取得する
    address = pyperclip.paste()

# Googleマップで住所を開く
webbrowser.open('https://www.google.com/maps/place/' + address)

