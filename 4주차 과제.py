do =int(input(" 1. 입력한 수식 계산 2. 두 수 사이의 합계 : "))

if do== 1:
    a = input("수식 입력 : ")
    result_1 = eval(a)
    print(result_1)
elif do == 2:
    b = int(input("첫번째 값을 입력하시오"))
    c = int(input("두번째 값을 입력하시오"))
    result = (abs(b-c)+1)*(b+c)/2
    print("{0}+...+{1}는 {2}입니다".format(b, c, result))
else:
     print ("다시실행하시오.")
    