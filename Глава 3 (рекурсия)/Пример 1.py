# У рекурсивной функции обязательно должно быть условие прерывания!

def countdown(i: int):
    if (i < 0):
        return
    else:
        print(i)
        countdown(i-1)

countdown(10)