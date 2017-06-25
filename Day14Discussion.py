"Elizabeth Ringhausen"

num=0
total=0
with open(sample_text.txt) as a:
    for line in a:
        if not line.startswith("X-DSPAM-Confidence:") :continue
        total=tot+num
        num+=1
avspam=total/num
print(avspam)
        
