import random


def hangman_easy(word):
    wrong = 0
    stage_easy = ["__________          ",
                  "|        |          ",
                  "|        O          ",
                  "|       /|\         ",
                  "|       / \         ",
                  "|                   ",
                  "|                   ",
                  "|                   ",
                  "|                   ",
                  "|___________________"
                  ]
    
    rletters = list(word)     #変数rlettersにwordを１文字ずつ分割したものを入れる
    board = ["_"] * len(word)  #wordの文字数分_で埋める
    win = False
    
    while wrong < len(stage_easy)-1:
        
        char = input(f'{len(word)}文字の単語を予想してね:')
        
        for char in list(char):
            if char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        
        if "_" not in board:
            print('You Win!')
            win = True
            break
        
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stage_easy[:e]))
        
    if not win:
        print('\n'.join(stage_easy[:wrong + 1]))
        print('Game Over')
        print(f'Answer:{word}')
                  

def hangman_normal(word):
    wrong = 0
    stage_normal = ["__________          ",
                    "|        |          ",
                    "|        O          ",
                    "|       /|\         ",
                    "|       / \         ",
                    "|                   ",
                    "|                   ",
                    "|___________________"
                   ]

    rletters = list(word)     #変数rletersにwordを１文字ずつ分割したものを入れる
    board = ["_"] * len(word)  #wordの文字数分_で埋める
    win = False
    
    while wrong < len(stage_normal)-1:
        print('\n')
        char = input(f'{len(word)}文字の単語を予想してね:')
        for char in list(char):
            if char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
                
        if "_" not in board:
            print('You Win!')
            win = True
            break
        
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stage_normal[:e]))
        
    if not win:
        print('\n'.join(stage_normal[:wrong + 1]))
        print('Game Over')
        print(f'Answer:{word}')
        
def hangman_hard(word):
    wrong = 0
    stage_hard = ["__________          ",
                  "|        |          ",
                  "|        O          ",
                  "|       /|\         ",
                  "|       / \         ",
                  "|___________________"
                  ]
    
    rletters = list(word)     #変数rletersにwordを１文字ずつ分割したものを入れる
    board = ["_"] * len(word)  #wordの文字数分_で埋める
    win = False
    
    while wrong < len(stage_hard)-1: 
        char = input(f'{len(word)}文字の単語を予想してね:')
        
        for char in list(char):
            if char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
                
        if "_" not in board:
            print('You Win!')
            win = True
            break
        
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stage_hard[:e]))
        
    if not win:
        print('\n'.join(stage_hard[:wrong + 1]))
        print('Game Over')
        print(f'Answer:{word}')


dict = {1:'google',2:'amazon',3:'facebook',4:'apple',5:'microsoft'}




print('ハングマンを始めます')
while True:
    try:
        num = int(input('難易度を選択してね（1: easy, 2: normal, 3: hard) -> '))

        num_dict = random.randint(1,6)
        word = dict[num_dict]
        
        if num == 1:
            hangman_easy(word)

        elif num == 2:
            hangman_normal(word)

        elif num == 3:
            hangman_hard(word)

        else:
            print('1から3の数字を入力してください')

    except  ValueError:
        print('数字を入力してください')
        break

