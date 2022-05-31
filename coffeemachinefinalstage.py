class CoffeeMachine():
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money
                     
    def takeMoney(self):
        print("I gave you ${}".format(self.money))
        self.money = 0
      
    def supplyCheck(self, coffee_choice):
        if coffee_choice == "espresso":
            if self.water // 250 >= 1 and self.coffee_beans // 16 >= 1 and self.cups // 1 >= 1:
                print("I have enough resources, making you a coffee!")
                return True
            else:
                if self.water // 250 < 1:
                    print("Sorry, not enough water!")
                elif self.coffee_beans // 16 < 1:
                    print("Sorry, not enough coffee!")
                elif self.cups // 1 < 1:
                    print("Sorry, not enough cups!")
                
        elif coffee_choice == "latte":
            if self.water  // 350 >= 1 and self.milk // 75 >= 1 and self.coffee_beans // 20 >= 1 and self.cups // 1 >= 1:
                print("I have enough resources, making you a coffee!")
                return True
            else:
                if self.water // 350 < 1:
                    print("Sorry, not enough water!")
                elif self.milk // 75 < 1:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans // 20 < 1:
                    print("Sorry, not enough coffee!")
                elif self.cups // 1 < 1:
                    print("Sorry, not enough cups!")
              
        elif coffee_choice == "cappuccino":
            if self.water  // 200 >= 1 and self.milk // 100 >= 1 and self.coffee_beans // 12 >= 1 and self.cups // 1 >= 1:
                print("I have enough resources, making you a coffee!")
                return True
            else:
                if self.water // 200 < 1:
                    print("Sorry, not enough water!")
                elif self.milk // 100 < 1:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans // 12 < 1:
                    print("Sorry, not enough coffee!")
                elif self.cups // 1 < 1:
                    print("Sorry, not enough cups!")

    def makeEspresso(self):
        self.water -= 250
        self.milk = self.milk
        self.coffee_beans -= 16
        self.cups -= 1
        self.money += 4

    def makeLatte(self):
        self.water -=  350
        self.milk -= 75
        self.coffee_beans -= 20
        self.cups -=  1
        self.money += 7

    def makeCappuccino(self):
        self.water -= 200
        self.milk -= 100
        self.coffee_beans -= 12
        self.cups -= 1
        self.money += 6
  
    def buyOptions(self):
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffee == "1":
            if coffee_machine.supplyCheck("espresso") == True:
                coffee_machine.makeEspresso()
        elif coffee == "2":
            if coffee_machine.supplyCheck("latte") == True:
                coffee_machine.makeLatte()
        elif coffee == "3":
            if coffee_machine.supplyCheck("cappuccino") == True:
                coffee_machine.makeCappuccino()
        elif coffee == "back":
            return
    
    def fillMachine(self):
        self.water += int(input("Write how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.cups += int(input("Write how many disposable cups you want to add:\n"))
        
    
    def __str__(self):
        return f"""The coffee machine has:\n
{self.water} ml of water\n
{self.milk} ml of milk\n
{self.coffee_beans} g of coffee beans\n
{self.cups} disposable cups\n
${self.money} of money"""

    def machineUpdate(self):
        while True:
            selection = input("Write action (buy, fill, take, remaining, exit):")
            if selection == "take":
                coffee_machine.takeMoney()
            elif selection == "buy":
                coffee_machine.buyOptions()
            elif selection == "fill":
                coffee_machine.fillMachine()
            elif selection == "remaining":
                print(coffee_machine)
            elif selection == "exit":
                break
        
coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.machineUpdate()