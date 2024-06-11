import random

guess = ''
while guess not in ('表', '裏'):
    print('コインの裏表を当ててください。表か裏かを入力してください:')
    guess = input()

toss = random.randint(0, 1)  # 0 は裏、1は表
toss_result = '表' if toss == 1 else '裏'

if toss_result == guess:
    print('当たり！')
else:
    print('はずれ！もう一回当てて！')
    guess = input()
    if toss_result == guess:
        print('当たり!')
    else:
        print('はずれ。このゲームは苦手ですね。')

