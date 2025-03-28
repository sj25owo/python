i,k,gugu = 0,0,""

for i in range (2,10):
    gugu=gugu+("# %d단 #" %1)

print(gugu)

for i in range(1,10):
    gugu = ""
    for k in range(2,10):
        gugu = gugu + str("%2d x %2d=%2d " % (k,i,k*i)) 
    print(gugu)