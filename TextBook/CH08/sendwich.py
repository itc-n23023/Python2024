
8章 入力検証
赤嶺正実
•
5月23日 （最終編集: 6月4日）
100 点
期限: 5月31日
下記の内容を行い、課題を提出しよう

[教科書] 8.2 プロジェクト：バカを何時間も忙しくさせておく方法(P.236-P.237)
GitHub提出 [仮想環境]-[PG2]-[TextBook]-[CH08]-[idiot.py]
[教科書] 8.3 プロジェクト：掛け算クイズ(P.238-P.240)
GitHub提出 [仮想環境]-[PG2]-[TextBook]-[CH08]-[multiplicationQuiz.py]
[教科書] 8.6.1 サンドイッチメーカー

(P.241-P.242) 
GitHub提出  [仮想環境]-[PG2]-[TextBook]-[CH08]-[sandwich.py]
[教科書] 8.6.2 自作の掛け算クイズ

(P.241-P.242) 
GitHub提出  [仮想環境]-[PG2]-[TextBook]-[CH08]-[mulquiz.py]

1. 仮想環境内で作成
2. 仮想環境からGitHubへプッシュ
3. GitHubのファイルのURLを提出

08章_入力検証
Google スライド

idiot.py
テキスト

mulquiz.py
テキスト

multiplicationQuiz.py
テキスト

sandwich.py
テキスト
あなたの課題
未提出
限定公開のコメント
クラスのコメント 1 件

赤嶺正実6月4日
8.2 プロジェクト：バカを何時間も忙しくさせておく方法(P.236-P.237) [idiot.py]
n23007 大山 朝夢

8.3 プロジェクト：掛け算クイズ(P.238-P.240) [multiplicationQuiz.py]
n23026 東崎原 結太

8.6.1 サンドイッチメーカー(P.241-P.242) [sandwich.py]
n23019 玉城 颯太

8.6.2 自作の掛け算クイズ(P.241-P.242) [mulquiz.py]
n23009 神谷 優太

クラスのコメントを追加…

# 演習プロジェクト 8.6.1

import pyinputplus as pyip

PRICES = {
    '小麦パン': 100,
    '白パン': 110,
    'サワー種': 120,
    'チキン': 200,
    'ターキー': 250,
    'ハム': 300,
    '豆腐': 280,
    'チェダー': 100,
    'スイス': 150,
    'モツァレラ': 180,
    'mayo': 10,
    'mustard': 10,
    'lettuce': 50,
    'tomato': 30,
}

def sandwich_maker():
    bread = pyip.inputMenu(('小麦パン', '白パン', 'サワー種'),
                           prompt='パンを選んでください\n',
                           numbered=True)
    protain = pyip.inputMenu(('チキン', 'ターキー', 'ハム', '豆腐'),
                             prompt='タンパク質を選んでください\n',
                             numbered=True)
    cheese = None
    if pyip.inputYesNo('チーズは必要ですか？') == 'yes':
        cheese = pyip.inputMenu(('チェダー', 'スイス', 'モツァレラ'),
                                prompt='チーズを選んで下さい\n',
                                numbered=True)
    mayo = pyip.inputYesNo('マヨネーズは必要ですか？') == 'yes'
    mustard = pyip.inputYesNo('カラシは必要ですか？') == 'yes'
    lettuce = pyip.inputYesNo('レタスは必要ですか？') == 'yes'
    tomato = pyip.inputYesNo('トマトは必要ですか？') == 'yes'
    numbers = pyip.inputInt('いくつ要りますか？', min=1)

    print('-' * 10)
    price = PRICES[bread]
    print(f'パン: {bread} {PRICES[bread]}円')
    price += PRICES[protain]
    print(f'タンパク質: {protain} {PRICES[protain]}円')
    if cheese:
        price += PRICES[cheese]
        print(f'チーズ: {cheese} {PRICES[cheese]}円')
    if mayo:
        price += PRICES['mayo']
        print(f'マヨネーズ: {PRICES["mayo"]}円')
    if mustard:
        price += PRICES['mustard']
        print(f'カラシ: {PRICES["mustard"]}円')
    if lettuce:
        price += PRICES['lettuce']
        print(f'レタス: {PRICES["lettuce"]}円')
    if tomato:
        price += PRICES['tomato']
        print(f'トマト: {PRICES["tomato"]}円')

    print(f'小計: {price}円')
    print(f'個数: {numbers}個')
    print(f'合計: {price * numbers}円')

sandwich_maker()
