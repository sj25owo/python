class Car :
    color = ""
    speed = 0

    def __init__(self) :
        self.color = "빨강"
        self,speed = 0

    def __init__(self, value1, value2) :
        self.color = value1
        self.speed = value2



    def upSpeed(self, value) :
        self.speed += value
    def downSpeed(self, value) :
        self.speed -= value
    def printMessage() :
        print("시험 출력이다.")

myCar1 = Car("빨강" ,30)

myCar2 = Car("파랑" , 60)



myCar1.upSpeed(30)
print("자동차 1의 색상은 %s 이며, 현재 속도는 %dkm 입니다." %(myCar1.color, myCar1.speed))
myCar2.upSpeed(60)
print("자동차 2의 색상은 %s 이며, 현재 속도는 %dkm 입니다." %(myCar2.color, myCar2.speed))



