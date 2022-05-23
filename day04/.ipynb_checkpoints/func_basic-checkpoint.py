# quiz 03> 커피메뉴 관리 프로그램
# 데이터 저장은 딕셔너리로 {'메뉴명':가격, 'coffee':2000}
# 프로그램에서 사용할 메뉴
#  1. 메뉴입력  2. 메뉴수정  3. 메뉴목록  4. 메뉴삭제  5. 프로그램종료
#   - 메뉴입력 : 메뉴명과 가격을 입력받아서 저장
#   - 메뉴수정 : 메뉴명을 확인하고 있는 메뉴에 가격을 입력받아 수정
#   - 메뉴목록 : 저장된 메뉴명과 가격을 출력(천단위 구분기호표기), 메뉴명 순서대로 출력
#   - 메뉴삭제 : 메뉴명을 확인하고 있는 메뉴에서 삭제
#   - 프로그램종료 : 프로그램을 종료하는 메시지를 출력하고 종료
#   - 메뉴 1~5까지만 입력받고 다른 값이 들어오면 관련 에러 메시지를 출력한다.
#   - 가격은 숫자로 입력해야됨
# menu = {'아이스아메리카노':3000,'라떼':4000,'코코아':3500}
def menu_input(menu):
    print('현재메뉴 :',list(menu.keys()))
    name = input('추가할 메뉴명을 입력하세요.')
    price = 'a'
    while not price.isdecimal():
        price = input('추가할 메뉴의 가격을 입력하세요.')
    menu[name]=int(price)

def menu_update(menu):
    print('현재메뉴 :',list(menu.keys()))
    name = ''
    while not name in menu.keys():
        if not name == menu.keys():
            name = input('수정할 메뉴명을 입력하세요.')
    price = 'a'
    while not price.isdecimal() :
        price = input("수정할 메뉴의 가격을 입력하세요.")        
    menu[name]=int(price)

def menu_list(menu):
    print('------ menu ------')
    for item in sorted(menu.items(),key=lambda data:data[1],reverse=True):
        print(f'{item[0]}:{item[1]:10,}')
def menu_delete(menu):
    print('현재메뉴 :',list(menu.keys()))
    name = ''
    while not name in menu.keys():
        name = input('삭제할 메뉴명을 입력하세요.')
    del menu[name]