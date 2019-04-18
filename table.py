num = input("Введите один из номеров - 3,12,17 или 80\n")
if num:
    num=int(num)
    if num == 3:
        print("Li")
    elif num ==12:
        print("Mg")
    elif num==17:
        print("Cl")
    elif num==80:
        print("Hg")
    else:
        print("Ошибка!")
else:
    print("Введите снова один из номеров - 3,12,17 или 80")


