# 로또는 총 6자리
# 1. 사용자는 횟수를 입력해야함 = 자동 선택시 몇 번 구매횟수
# 2. 컴퓨터가 먼저 로또번호를 만들어야함.
# 3. 주어진 게임 수 만큼 로또 번호 생성해야함 (랜덤으로)
# 4. 당첨 번호를 바탕으로 자동으로 입력한 번호랑 비교해야함. 어떤 번호가, 몇개 맞았는지
# 등수가 나와야함. // 결과는 정렬되어서 보여져야함.
# 5. 결과 정산 포맷
# 1등 : n번
# 2등 : n번
# 3등 : n번
# 4등 : n번

# 6. 수동 입력시 '중복없이' 6개를 입력 받을 수 있어야함.
# 7. 예외처리 해줘야함. (중복 숫자나, 문자가 들어왔을 시.)
'''
함수 하나당 되도록 30줄을 넘지 않도록
필요한 함수들

메뉴함수 (1.자동 2.수동 3.종료)

-자동 로또
    1. 정답 랜덤 숫자 생성 함수
    2. 사용자용 랜덤 숫자 생성 함수
    3. 결과화면 함수

-수동 로또
    1. 정답 랜덤 숫자 생성 함수
    2. 사용자용 숫자 입력 함수
    3. 결과화면 함수

중복 되는 부분
- 랜덤 숫자 생성 함수
- 결과 함수(내가 구매한 로또와 당첨로또 번호를 비교하여 몇개의 번호가 맞았고 어떤 번호가 맞았고 몇등인지 까지)
'''

import random

def menu():     #메뉴 함수

    while True:
        print("원하는 기능을 선택하세요.")
        print("=============================")
        print("1.자동 2.수동 3.종료")
        print("=============================")
        num = int(input())

        if num == 1:
            print("자동 로또를 선택하셨습니다. 자동 로또 기능을 실행합니다.")
            autoLotto()
        elif num == 2:
            print("수동 로또를 선택하셨습니다. 수동 로또 기능을 실행합니다.")
            manualLotto()
        elif num == 3:
            print("프로그램을 종료합니다.")
            break
        else:
            print("숫자를 다시 입력해주세요")

############################################################################

# 보너스 번호 생성 함수
def bonusNum():
    return random.randint(1,45)

############################################################################

def randomNum():   # 랜덤 숫자 생성 함수(정답 생성기), 보너스 번호 추가해야함.
    answer = sorted(random.sample(range(1,46),6))
    while True:
        bonus = bonusNum()
        if bonus not in answer:
            break
    return answer, bonus
############################################################################

def autoLotto():    # 자동 로또 함수
    print("자동 로또 프로그램 실행 중")
    # 컴퓨터 랜덤번호 생성
    autoAnswers = randomNum()

    lottoArray = autoUser()

    for autoAnswer in autoAnswers:
        # result는 등수를 리턴
        # TODO
        autoAns = result(autoAnswer, lottoArray)
    print(autoAns)

    # 결과정산
    # TODO

'''
"몇개의 자동 로또를 생성하시겠습니까?" 
몇개의 로또 프로그램을 돌릴지 정수를 입력한다.
입력한 숫자의 횟수대로 자동 숫자 생성기가 돌아간다. 단, list에 중복되는 숫자는 없어야한다.
"귀하께서 구매하신 로또의 번호는 다음과 같습니다."
'''

############################################################################

def autoUser():     #유저용 랜덤숫자 생성기

    yourlotto = []

    print("몇개의 자동 로또를 생성하시겠습니까?")

    howmany = int(input())  #몇개의 로또를 구매할지 정수 입력

    print(f"{howmany}개의 자동 로또를 구매하셨습니다.")

    n = random.randint(1, 45)

    for i in range(howmany):
        yourlotto.append(randomNum())

    print(f"{howmany}개의 자동 로또가 생성되었습니다. 구매하신 로또의 번호는 {yourlotto} 입니다.")

    return yourlotto


    # for i in range(howmany):    # 구매한 로또 갯수대로 배열 갯수 생성
    #     lottoList.append([])
    # userlotto = []
    # print("귀하께서 구매하신 로또 번호는 다음과 같습니다.")

    # n = random.randint(1,45)

    # while True:
    #     if len(userlotto) == 6:
    #         break
    #     if n not in userlotto:
    #         userlotto.append(n)
    #
    # print(f"귀하게서 구매하신 로또 번호는 다음과 같습니다. {userlotto}")
    #
    # return userlotto

