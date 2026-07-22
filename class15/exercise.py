import time
timetamp = time.strftime('%H:%M:%S')
print(timetamp)
hours = int(time.strftime('%H'))

if(hours >= 0 and hours < 12):
    print("Good morning sir")
elif(hours >= 12 and hours < 18):
    print("Good afternoon sir")
elif(hours >= 18 and hours < 20):
    print("Good evening sir")
else:
    print("Good night sir")

