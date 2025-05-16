inFp=None
inStr=""

inFp=open("C:\\Users\\유세진\\OneDrive\\바탕 화면\\컴과\\python\\file test\\data1.txt")

inStr=inFp.readline()
print(inStr,end="")

inStr=inFp.readline()
print(inStr,end="")

inStr=inFp.readline()
print(inStr,end="")

inFp.close()