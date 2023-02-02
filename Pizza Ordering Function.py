total = 0
order = []


def homepage():
    print('\nWELCOME TO PIZZA HUNTERS!')
    c = int(input('\nType 1 for CHICKEN PIZZA\nType 2 for BEEF PIZZA\nType 3 for DRINKS\nType 4 for SIDES'
                  '\nType 5 for BILL\nType 6 for END THE PROCESS\nPlease select from above: '))
    if c == 1:
        chicken()
    elif c == 2:
        beef()
    elif c == 3:
        drinks()
    elif c == 4:
        sides()
    elif c == 5:
        bill()
    elif c == 6:
        print('\nThanks for staying with us!')
        homepage()
    else:
        print("Invalid Input. Please try Again!")
        homepage()


def chicken():
    global total, order
    c = int(input('\nType 1 for CHICKEN BBQ PIZZA(650)\nType 2 for CHICKEN SPECIAL PIZZA(750)'
                  '\nType 3 for CHICKEN GARLIC PIZZA(600)\nType 4 for Return Back\nPlease select from above: '))
    if c == 1:
        n = int(input('How many? : '))
        total = total + 650 * n
        order.append(f'CHICKEN BBQ PIZZA x {n} = {n * 650}')
        c = int(input('\nType 1 for CHICKEN PIZZA\nType 2 for BEEF PIZZA\nType 3 for DRINKS\nType 4 for SIDES'
                      '\nType 5 for BILL\nType 6 for END THE PROCESS\nPlease select from above: '))
        if c == 1:
            chicken()
        elif c == 2:
            beef()
        elif c == 3:
            drinks()
        elif c == 4:
            sides()
        elif c == 5:
            bill()
        elif c == 6:
            print('\nThanks for staying with us!')
            homepage()
        else:
            print("Invalid Input. Please try Again!")
            chicken()

    elif c == 2:
        n = int(input('How many? : '))
        total = total + 750 * n
        order.append(f'CHICKEN SPECIAL PIZZA x {n} = {n * 750}')
        c = int(input('\nType 1 for CHICKEN PIZZA\nType 2 for BEEF PIZZA\nType 3 for DRINKS\nType 4 for SIDES'
                      '\nType 5 for BILL\nPlease select from above: '))
        if c == 1:
            chicken()
        elif c == 2:
            beef()
        elif c == 3:
            drinks()
        elif c == 4:
            sides()
        elif c == 5:
            bill()
        elif c == 6:
            print('\nThanks for staying with us!')
            homepage()
        else:
            print("Invalid Input. Please try Again!")
            chicken()

    elif c == 3:
        n = int(input('How many? : '))
        total = total + 600 * n
        order.append(f'CHICKEN GARLIC PIZZA x {n} = {n * 600}')
        c = int(input('\nType 1 for CHICKEN PIZZA\nType 2 for BEEF PIZZA\nType 3 for DRINKS\nType 4 for SIDES'
                      '\nType 5 for BILL\nType 6 for END THE PROCESS\nPlease select from above: '))
        if c == 1:
            chicken()
        elif c == 2:
            beef()
        elif c == 3:
            drinks()
        elif c == 4:
            sides()
        elif c == 5:
            bill()
        elif c == 6:
            print('\nThanks for staying with us!')
            homepage()
        else:
            print("Invalid Input. Please try Again!")
            chicken()

    elif c == 4:
        homepage()

    else:
        print("Invalid Input. Please try Again!")
        chicken()


def beef():
    print('\nSorry, currently not available! Please try later!!')
    c = int(input('\nType 1 for CHICKEN PIZZA\nType 2 for DRINKS\nType 3 for SIDES'
                  '\nType 4 for BILL\nType 5 for END THE PROCESS\nPlease select from above: '))
    if c == 1:
        chicken()
    elif c == 2:
        drinks()
    elif c == 3:
        sides()
    elif c == 4:
        bill()
    elif c == 5:
        print('\nThanks for staying with us!')
        homepage()
    else:
        print("Invalid Input. Please try Again!")
        homepage()


