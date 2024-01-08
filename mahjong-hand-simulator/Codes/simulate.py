import numpy as np
import random
import sys
import copy

# ndarrayから特定の値の要素をなくす関数
def remove_val(arr, val):
    index = np.where(arr == val)[0][0]
    arr = np.delete(arr, index)
    return arr

# 数字から牌の記号を出力する関数
def print_hand(arr):
    Circle = 0
    Banboo = 0
    Character = 0
    num = 0
    Suit = 'm'
    for i in range(arr.size):
        if arr[i] > 11 and num <= 2:
            print("p", end="")
            Suit = 's'
        elif arr[i] > 18 and num <= 18:
            print("s", end="")
            Suit = 'z'
        elif arr[i] > 25 and num <= 25:
            print("z", end="")
            Suit = 'm'
            
        if Suit == 'p':
            print(arr[i], end="")
            Circle += 1
        elif Suit == 's':
            print(arr[i] - 9, end="")
            Banboo += 1
        elif Suit == 'z':
            print(arr[i] - 18, end="")
            Character += 1
        elif Suit == 'm':
            if arr[i] == 26:
                print(1, end="")
            elif arr[i] == 27:
                print(9, end="")
            Character += 1
        num = arr[i]
    print(Suit + "\n", end="")
    print("筒子 :" + str(Circle) + "枚 索子: " + str(Banboo) + "枚 一九字牌: " + str(Character) + "枚")

    
    
    Suit = 'p'
    for i in range(arr.size):
        if arr[i] > 9 and num <= 9:
            print("p", end="")
            Suit = 's'
        elif arr[i] > 18 and num <= 18:
            print("s", end="")
            Suit = 'z'
        elif arr[i] > 25 and num <= 25:
            print("z", end="")
            Suit = 'm'
            
        if Suit == 'p':
            print(arr[i], end="")
            Circle += 1
        elif Suit == 's':
            print(arr[i] - 9, end="")
            Banboo += 1
        elif Suit == 'z':
            print(arr[i] - 18, end="")
            Character += 1
        elif Suit == 'm':
            if arr[i] == 26:
                print(1, end="")
            elif arr[i] == 27:
                print(9, end="")
            Character += 1
        num = arr[i]
    print(Suit + "\n", end="")
    print("筒子 :" + str(Circle) + "枚 索子: " + str(Banboo) + "枚 一九字牌: " + str(Character) + "枚")

# player2, 3にランダムに配布する処理
def bring_players(tiles):
    Player2 = np.random.choice(tiles, 13, replace=False)    #この書き方で値の重複も出来てるぽいしいけそう
    Player2 = np.sort(Player2)
    #print("Player2", Player2)

    for i in range(13):
        tiles = remove_val(tiles, Player2[i])
        
    #print("After tiles:", tiles)


    Player3 = np.random.choice(tiles, 13, replace=False)
    Player3 = np.sort(Player3)
    #print("Player3", Player3)

    for i in range(13):
        tiles = remove_val(tiles, Player3[i])
    
    return Player2, Player3

# 数値が牌の種類を表し、番号が管理用に1~108でつけられている
# 1~9:1~9p 10~18:1~9s 19~25:1~7z(東南西北白發中) 26:1m 27:9m
# -> 1,2:1m,9m 3~11:1~9p 12~20:1~9s 21~27:1~9z 

# 各種4枚ずつ 108枚
tiles = np.tile(np.arange(1, 28).reshape(-1, 1), 4).flatten()

#print("tiles:", tiles)

hand = input("手牌を入力してください\n")
print("\n")
#hand = "123456789p12345z"  # ex) 9m133459p25679s12z

# 手牌の数値化

handnum = []
lenhand = len(hand)
Suit = 'z'
for i, v in enumerate(hand):  #いずれ例外処理も書かないといけないかも
    if hand[lenhand - 1 - i] == 'z':
        Suit = 'z'
        continue
    elif hand[lenhand - 1 - i] == 's':
        Suit = 's'
        continue
    elif hand[lenhand - 1 - i] == 'p':
        Suit = 'p'
        continue
    elif hand[lenhand - 1 - i] == 'm':
        Suit = 'm'
        continue

    if Suit == 'z':
        handnum.append(int(hand[lenhand - 1 - i]) + 20)
    elif Suit == 's':
        handnum.append(int(hand[lenhand - 1 - i]) + 11)
    elif Suit == 'p':
        handnum.append(int(hand[lenhand - 1 - i]) + 2)
    elif Suit == 'm':
        if hand[lenhand - 1 - i] == '1':
            handnum.append(1)
        elif hand[lenhand - 1 - i] == '9':
            handnum.append(9)


'''
for i in range(28): #28文字なはず  #いずれ例外処理も書かないといけないかも
    if hand[2 * i - 1] == 'p':
        handnum.append([int(hand[2 * i - 2])])
    elif hand[2 * i - 1] == 's':
        handnum.append([int(hand[2 * i - 2]) + 9])
    elif hand[2 * i - 1] == 'z':
        handnum.append([int(hand[2 * i - 2]) + 18])
    elif hand[2 * i - 1] == 'm':
        if hand[2 * i - 2] == '1':
            handnum.append([int(hand[2 * i - 2]) + 25])
        elif hand[2 * i - 2] == '9':
            handnum.append([int(hand[2 * i - 2]) + 18])
'''


#print("手牌")
#print(handnum)

# 入力された手牌の数字化までおけ
# 次は牌山からのピック
if len(handnum) > 14:
    print("多牌しています！")
    sys.exit()
elif len(handnum) < 14:
    print("少牌しています！")
    sys.exit()

for i in range(14):
    if handnum[i] in tiles:
        tiles = remove_val(tiles, handnum[i])
    else:
        print("イカサマしないでください！")
        sys.exit()
#print("After tiles:", tiles)

# ピックもおけ

sim_num = int(input("何回試行しますか？\n"))

    
#print("After tiles:", tiles)

# 配るのもおけ
# あとは記号での出力の仕方

# ミスった気がする　一旦　ぴんそーじまんの順で出すことにする

if sim_num == 1:
    Player2, Player3 = bring_players(tiles)

    print("Player2")
    print_hand(Player2)
    print("\n")

    print("Player3")
    print_hand(Player3)

elif sim_num > 1:
    Circle2 = 0
    Bamboo2 = 0
    Character2 = 0
    tiles_orig = copy.deepcopy(tiles)
    for i in range(sim_num):
        Player2, Player3 = bring_players(tiles_orig)
        Circle2 += sum(x <= 9 for x in Player2)
        Bamboo2 += sum((x > 9 and x <= 18) for x in Player2)
        Character2 += sum(x > 18 for x in Player2)
        
        Circle2 += sum(x <= 9 for x in Player3)
        Bamboo2 += sum((x > 9 and x <= 18) for x in Player3)
        Character2 += sum(x > 18 for x in Player3)
          
    print("他家の" + str(sim_num) + "回平均(枚)")
    print("筒子", Circle2 / (2*sim_num))
    print("索子", Bamboo2 / (2*sim_num))
    print("やおちゅうはい", Character2 / (2*sim_num))
    
# 思い付きのコーナー
#   親か子かは選べてもよい n = 13or14, 2*nとかで対処可能だと思う
#   四麻への拡張はできなくはなさそう 牌種多くて面倒くさそうではあるけど

# エラー処理
#   13枚or14枚でなかった場合の処理
#   ない記号とかを書かれたときの処理