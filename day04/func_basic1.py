def load_save_data(file,mode,data=None):
    path = os.path.dirname(__file__)+'/'+file
    # print(os.path.dirname(__file__))
    with open(file,mode)as f:
        if mode == 'r':
            data = json.load(f)
            return data
        elif mode == 'w':
            json.dump(data,f)


def quiz_input(word):
        while True:
            quiz = input('추가할 단어를 입력(종료:0) >>>')
            while quiz in word:
                quiz = input('중복된 단어입니다. 다시 입력해주세요.(종료:0) >>>')
            if quiz == '0':
                break
            word.append(quiz)
            print(word)

def typing_game(word, rank):
        input('엔터누르면 시작')
        start = time.time()

        for i in range(1,6):
            print('%s번 문제!'%(i))
            while True:
                ran = word[random.randint(0,len(word)-1)]
                answer = input('%s'%(ran))
                if not answer == ran:
                    print('틀렸습니다. 새로운 문제를 출제합니다.')
                else:
                    print('정답!')
                    break
        print('문제를 모두 풀었습니다 ㅎㅎ')
        end=time.time()
        print(f'{end-start:.0f}초')
        name = input('사용자명을 입력하세요.')
        while name in rank:
            name = input('사용자명이 중복되었습니다. 다른 이름을 입력하세요.')
        rank[name] = end-start
        print(rank)
def rank_list(rank):
        ranklist = sorted(rank.items(),key=lambda x:x[1])
        for index,item in enumerate(ranklist):
            print(f'{index+1}등 {item[0]}{item[1]:.2f}')