def drinks():
    global total, order
    c = int(input('\nType 1 for PEPSI(25)\nType 2 for COKE(20)'
                  '\nType 3 for MOUNTAIN DEW(25)\nType 4 for Return Back\nPlease select from above: '))
    if c == 1:
        n = int(input('How many? : '))
        total = total + 25 * n
        order.append(f'PEPSI x {n} = {n * 25}')
        c = int(input('\nType 1 for CHICKEN PIZZA\nType 2 for BEEF PIZZA\nType 3 for DRINKS\nType 4 for SIDES'
                      '\nType 5 for BILL\nType 6 for END THE PROCESS\nPlease select from above: '))
        if c == 1:
            chicken()
        elif c == 2:
            beef()
        elif c == 3:
            drinks()
        elif c == 4:
            sides()
        elif c == 5:
            bill()
        elif c == 6:
            print('\nThanks for staying with us!')
            homepage()
        else:
            print("Invalid Input. Please try Again!")
            drinks()

    elif c == 2:
        n = int(input('How many? : '))
        total = total + 20 * n
        order.append(f'COKE x {n} = {n * 20}')
        c = int(input('\nType 1 for CHICKEN PIZZA\nType 2 for BEEF PIZZA\nType 3 for DRINKS\nType 4 for SIDES'
                      '\nType 5 for BILL\nType 6 for END THE PROCESS\nPlease select from above: '))
        if c == 1:
            chicken()
        elif c == 2:
            beef()
        elif c == 3:
            drinks()
        elif c == 4:
            sides()
        elif c == 5:
            bill()
        elif c == 6:
            print('\nThanks for staying with us!')
            homepage()
        else:
            print("Invalid Input. Please try Again!")
            drinks()

    elif c == 3:
        n = int(input('How many? : '))
        total = total + 25 * n
        order.append(f'MOUNTAIN DEW x {n} = {n * 25}')
        c = int(input('\nType 1 for CHICKEN PIZZA\nType 2 for BEEF PIZZA\nType 3 for DRINKS\nType 4 for SIDES'
                      '\nType 5 for BILL\nType 6 for END THE PROCESS\nPlease select from above: '))
        if c == 1:
            chicken()
        elif c == 2:
            beef()
        elif c == 3:
            drinks()
        elif c == 4:
            sides()
        elif c == 5:
            bill()
        elif c == 6:
            print('\nThanks for staying with us!')
            homepage()
        else:
            print("Invalid Input. Please try Again!")
            drinks()

    elif c == 4:
        homepage()

    else:
        print("Invalid Input. Please try Again!")
        drinks()


def sides():
    global total, order
    c = int(input('\nType 1 for FRENCH FRIES(100)\nType 2 for NACHOS(100)\n'
                  'Type 3 for Return Back\nPlease select from above: '))
    if c == 1:
        n = int(input('How many? : '))
        total = total + 100 * n
        order.append(f'FRENCH FRIES x {n} = {n * 100}')
        c = int(input('\nType 1 for CHICKEN PIZZA\nType 2 for BEEF PIZZA\nType 3 for DRINKS\nType 4 for SIDES'
                      '\nType 5 for BILL\nType 6 for END THE PROCESS\nPlease select from above: '))
        if c == 1:
            chicken()
        elif c == 2:
            beef()
        elif c == 3:
            drinks()
        elif c == 4:
            sides()
        elif c == 5:
            bill()
        elif c == 6:
            print('\nThanks for staying with us!')
            homepage()
        else:
            print("Invalid Input. Please try Again!")
            sides()

    elif c == 2:
        n = int(input('How many? : '))
        total = total + 100 * n
        order.append(f'NACHOS x {n} = {n * 100}')
        c = int(input('\nType 1 for CHICKEN PIZZA\nType 2 for BEEF PIZZA\nType 3 for DRINKS\nType 4 for SIDES'
                      '\nType 5 for BILL\nType 6 for END THE PROCESS\nPlease select from above: '))
        if c == 1:
            chicken()
        elif c == 2:
            beef()
        elif c == 3:
            drinks()
        elif c == 4:
            sides()
        elif c == 5:
            bill()
        elif c == 6:
            print('\nThanks for staying with us!')
            homepage()
        else:
            print("Invalid Input. Please try Again!")
            sides()

    elif c == 3:
        homepage()

    else:
        print("Invalid Input. Please try Again!")
        homepage()


def bill():
    print("\n*** BILL ***")
    global total, order
    if total == 0:
        print("\nTotal bill is 0 TK")
    for i in order:
        print()
        print(i)
    if total >= 200:
        tax = total * .1
        total = total + tax
        print(f'\nTAX(10%) = {tax}')
        print("\nTotal bill is", total, 'TK')
    elif total < 200 and total != 0:
        print("\nTotal bill is", total, 'TK')
    print()
    total = 0
    order = []
    homepage()


homepage()