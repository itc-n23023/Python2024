def is_valid_chess_board(board):
    # 各駒の数をカウントするための辞書を初期化
    piece_count = {'bking': 0, 'bqueen': 0, 'bbishop': 0, 'wking': 0, 'wqueen': 0, 'wbishop': 0}
    # チェス盤の位置を示す文字列のリスト
    positions = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h',
                 '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h',
                 '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h',
                 '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h',
                 '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h',
                 '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',
                 '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h',
                 '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h']
    
    # チェス盤の辞書をループし、各駒の数をカウントする
    for piece in board.values():
        if piece in piece_count:
            piece_count[piece] += 1
        else:
            # 有効な駒でない場合はFalseを返す
            return False
    
    # 各駒の数が制限を超えないかチェックする
    for count in piece_count.values():
        if count > 1:
            # 同じ種類の駒が2つ以上ある場合はFalseを返す
            return False
    
    # チェス盤の位置が有効かどうかをチェックする
    for position in board.keys():
        if position not in positions:
            # 有効な位置でない場合はFalseを返す
            return False
    
    # すべての条件をクリアした場合はTrueを返す
    return True

# テスト用の辞書
board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

# 関数を呼び出して結果を出力
print(is_valid_chess_board(board))  # True を返す

