inFp = None
inList = ""

inFp = open("C:\\Users\\유세진\\OneDrive\\바탕 화면\\컴과\\python\\10주차\\10주차 과제\\data1.txt", "r", encoding="UTF8")

inList = inFp.readlines()
#print(inList)
for i, inStr in enumerate(inList) :
    print(i+1,'\b:', inStr, end = "")

inFp.close()