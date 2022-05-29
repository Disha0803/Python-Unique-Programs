import pyautogui as pg
num=int(input("Enter a number to divide by 100: "))
if num==0:
    pg.alert("Can't divide by zero")
else:
    print(100/num)