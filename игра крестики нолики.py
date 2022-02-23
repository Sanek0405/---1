
field = list(range (1,10))

wins = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def draw_field():
    print("-------------")
    for i in range(3):
        print("|",field [0 + i * 3], "|",field[1 + i * 3],"|", field[2 + i * 3],"|")
    print("-------------")

def take(playar_token):
    while True:
         value = input("Куда поставить:" + playar_token  + " ? " )
         if not (value in "123456789"):
            print("Ошибка ввода, Повторите попытку.")
            continue
         value = int(value)
         if str (field[value - 1]) in "X0":
           print("Клетка занята")
           continue
         field[value - 1] = playar_token
         break
def check():
    for b in wins:
        if (field[b[0]-1]) == (field[b[1]-1]) == (field[b[2]-1]):
           return field[b[1]-1]
    else:
        return False
def main():
    counter = 0
    while True:
        draw_field()
        if counter % 2 == 0:
            take("X")
        else:
            take("O")
        if counter > 3:
            winner = check()
            if winner:
                draw_field()
                print(winner, "Выйграл!")
                break
        counter += 1
        if counter > 8:
            draw_field()
            print("Ничья!")
            break

main()
