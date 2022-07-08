##명령어 함수 정의

#학생 정보를 저장하는 함수
def Menu1(students, info) :
    name, mid, final = info
    students['name'].append(name)
    students['mid'].append(int(mid))
    students['final'].append(int(final))

#학점을 부여하는 함수
def Menu2(students) :
    for i in range(len(students['name'])):
        try:
            tmp = students['grade'][i]
        except:
            avg = (students['mid'][i] + students['final'][i]) / 2
            if avg >= 90:
                grade = 'A'
            elif avg >= 80:
                grade = 'B'
            elif avg >= 70:
                grade = 'C'
            else:
                grade = 'D'
            students['grade'].append(grade)
            
#학생들 정보를 출력하는 함수
def Menu3(students) :
    print('-'*30)
    print('name\tmid\tfinal\tgrade')
    print('-'*30)
    for i in range(len(students['name'])):
        print(f"{students['name'][i]}\t{students['mid'][i]}\t{students['final'][i]}\t{students['grade'][i]}")

#학생 정보를 삭제하는 함수
def Menu4(students, name):
    for i in range(len(students['name'])):
        if name == students['name'][i]:
            del students['name'][i]
            del students['mid'][i]
            del students['final'][i]
            if len(students['grade']) > i:
                del students['grade'][i]
            break
    
## 메인 영역

#학생 정보를 저장할 변수 초기화
students = {'name':[], 'mid':[], 'final':[], 'grade':[]}

# 명령어 설명
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

# 프로그램 실행
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")

    if choice == "1":
        #학생 정보 입력받기
        info = input("Enter name mid-score final-score : ").split()
        #예외사항 처리(데이터 입력 개수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        if len(info) != 3:
            print("Num of data is not 3!")
            continue
        if info[0] in students['name']:
            print("Already exist name!")
            continue
        try:
            tmp1 = int(info[1])
            tmp2 = int(info[2])
            if tmp1 <= 0 or tmp2 <= 0:
                raise Exception
        except:
            print("Score is not positive integer!")
            continue
        #예외사항이 아닌 입력인 경우 1번 함수 호출 
        Menu1(students, info)
    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if len(students['name']) == 0:
            print("No student data!")
            continue
        #예외사항이 아닌 경우 2번 함수 호출
        Menu2(students)
        print("Grading to all students.")

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        if len(students['name']) == 0:
            print("No student data!")
            continue
        if len(students['name']) != len(students['grade']):
            print("There is a student who didn't get grade.")
            continue
        #예외사항이 아닌 경우 3번 함수 호출
        Menu3(students)

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if len(students['name']) == 0:
            print("No student data!")
            continue
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        name = input("Enter the name to delete : ")
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        if name not in students['name']:
            print("Not exist name!")
            continue
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        Menu4(students, name)
        print(f"{name} student information is deleted.")

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        print("Exit Program!")
        #반복문 종료
        break
    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")