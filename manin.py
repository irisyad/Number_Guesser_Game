import random


def validate_input(num_gusser):
    if not num_gusser.isdigit():
        print('invalid input please try again')
        return False
    num_gusser = int(num_gusser)
    if num_gusser > 100 or num_gusser < 1 :
        print("your input is out of range please try again [1 , 100]")
        return False
    return True    

def main():
    random_num = random.randint(1,100)
    score = 100
    while True:
        num_gusser = input('Guess a number bettwen 1 and 100 :' )
        if num_gusser == 'q' :
            print('Thank you for your playing')
            break

        if not validate_input(num_gusser):
            continue
        
        num_gusser = int(num_gusser)
        if num_gusser < random_num:
            print("your guess is too low. try again")
        else:
            print("your guess is too hight. try again")
        if num_gusser == random_num:
            print("congratulations .thats True")
            print(f'your score is :{score}')
            play_again = input("Do you whant play again? (y or n)")
            if play_again == 'y':
                score = 100
                random_num = random.randint(1,100)

                continue
            elif play_again == 'n':
                print('Thank you for your playing')
                break

        score -= 5
        score = max(score, 0)



if __name__ == '__main__':
    main()
    