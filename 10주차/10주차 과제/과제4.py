inFp, outFp = None, None
inStr = ""

inFname = input("소스 파일명을 입력하세요 : ")
outFname = input("타깃 파일명을 입력하세요 : ")
inFp = open(inFname, "r")
outFp = open(outFname, "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print(f"--- {inFname} 파일이 {outFname} 파일로 복사되었음 ---")