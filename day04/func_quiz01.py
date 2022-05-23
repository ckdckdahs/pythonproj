# quiz 01>
# 주민등록번호 14자리를 입력받아서 성별을 체크합니다.
# 프로그램 종료는 (q,Q)를 누를 때까지 반복처리합니다.
# 입력예 : 123456-1234567
# 조건처리 : -길이값 체크
#            -성별 체크 (기능값 : 1,2,3,4)
# 출력 : 여성입니다. or 남성입니다.

def jumin_check():
    while True:
        num = input('\n\n주민등록번호를 입력하세요.   입력 예) OOOOOO-OOOOOOO\n')
        if len(num) == 1 and num.lower() == 'q':
            print('프로그램 종료')
            break
        elif len(num) == 14 and num[6] == '-' and num[7] in ['1','2','3','4']:
            if num[7] in ['1','3']:
                print('       남성입니다.')
            else:
                print('       여성입니다.')
        else:
            print('       주민등록번호를 정확히 입력해주세요.')

jumin_check()

## 입력 : 주민등록번호 
## 리턴값 : 성별

def jumin_check1(num):
    gender = ''
    if len(num) == 14 and num[6] == '-' and num[7] in ['1','2','3','4']:
            if num[7] in ['1','3']:
                gender = '남성'
            else:
                gender = '여성'
    else:
        print('       주민등록번호를 정확히 입력해주세요.')
    return gender


while True:
        j = input('\n\n주민등록번호를 입력하세요.   입력 예) OOOOOO-OOOOOOO\n')
        if len(j) == 1 and j.lower() == 'q':
            print('프로그램 종료')
            break
            gender = jumin_check1(j)
            print(gender)