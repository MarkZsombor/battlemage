
def main():
    print_header()
    game_loop()


def print_header():
    print('          Battlemage')


def game_loop():

    while True:

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
        if cmd == 'a':
            print('a')
        elif cmd == 'r':
            print('r')
        elif cmd == 'l':
            print('l')
        else:
            print('Exiting Game')
            break


if __name__ == '__main__':
    main()