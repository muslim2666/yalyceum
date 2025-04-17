import sys


def main_menu():
    print('Выберите игру:')
    print('1. Snake')
    print('2. Tetris')
    print('0. Выход')
    choice = input('Ваш выбор: ')
    return choice


def main():
    while True:
        choice = main_menu()

        if choice == '1':
            from snake_game.game import Game 
            Game().run()
        elif choice == '2':
            from tetris_game.game import Game 
            Game().run()
        elif choice == '0':
            print('До свидания!')
            sys.exit()
        else:
            print('Некорректный ввод. Попробуйте снова.')


if __name__ == '__main__':
    main()