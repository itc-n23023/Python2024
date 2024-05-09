import random, sys
print('ROCK, PAPER, SCISSORS')

# 次の変数に、勝ち、負け、引き分けの数を記録する
wins = 0
losses = 0
ties = 0

while True: # メインのゲームループ
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    
    while True: # プレイヤーの入力ループ
        print("Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit")
        player_move = input().lower() # 小文字で処理
        if player_move == 'q':
            sys.exit()  # プログラムを終了
        if player_move in ('r', 'p', 's'):
            break
        print("Invalid input. Type one of r, p, s, or q.")

    # プレイヤーの入力した手を表示する
    if player_move == 'r':
        print("ROCK versus...")
    elif player_move == 'p':
        print("PAPER versus...")
    elif player_move == 's':
        print("SCISSORS versus...")

    # コンピューターの手を表示する
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print("ROCK")
    elif random_number == 2:
        computer_move = 'p'
        print("PAPER")
    elif random_number == 3:
        computer_move = 's'
        print("SCISSORS")

    # 勝ち/負け/引き分けを表示し、記録する
    if player_move == computer_move:
        print("It is a tie!")
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or \
         (player_move == 'p' and computer_move == 'r') or \
         (player_move == 's' and computer_move == 'p'):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1

