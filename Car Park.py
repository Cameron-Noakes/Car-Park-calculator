#Car Park Tickets
#Ask driver how many hours they need
#If under 2 hours it's £3.50
#If 2 hours over but less than 4 hours it's £5.60
#4 hours and over you get 10% off and is £7.20

answer1 = int(input("How many hours do you need for parking?: "))
if answer1 < 2:
    print ("Price is £3.50")

elif answer1 >= 2 and answer1 < 4:
    print ("Price is £5.60")

elif answer1 >= 4:
    discount = 7.20*0.10
    print (discount)
    
    
