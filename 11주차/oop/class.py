class Car :
    color = ""
    speed = 0
    count = 0

    def __init__(self) :
        self.speed = 0
        Car.count += 1

myCar1, myCar2 = None, None

mycar1 = ()
myCar1.speed = 30
print ("자동차 1의 현재 속도는 %dkm, 생산된 자동차ㅡㄴ 총 %d대 입니다" %(myCar1.speed, myCar1.count))

mycar2 = ()
myCar2.speed = 60
print ("자동차 2의 현재 속도는 %dkm, 생산된 자동차ㅡㄴ 총 %d대 입니다" %(myCar2.speed, myCar2.count))