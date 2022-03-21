from random import choice

def main():
    try:
        length = int(input('Enter Length of the password: '))

        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

        small_letters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
                    'w', 'x', 'y', 'z']
        
        caps_letters = [i.upper() for i in small_letters]
        
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        passwd = ''
        
        options = [small_letters, caps_letters, numbers, symbols]
        
        for i in range(0, length):   
             opt = choice(choice(options))
             opt = str(opt)
             passwd+=opt
        
        print('your password: {}'.format(passwd))
        
        
        def again_():
            again = input('Do you want to generate another password? [Y/N]').lower()
            if again == 'y':
                main()
            elif again=='n':
                return False
            else:
                again_()
        again_()
    
    except ValueError:
        print('Enter a valid length')
        main()
main()
