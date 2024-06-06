

none = ' '
x = 'x'
o = '○'

game = [
        [none, none, none],
        [none, none, x],
        [o, none, x]
        ]

print(game)

START_GAME = True


def print_tic_tac_toe():
    board = f"""
 {game[0][0]} │  {game[0][1]}  │ {game[0][2]}
───┼─────┼───
 {game[1][0]} │  {game[1][1]}  │ {game[1][2]}
───┼─────┼───
 {game[2][0]} │  {game[2][1]}  │ {game[2][2]}
"""
    print(board)


atual = "x"

print((f"insira a sua posição de jogada para o {atual}, exemplo: 2,1 "
       "primeiro a linha desejada e depois a coluna "))


print_tic_tac_toe()


while START_GAME:
    position = input()

    positionArray = position.split(',')

    if game[int(positionArray[0])][int(positionArray[1])] != none:
        print("posição inválida, tente novamente")
        atual = atual
    else:
        game[int(positionArray[0])][int(positionArray[1])] = atual
        if atual == x:
            atual = o
        else:
            atual = x
    print_tic_tac_toe()
