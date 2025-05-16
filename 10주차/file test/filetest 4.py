import os
inFp = None
fname = input ("파일명을 입력하세요 :")

if os.path.exists(fname) :
    inFp = open (fname, "r")
    inList = inFp.readlines ()
    for inStr in inList :
        print (inStr,end = "")

        inFp.close()
else : 
    print("%s 파일이 없습니다"% fname)