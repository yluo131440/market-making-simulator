import random
import math
import statistics

def calculate_quotes(mid_price, spread):
    bid = mid_price-spread/2
    ask = mid_price+spread/2
    return bid,ask

def calculate_fill_probability(spread,sensitivity):
    return math.exp(-sensitivity*spread)


def execute_trade(inventory, quantity,costumer_side):
    if costumer_side == 'buy':
        inventory -= quantity
    elif costumer_side == 'sell':
        inventory += quantity
    else:
        raise ValueError("only 'buy'or'sell'")
    return inventory

def execute_cash(cash, quantity,costumer_side,bid,ask):
    if costumer_side == 'buy':
        cash += quantity*ask
    elif costumer_side == 'sell':
        cash -= quantity*bid
    else:
        raise ValueError("only 'buy'or'sell'")
    return cash

def adjust_mid_price(mid_price,inventory,target_inventory,adjustment_strength):
    d = inventory - target_inventory
    mid_price = mid_price - d*adjustment_strength
    return mid_price


def run_simulation(orders,inventory,mid_price,target_inventory,adjustment_strength,spread,cash,sensitivity):
    for i in orders:
        adjust_price = adjust_mid_price(mid_price,inventory,target_inventory,adjustment_strength)
        quotes = calculate_quotes(adjust_price,spread)
        bid,ask = quotes
        costumer_side,quantity = i
        probability = calculate_fill_probability(spread,sensitivity)
        if random.random() < probability:
            inventory = execute_trade(inventory,quantity,costumer_side)
            cash = execute_cash(cash,quantity,costumer_side,bid,ask)
            #print("order filled")
        else:
            pass
            #print("order not filled")
        #print(f"costumer_side:{costumer_side},quantity:{quantity},inventory:{inventory},bid:{bid:.2f},ask:{ask:.2f},cash:{cash}")
    return inventory,cash

def calculate_pnl(initial_cash,initial_inventory,final_cash,final_inventory,mid_price):
    final_value = final_cash+final_inventory*mid_price
    initial_value = initial_cash+initial_inventory*mid_price
    pnl = final_value - initial_value
    return pnl

orders = [('buy',3),('sell',5),('buy',2),('sell',4) ]
initial_inventory = 15
mid_price = 100
target_inventory = 10
adjustment_strength = 0.02
spread = 0.20
initial_cash = 10000
sensitivity = 1

results = []
for i in range(1000):
    final_inventory,final_cash= run_simulation(orders,initial_inventory,mid_price,target_inventory,adjustment_strength,spread,initial_cash,sensitivity)
    pnl = calculate_pnl(initial_cash,initial_inventory,final_cash,final_inventory,mid_price)
    results.append(pnl)

averge_pnl = sum(results) / len(results)
profitable_runs = sum(1 for result in results if result > 0)/len(results)
pnl_std = statistics.stdev(results)

print(f"Number of simulation:{len(results)}")
print(f"Average PnL:{averge_pnl}")
print(f"profitable runs:{profitable_runs:1%}")
print(f"PnL standard deviation:{pnl_std}")