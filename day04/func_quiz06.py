import random,time,json
import func_basic1 as fb1


word = fb1.load_save_data('word.json','r')
rank = fb1.load_save_data('rank.json','r')

import random,time,json

while True:
    menu = input('''
------------------------------------------------------
1. 문제추가  2. 타자게임  3. 등수리스트  4. 프로그램종료  
------------------------------------------------------
메뉴 번호를 선택해주세요. ''')
    if menu == '1':
        fb1.quiz_input(word)
        fb1.load_save_data('word.json','w',word)
    elif menu == '2':
        fb1.typing_game(word,rank)
    elif menu == '3':
        fb1.rank_list(rank)
    elif menu == '4':
        print('프로그램을 종료합니다.')
        fb1.load_save_data('rank.json','w',rank)
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')