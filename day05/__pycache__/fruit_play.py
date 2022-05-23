import function_fruit as ff

fruit=[{'name':'사과', 'price': 3000, 'stock':10},
         {'name':'딸기', 'price': 5000, 'stock':10},
         {'name':'두리안', 'price': 20000, 'stock':10},        
         {'name':'아보카도', 'price': 12000, 'stock':10},
         {'name':'스타후르츠', 'price': 30000, 'stock':10},
         {'name':'체리자두', 'price': 15000, 'stock':10},
         {'name':'애플수박', 'price': 30000, 'stock':10},
         {'name':'샤인머스켓', 'price': 20000, 'stock':10}]

       

sold = 0


import json

with open('fruit.json','r',encoding='utf-8') as fruit1:
    fruit = json.load(fruit1)
with open('sold.json','r',encoding='utf-8') as fruit2:
    sold = json.load(fruit2)

total = {'total' : sold}


while True:
    choice = input('''
재고 및 매출 관리 프로그램입니다. 할 일을 선택해주세요.  (종료:q or Q)
A - 과일 추가   S - 판매    L - 재고 및 매출 현황    D - 삭제    U - 재고 수정   Q - 종료 \n>>> ''').upper()

    if choice == 'A' :
        ff.fruit_add(fruit)


    elif choice == 'S' :
        sold,total=ff.fruit_sell(fruit,sold,total)
        

    elif choice == 'L' :
        sold,total=ff.fruit_list(fruit,sold,total)
        

    elif choice == 'D' :
        ff.fruit_delete(fruit)

    elif choice == 'U' :
        ff.fruit_update(fruit)

    elif choice == 'Q' :
        print('프로그램을 종료합니다.')       
        
        with open('fruit.json','w')as fruit1:
            json.dump(fruit, fruit1)
        with open('sold.json','w')as fruit2:
            json.dump(sold, fruit2)
        
        break