inFp=None
inStr=""

inFp=open("C:\\Users\\유세진\\OneDrive\\바탕 화면\\컴과\\python\\file test\\data1.txt")

while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    print(inStr,end="")

inFp.close()