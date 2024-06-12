#! python3
# downloadXkcd.py - XKCDコミックを1つずつダウンロードする

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    #TODO: ページをダウンロードする

    #TODO: コミック画像のURLを見つける

    #TODO: 画像をダウンロードする

    #TODO: 画像を./xkcdに保存する

    #TODO: PrevボタンのURLを取得する

print('完了')
