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
        while True :
            while True:
                buy = {'name': '', 'price': '', 'stock': ''}
                v = input('과일명   (종료:q or Q) >>>  ')
                if fruit['name'] == v:
                    print('중복된 과일입니다.')
                elif v.lower() == 'q' :
                    print("메뉴로 돌아갑니다.")
                    break
                break    
            buy['name'] = v

            while True :
                n = input('가격 >>>  ')
                if n.isdecimal() :
                    buy['price'] = n
                    break
                       

            while True :
                m = input('재고 >>>  ')
                if m.isdecimal() :
                    buy['stock'] = m
                    break

            fruit.append(buy)
            print(buy)
        
        
        
        
    elif choice == 'S' :
        while True :
            sell = input('판매할 과일명   (종료:q or Q) >>>  ')
            delok = 0
            if sell.lower() == 'q' :
                print("메뉴로 돌아갑니다.")
                break
                

            for i in range(len(fruit)) :
                if fruit[i]['name'] == sell :
                    price = fruit[i]['price']
                    stock = fruit[i]['stock']
                    delok = 1

                    while True :
                        num = input('과일 개수(종료:q) >>> ')
                        if num.lower() == 'q' :
                            print("이전으로 돌아갑니다.")
                            break

                        elif num.isalpha() :
                            print('숫자를 입력해주세요.')

                        elif int(num) > stock :
                            print('재고가 부족합니다.')

                        elif int(num) <= stock :
                            many = int(num)
                            price1 = price * many

                            sold += price1
                            total = {'total' : sold}

                            for i in range(len(fruit)) :
                                if fruit[i]['name'] == sell :
                                    fruit[i]['stock'] -= many
                                    break

                            print(f'{sell} 이 {many} 개 판매되었습니다.')
                            print(f'매출이 {price1} 원 적립되었습니다.')
                            break

            if delok == 0 :
                print('정확한 과일명을 기재해주세요.')


                
                
    elif choice == 'L' :
        print('''    과일명          가격          재고    
-----------------------------------------''')
        for i in fruit :
            print('    ', i['name'], '       ', i['price'], '       ', i['stock'])
        print('-----------------------------------------')
        
        tot = total['total']
        print(f'총 판매금액 : {tot}')
        

        
        
    elif choice == 'D' :
        
        while True :
            x = input('삭제할 과일명(종료:q) >>> ')
            delok = 0
                
            if x.lower() == 'q' :
                print("메뉴로 돌아갑니다.")
                break

            for i in range(len(fruit)) :
                if fruit[i]['name'] == x :
                    print(f'{fruit[i]} 이 삭제되었습니다.')
                    del fruit[i]
                    delok = 1
                    break
            if delok == 0 :
                print('등록되지 않은 과일입니다.')
                
                
                
                
    elif choice == 'U' :
        while True :
            p = input('수정할 과일명(종료:q) >>> ')

            if p.lower() == 'q' :
                print("메뉴로 돌아갑니다.")
                break
            
            for i in fruit :
                if i['name'] == p :
                    print(i)
                    var = input('''수정할 항목을 선택하세요.
1 - 가격  2 - 재고
''')
                    if var == '1' :
                        pre = i['price']
                        i['price'] = int(input('수정된 가격 >>> '))
                        now = i['price']
                        print(f'{pre} -> {now} 로 변동되었습니다.')
                        break
                    elif var == '2' :
                        pre = i['stock']
                        i['stock'] = int(input('수정된 재고량 >>> '))
                        now = i['stock']
                        print(f'{pre} -> {now} 로 변동되었습니다.')
                
        
        
        
    elif choice == 'Q' :
        print('프로그램을 종료합니다.')       
        
        ####
        with open('fruit.json','w')as fruit1:
            json.dump(fruit, fruit1)
        with open('sold.json','w')as fruit2:
            json.dump(sold, fruit2)
        
        break