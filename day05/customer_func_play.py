import customer_func as cf1

custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong123@gmail.com', 'birthyear': '2000'},
          {'name': '박철수', 'gender': 'M', 'email': 'park01@gmail.com', 'birthyear': '2002'},
          {'name': '김나리', 'gender': 'F', 'email': 'kim123@gmail.com', 'birthyear': '1999'} ]
page = 2 

while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요 :
I - 입력   C - 현재   P - 이전   N - 다음   U - 수정   D - 삭제   Q - 종료
    ''').upper()  

    if choice=="I":  
        page = cf1.customer_input(custlist)
    elif choice=="C":
        cf1.customer_c(custlist, page)
    elif choice == 'P':
        page = cf1.customer_p(custlist, page)
    elif choice == 'N':
        page = cf1.customer_n(custlist, page)
    elif choice=='D':
        cf1.customer_delete(custlist)
    elif choice=="U":
        cf1.customer_update(custlist)
    elif choice=="Q":
        print('프로그램을 종료합니다.')
        break