# python module
import time   #for time backend
import random   #for random numbers
# Module End

# veriable start

t1 = time.time()
winning_number = random.randint(1,100) #Can input any number like(1,50,100, n)
guess = 1
game_over = False

# veriable end

# input Your Number 
number = int(input(' Enter your Number:  '))

# While loop and start Your Game
while not game_over:

    #Nested if condition 
    if number == winning_number:
        print(f'You win, and the gussing number is {guess} times \n Thank You For Playing \U0001F642')
        game_over = True   # Game over
        # t2 is a veriable
        t2 = time.time()
        # t2 end here
        print(f'Your Gaming Process Time(Backend Time): {t2-t1}') #for backend time process
        input('Press Enter to Close ')
        
    else:
        if number < winning_number:
            print(f'Too low')
        else:
            print(f'Too high')
        #Nested If condition end

        guess += 1
        number = int(input('Guess Again: '))
       
        
        
        # <------------------------------------   Happy Gaming  ------------------------------------------->
        

        



    

    



