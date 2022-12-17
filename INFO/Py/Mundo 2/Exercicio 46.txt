from time import sleep

for a in range (10,-1,-1):
    sleep(1)
    print(a)
    if a == 0:
        print("Fogos de artificio!")
        