leap = [r''' 88                                                ,ad8888ba,  88                                88
88                                               d8"'    `"8b 88                                88
88                                              d8'           88                                88
88          ,adPPYba, ,adPPYYba, 8b,dPPYba,     88            88,dPPYba,   ,adPPYba,  ,adPPYba, 88   ,d8
88         a8P_____88 ""     `Y8 88P'    "8a    88            88P'    "8a a8P_____88 a8"     "" 88 ,a8"
88         8PP""""""" ,adPPPPP88 88       d8    Y8,           88       88 8PP""""""" 8b         8888[
88         "8b,   ,aa 88,    ,88 88b,   ,a8"     Y8a.    .a8P 88       88 "8b,   ,aa "8a,   ,aa 88`"Yba,
88888888888 `"Ybbd8"' `"8bbdP"Y8 88`YbbdP"'       `"Y8888Y"'  88       88  `"Ybbd8"'  `"Ybbd8"' 88   `Y8a
                                 88
                                 88  ''']
print(leap[0])



def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

year=int(input("Enter the year: \n "))
print(is_leap_year(year))
