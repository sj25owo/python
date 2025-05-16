inFp,outFp = None,None
inStr = ""

inFp = open("C:\indows\win.ini","r")
outFp = open("C:\temp\data3.txt","w")
inList =inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.cloes()
outFp.close()
print("---파일이 정상적으로 복사되었음---")