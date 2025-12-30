import numpy as np

products = np.array(["Beer", "Wine", "Whisky", "Vodka", "Gin"])
quantity_sold = np.array([120, 80, 60, 40, 50])
price_per_unit = np.array([250, 800, 1500, 1200, 900])
cost_per_unit = np.array([180, 600, 1100, 900, 650])


revenue = price_per_unit * quantity_sold

print("RRevenue per product sold: ", revenue)

#cost per product

cost =  quantity_sold * cost_per_unit

print("Cost per product sold: ", cost)

#profit per product

profit = revenue - cost

print("profit per product sold : ",  profit)


print("Total revenue is:  ", revenue.sum())

#total  profit

print("Total profit is : ", profit.sum())


# Avareege Revenue per product 

print("Avereage revenue:", revenue.mean())


#BEst and wworse products

best_index = quantity_sold.argmax()

print("The best selling product is :", products[best_index])


#Most profitable product

profit_index =  profit.argmax()

print("The most profitable selling product is:", products[profit_index])


#the worst seling product is 

worst_index  = quantity_sold.argmin()

print("The worst selling product is :", products[worst_index])


#Growth and percentage  contribution to revenue

revenue_percentage = (revenue / revenue.sum()) * 100

for i in range(len(products)):

    print(products[i], ":", round(revenue_percentage[i],2), "%")

print("Revenue percentage contribution by each product")


