"Elizabeth Ringhausen"

hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
basepay = 40*r
overtime_rate = 1.5*r
overtime_hours = h-40
if h <= 40:
    pay = r*h
else:
    pay = basepay + overtime_hours * overtime_rate
print (pay)
    
