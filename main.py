from random import randint
from time import sleep

class Player:
    def __init__(self, name, money):
        self.money = money
        self.name = name

    def bet(self, num, betMoney):
        self.money -= betMoney
        randomNum = randint(0,30)
        print('The random number is: ' + str(randomNum))
        sleep(1)
        if num == randomNum:
            profit = round(betMoney*numbers[num].multiplier,2)
            self.money += profit
            print("Congratulation! You've won $" + str(profit) + '\nNew balance =' , self.money)
        else:
            print('Unlucky! \nNew balance =' , self.money)
        
class Numbers:
    def __init__(self, value):
        self.value = value
        self.multiplier = 1
        self.primes = [2,3,5,7,11,13,17,19,23,29]
    
    def initialiseMultiplier(self):
        if self.value % 2 == 0:
            self.multiplier *= 2
        if self.value % 10 == 0:
            self.multiplier *= 3
        if self.value in self.primes:
            self.multiplier *= 5
        if self.value < 5:
            self.multiplier *= 2
            
numbers = [Numbers(i) for i in range(0,31)]
for i in numbers:
    i.initialiseMultiplier()


player1 = Player('Player1',200)
while True:
    num = int(input('Enter the number you are guessing(between 0 and 30 inclusive): '))
    bet = float(input('Enter your bet: '))
    player1.bet(num,bet)
    if player1.money <= 0:
        print('You are broke!\nBye Bye!')
        break
    