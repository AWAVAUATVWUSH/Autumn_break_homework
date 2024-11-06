import math

def get_num_in_range():
    while(True):
        try:
            num:int = int(input("Adj meg egy számot 200 és 920 között: "))
            if(num>=200 and num<=920):
                return num
            else:
                print("Hibás szám")
        except ValueError:
            print("Hibás szám")

def print_excitement_level():
    while(True):
        try:
            num:int = int(input("Hány órád lesz? "))
            if(num>=0):
                if(num==0):
                    print("Be se jövök!")
                elif(num<=1):
                    print("Még 90% on vagyunk!")
                elif(num<=3):
                    print("Még bírjuk (60%)")
                elif(num<=7):
                    print("Progit tanulunk, töltődünk! 70%")
                elif(num<=9):
                    print("Lassan nem bírjuk tovább! 50%")
                else:
                    print("Ez már tényleg túlzás")
                break
            else:
                print("Hibás szám")
        except ValueError:
            print("Hibás szám")

def get_student_condition(day:str = "", lesson:str = ""):
    lesson = lesson.lower()
    day = day.lower()
    if(day == "hétfő"):
        print("Márti alszik")
    elif(day == "kedd"):
        if(lesson == "hittan"):
            print("Márti figyel")
        else:
            print("Márti alszik")
    elif(day == "szerda"):
        if(lesson == "programozás"):
            print("Márti dolgozik")
        else:
            print("Márti állapotáról nincs info")
    elif(day == "csütörtök"):
        print("Márti figyel")
    elif(day == "péntek"):
        print("Márti félig van jelen")
    else:
        print("Ilyen napon nincs iskola")

def get_sqrt():
    while(True):
        try:
            num:float = float(input("\nAdj meg egy valós számot: "))
            if(num>=0):
                return math.sqrt(num)
            else:
                print("Hibás szám")
        except ValueError:
            print("Hibás szám")

def get_rectangle_data():
    while(True):
        try:
            num1:float = float(input("Add meg egy téglalap egyik oldalát: "))
            if(num1>0):
                break
            else:
                print("Hibás szám")
        except ValueError:
            print("Hibás szám")
    while(True):
        try:
            num2:float = float(input("Add meg egy téglalap másik oldalát: "))
            if(num2>0):
                break
            else:
                print("Hibás szám")
        except ValueError:
            print("Hibás szám")
    print(f"A téglalap területe: {num1*num2:.2f}, A téglalap kerülete: {num1*2+num2*2:.2f}:")
