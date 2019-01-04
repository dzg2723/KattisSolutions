import math

num_of_teas = int(input())
tea_prices = [int(x) for x in input().split()]

toppings_num = int(input())
topping_prices = [int(x) for x in input().split()]

##print("TEA: ", tea_prices)
##print("Tops: ", topping_prices)

cheapest_tea = 0
for i in range(num_of_teas):
    allowed_tops = [int(x) for x in input().split()]
    
    for j in allowed_tops[1:]:
        tea_combination = tea_prices[i] + topping_prices[j-1]
##        print(i, j, tea_combination)
        
        if (cheapest_tea == 0):
            cheapest_tea = tea_combination
        elif (tea_combination < cheapest_tea):
            cheapest_tea = tea_combination
            

money = int(input())
cups_to_buy = math.floor(money/cheapest_tea)
students = max(cups_to_buy - 1, 0)
print(students)