############################################################################################

# 정답과 유저로또를 비교하여 당낙 비교하는 함수
def result(a, b):   # a = 로또 정답 b = 유저 로또(자동 or 수동)

    # comment: bonus 번호는 어디감?
    # comment: 2등처리 로직 어디?

    answer = b[0]
    bonus = b[1]
    cnt = 0
    # 맞은 개수 체크
    # cnt++?
    for num in b[0]:
            if num in a[0]:
                cnt += 1

    if cnt == 5 and bonus in a:
        print("2등")
    elif cnt == 6:
        print("1등")
    elif cnt >= 3 and cnt <= 5: # cnt 5,4,3 = (3,4,5등)
        print(f"{8-cnt}등")
    else:
        print("낙첨")

    # for i in answer:        
    #     corNum = 0          # 맞은 숫자가 있으면 늘어날 예정
    #     corArray = []       # 맞은 숫자를 저장할 리스트
    #     for j in i:         
    #         if j in a:
    #             corNum += 1
    #             corArray.append(j)
        # '''
        # b = [([1,2,3],4), ([5,6,7],8)]
        # b[0][0] = [1,2,3]
        # b[0][1] = 4
        # b[1][0] = [5,6,7]
        # b[1][1] = 8
        # '''

# result()를 토대로 각각 몇등을 몇번했는지 결과화면으로 나타내는 함수

# def resultScreen() :

#     if corNum == 6 :
#         print(f"맞춘 번호는 {corArray}, 맞춘 갯수는 {corNum}개 입니다. 1등 당첨입니다.")

#     elif corNum == 5 :
#         print(f"맞춘 번호는 {corArray}, 맞춘 갯수는 {corNum}개 입니다. 2등입니다.")

#     elif corNum == 5 :
#         print(f"맞춘 번호는 {corArray}, 맞춘 갯수는 {corNum}개 입니다. 3등입니다.")

#     elif corNum == 4 :
#         print(f"맞춘 번호는 {corArray}, 맞춘 갯수는 {corNum}개 입니다. 4등입니다.")

#     elif corNum == 3 :
#         print(f"맞춘 번호는 {corArray}, 맞춘 갯수는 {corNum}개 입니다. 5등입니다.")

#     else :
#         print(f"맞춘 번호는 {corArray}, 맞춘 갯수는 {corNum}개 입니다. 낙첨입니다.")

############################################################################

def manualLotto():  # 수동 로또 함수
    print("몇개의 수동 로또를 구매하시겠습니까?")

    mymanual = int(input())     #num_of_rows

    # print("6개의 숫자를 중복없이 입력해주세요.")

    manualList = []         #num_per_row

    for i in range(mymanual) :
        numbers = []
        for j in range(6) :
            num = int(input("로또 숫자를 중복없이 찍어주세요 : "))
            if num in numbers :
                print("중복된 숫자입니다. 다시 입력하세요.") 
            else :
                numbers.append(num)
        manualList.append(numbers)
        manualList.append(int(input("보너스 번호를 입력하세요 : ")))

    answer = randomNum()

    # while True :
    #     for i in range(mymanual):
    #         numbers = []
    #         for j in range(6):
    #             num = int(input("로또 숫자를 중복없이 찍어주세요: "))
    #             if num in numbers :
    #                 print("중복 숫자입니다. 다시 입력하세요")
    #             else :
    #                 numbers.append(num)
    #                 cnt+=1
    #     if cnt == 6:
    #         manualList.append(numbers)
                

    result(answer, manualList)

'''
몇개의 수동 로또를 구매하시겠습니까?
6개의 숫자를 중복 없이 입력해주세요.
...
exception 숫자를 다시 입력해주세요.
'''

if __name__ == "__main__":
    while True:
        if menu() != 3:
            break