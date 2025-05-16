inFp=None
inList,inStr = [],""

inFp = open("C:\\Users\\유세진\\OneDrive\\바탕 화면\\컴과\\python\\file test\\data1.txt")

inList = inFp.readlines()
for inStr in inList :
    print (inStr, end = "" )

inFp.close()