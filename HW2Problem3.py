"Elizabeth Ringhausen"

for n in range (50,56):
    for a in range(0,round (n/6)):
        for b in range(0,round (n/9)):
            for c in range(0,round (n/20)):
                if (6*a+9*b+20*c==n):
                    print("%d nuggets can be bought with a=%d, b=%d, c=%d"%(n,a,b,c))
    
