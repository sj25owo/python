from tkinter import *

def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')
    inImage = []

    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            byte = fp.read(1)
            if byte:  # 오류발생으로 추가
                data = int(ord(byte))
            else:  
                data = 0
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def displayImage(image):
    global XSIZE, YSIZE, paper
    for i in range(0, XSIZE):
        rgbString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            rgbString += "#%02x%02x%02x " % (data, data, data)
        paper.put("{" + rgbString + "}", (0, i))

window = Tk()
window.title("흑백 사진 보기")

XSIZE, YSIZE = 256, 256
inImage = []

canvas = Canvas(window, height=YSIZE, width=XSIZE)
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image=paper, state="normal")

filename = 'C:\\Users\\유세진\\OneDrive\\바탕 화면\\컴과\\python\\10주차\\Lenna.raw'
loadImage(filename)
displayImage(inImage)

canvas.pack()
window.mainloop()
