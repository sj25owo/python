inFp = None
inStr = ""
i = 0
j = '\b:'

inFp = open("C:\\Users\\유세진\\OneDrive\\바탕 화면\\컴과\\python\\10주차\\10주차 과제\\data1.txt", "r", encoding="utf8")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    i += 1
    print(("%d %s" % (i, j)), inStr, end= "")

inFp.close()