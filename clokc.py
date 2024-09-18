import time
SecNum=int(input("60, 30, 15"))
if SecNum==60:
    my_time = int(60)
    for x in range(my_time, 0, -1):
        time.sleep(1)
        print(x)
elif SecNum==30:
    my_time = int(30)
    for x in range(my_time, 0, -1):
        time.sleep(1)
        print(x)
elif SecNum==15:
    my_time = int(15)
    for x in range(my_time, 0, -1):
        time.sleep(1)
        print(x)