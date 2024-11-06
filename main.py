from functions import get_num_in_range, print_excitement_level, get_student_condition, get_sqrt, get_rectangle_data

numAsText:str = f"{get_num_in_range()}"
print(f"A megadott szám első számjegye: {numAsText[0]}\n")

print_excitement_level()

day:str = input("\nAdj meg egy napot (pl:Hétfő, Kedd, stb..): ")
lesson:str = input("Adj meg egy tanóra nevét (pl:Hittan, Programozás, stb..): ")

get_student_condition(day, lesson)

print(f"A megadott szám négyzetgyöke: {get_sqrt()}\n")

get_rectangle_data()


