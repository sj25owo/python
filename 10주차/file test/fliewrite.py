outFp = None
outStr = ""

outFp = open("C:\\.Users\\유세진\\OneDrive\\바탕 화면\\컴과\\python\\10주차\\nomal.txt")

while True :
    outStr = input("내용 입력 : ")
    if outStr != "" :
        outFp.writelines(outStr+"\n")
    else :
        break

outFp.close()
print("---정상적으로 파일에 쏨 ---")