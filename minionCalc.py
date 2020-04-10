import sys,os
def clear():
    os.system("cls")
    
hour = 3600
def main():
    diamond_spreading = False
    global minion_upgrade
    print("please enter minion's time between actions in seconds")
    action_time = float(input())
    print("_______________________________________________________________")

    print('please enter the sell price of 1 item')
    price_per = float(input())
    print("_______________________________________________________________")

    print("please enter the amount of items obtained per action")
    items_per_action = float(input())
    print("_______________________________________________________________")

    print("please choose your minion fuel. *Fuel duration is not taken into calculation")
    print("1) e-lava Bucket \n2) hamster wheel \n3) foul flesh \n4) e-charcoal \n5) none\n")
    fuel_answer = int(input())
    if fuel_answer == 1:
        minion_fuel = 1.25         
    elif fuel_answer == 2:
        minion_fuel = 1.50  
    elif fuel_answer == 3:
        minion_fuel = 1.90      
    elif fuel_answer == 4:
        minion_fuel = 1.20      
    elif fuel_answer == 5:
        minion_fuel = 1            
    else:
        print('fuel set to none')
        minion_fuel = 1
    print("_______________________________________________________________")

    print('please choose a minion upgrade')
    print('1) diamond spreading\n2) flycatcher\n3) minion expander\n4) none\n')
    upgrade_answer = int(input())

    if upgrade_answer == 1:
        diamond_spreading = True
        minion_upgrade = 0
    elif upgrade_answer == 2:
        minion_upgrade = 0.20
    elif upgrade_answer == 3:
        minion_upgrade = 0.05
    elif upgrade_answer == 4:
        minion_upgrade = 0
    print("_______________________________________________________________")

    print('how many minions are you using?')
    minion_amount = float(input())
    print("_______________________________________________________________")







    fuel_efficency = 1 / minion_fuel
    upgrade_efficiency = 1 / (minion_upgrade + 1)
    action_time = action_time * fuel_efficency * upgrade_efficiency
    actions_per_hour = hour / action_time
    items_per_hour = actions_per_hour * items_per_action
    profit_per_hour = items_per_hour * minion_amount * price_per

    if diamond_spreading == True:
        spreding_money = items_per_hour / 10 * 8 * minion_amount
        profit_per_hour = profit_per_hour + spreding_money





    profit_per_day = profit_per_hour * 24
    profit_per_week = profit_per_day * 7

    clear()
    print("Profit Per Hour = "+'{:20,.2f}'.format(profit_per_hour).replace(" ", '')+ " coins")
    print("Profit Per Day = "+'{:20,.2f}'.format(profit_per_day).replace(" ", '')+" coins")
    print("Profit Per Week = "+'{:20,.2f}'.format(profit_per_week).replace(" ", '')+" coins")
    print("_______________________________________________________________")

    print("1) Restart \n2) Exit\n")
    command = input()
    if command == "2":

        exit()
    else:
        print("_______________________________________________________________")
        main()
        clear()

print("_______________________________________________________________\n\nwelcome to minion price calculator\noriginally by ThirtyVirus https://youtube.com/thirtyvirus/\nremade in python by reaal https://github.com/reaaldev/\n_______________________________________________________________")




main()    
