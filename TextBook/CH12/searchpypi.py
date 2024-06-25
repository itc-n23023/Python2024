#! python3
# searchpypi.py - pypiの検索結果をいくつか開く
import requests, sys, webbrowser, bs4

print('Searching...') #検索結果をダウンロード中のテキストを表示
res = requests.get('https://pypi.org/search/?q= ' + '.join(sys.argv[1:]))
res.raise_for_status()

#TODO: 上位の検索結果のリンクを取得する

#TODO:　各結果をブラウザのタブで開く
