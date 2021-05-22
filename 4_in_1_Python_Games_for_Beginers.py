
import random as rand

play_again4 = 'y'
play_again2 = 'y'
while play_again2 == 'y':
    print("Which Game would you like to play: ")
    print("1. Guess the number")
    print("2. Mad libs")
    print("3. Roll a Die")
    print("4. Math Game")
    which_game = input("\nEnter your Choice: ")
    which_game = str(which_game)

    if which_game.isdigit() is False:
        print("Incorrect input")
        play_again2 = 'y'

    if which_game == '1':

        play_again = 'y'
        while play_again == 'y':
            print("Guessing Game!!!")
            rand_num = rand.randint(1, 9)
            num = input("Guess the number from 1 to 9: ")
            num = str(num)
            rand_num = str(rand_num)

            if num.isdigit() is False:
                print("Incorrect input")
                play_again = 'y'

            if num == rand_num:
                print("\nYou are correct!!!")
                rand_num = str(rand_num)
                print("The answer is: " + rand_num)
                play_again = input("\nDo you want to play again? y/n: ")
                play_again = str(play_again)

            elif num != rand_num:
                print("\nYou are wrong!!!")
                rand_num = str(rand_num)
                print("The answer is: " + rand_num)

                play_again = input("\nDo you want to play again? y/n: ")
                play_again = str(play_again)
        # play_again2 = input("Do you want to choose game? y/n: ")
        # play_again2 = str(play_again2)

    elif which_game == '2':
        play_again3 = 'y'
        while play_again3 == 'y':
            print("MAD LIBS")

            word1 = input("\nFirst word:  ")
            word1 = str(word1)
            word2 = input("Second word: ")
            word2 = str(word2)
            word3 = input("Third word:  ")
            word3 = str(word3)

            print("\nRoses are " + word1)
            print("Violets are " + word2)
            print("Everytime I thought of you I see " + word3)

            play_again3 = input("\nDo you want to play again? y/n: ")
            play_again3 = str(play_again3)

    elif which_game == '3':

        while play_again4 == 'y':
            dice = rand.randint(1, 6)
            dice = str(dice)
            print("\nRoll a Die")

            print("\n" + dice)

            play_again4 = input("\nDo you want to roll again? y/n: ")
            play_again4 = str(play_again4)
            if play_again4.isdigit() is True:
                print("Incorrect input!!!")
                play_again4 = input("\nDo you want to roll again? y/n: ")
                play_again4 = str(play_again4)

    elif which_game == '4':
        play_again5 = 'y'
        print("Math Game!")
        while play_again5 == 'y':
            operators = rand.randint(1, 4)
            num_a = rand.randint(0, 99)
            num_b = rand.randint(0, 99)
            num_a = str(num_a)
            num_b = str(num_b)
            if operators == 1:
                sum_1 = int(num_a) + int(num_b)
                print(num_a + "+" + num_b + "=")
                sum_2 = input("Enter the answer: ")
                sum_2 = str(sum_2)
                sum_valid = sum_2.isalpha()
                if sum_valid is True:
                    print("\nIncorrect Input!")
                    play_again5 = 'y'
                else:
                    sum_2 = int(sum_2)

                if sum_1 == sum_2:
                    print("\nYou are Correct!!")
                    play_again5 = input("\nDo you want to play again? y/n: ")
                    play_again5 = str(play_again5)
                elif sum_1 != sum_2:
                    print("\nYou are Wrong!!!")
                    print("\nThe correct answer is: " + str(sum_1))
                    play_again5 = input("\nDo you want to play again? y/n: ")
                    play_again5 = str(play_again5)

            if operators == 2:
                sub_1 = int(num_a) - int(num_b)
                print(num_a + "-" + num_b + "=")
                sub_2 = input("Enter the answer: ")
                sub_2 = str(sub_2)
                sub_valid = sub_2.isalpha()
                if sub_valid is True:
                    print("\nIncorrect Input!")
                    play_again5 = 'y'

                else:
                    sub_2 = int(sub_2)
                if sub_1 == sub_2:
                    print("\nYou are Correct!!")
                    play_again5 = input("\nDo you want to play again? y/n: ")
                    play_again5 = str(play_again5)
                elif sub_1 != sub_2:
                    print("\nYou are Wrong!!!")
                    print("\nThe correct answer is: " + str(sub_1))
                    play_again5 = input("\nDo you want to play again? y/n: ")
                    play_again5 = str(play_again5)

            if operators == 3:
                mul_1 = int(num_a) * int(num_b)
                print(num_a + "*" + num_b + "=")
                mul_2 = input("Enter the answer: ")
                mul_2 = str(mul_2)
                mul_valid = mul_2.isalpha()
                if mul_valid is True:
                    print("\nIncorrect Input!")
                    play_again5 = 'y'
                else:
                    mul_2 = int(mul_2)
                if mul_1 == mul_2:
                    print("\nYou are Correct!!")
                    play_again5 = input("\nDo you want to play again? y/n: ")
                    play_again5 = str(play_again5)
                elif mul_1 != mul_2:
                    print("\nYou are Wrong!!!")
                    print("\nThe correct answer is: " + str(mul_1))
                    play_again5 = input("\nDo you want to play again? y/n: ")
                    play_again5 = str(play_again5)

            if operators == 4:
                div_1 = int(num_a) / int(num_b)
                div_1 = round(div_1, 2)
                print(num_a + "/" + num_b + "=")
                div_2 = input("Enter the answer: ")
                div_2 = str(div_2)
                div_valid = div_2.isalpha()

                if div_valid is True:
                    print("\nIncorrect Input!")
                    play_again5 = 'y'
                else:
                    div_2 = float(div_2)
                if div_1 == div_2:
                    print("\nYou are Correct!!")
                    play_again5 = input("\nDo you want to play again? y/n: ")
                    play_again5 = str(play_again5)
                elif div_1 != div_2:
                    print("\nYou are Wrong!!!")
                    print("\nThe correct answer is: " + str(div_1))
                    play_again5 = input("\nDo you want to play again? y/n: ")
                    play_again5 = str(play_again5)
print("\nThank you for playing :) ")
