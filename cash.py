def main():
    while True:
        inp = input('O hai! How much change is owed?')

        try:
            amount = float(inp)
            if amount > 0 or type(amount) == str:
                break
        except:
            print('You can\'t input a string')

    cents = int(round(amount*100.0))
    number_of_coins = 0

    number_of_coins += cents // 25
    cents %= 25

    number_of_coins += cents // 10
    cents %= 10

    number_of_coins += cents // 5
    cents %= 5

    number_of_coins += cents

    print (number_of_coins)

if __name__ == "__main__":
    main()
