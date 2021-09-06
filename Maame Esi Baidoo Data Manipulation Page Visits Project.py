import codecademylib
import pandas as pd
#Loading the csv files into dataframes
visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())                      
print(checkout.head())
print(purchase.head())
#Combining visits and cart using a left merge
visits_and_cart_left = pd.merge(visits, cart, how = "left")
print(visits_and_cart_left)
print(len(visits_and_cart_left))
#Checking how many of the timestamps are null for the cart_time column in the merged df
cart_time_null = visits_and_cart_left[visits_and_cart_left.cart_time.isnull()]
print(cart_time_null)
print("{} out of {} users did not add something to their carts.".format(len(cart_time_null), len(visits_and_cart_left)))
#Finding the percentage of users who did not add something to their cart
print("{} percent of users did not add something to their carts.".format((float(len(cart_time_null)) / float(len(visits_and_cart_left))) * 100))
#Determining the percentage of users who added something to their cart but did not checkout
cart_and_checkout_left = pd.merge(cart, checkout, how = "left")
print(cart_and_checkout_left)
print(len(cart_and_checkout_left))
#Checking how many of the timestamps are null for the checkout_time column in the merged df
checkout_time_null = cart_and_checkout_left[cart_and_checkout_left.checkout_time.isnull()]
print(checkout_time_null)
print("{} out of {} users did not add something to their carts.".format(len(checkout_time_null), len(cart_and_checkout_left)))
#Finding the percentage of users who added something to their cart but did not check out
print("{} percent of users did not checkout after adding something to their carts.".format((float(len(checkout_time_null)) / float(len(cart_and_checkout_left))) * 100))
#Merging all four dataframes using a series of left merges
all_data = visits.merge(cart, how = "left").merge(checkout, how = "left").merge(purchase, how = "left")
print(all_data.head())
#Merging checkout and purchase dataframes with a left merge
checkout_and_purchase_left = pd.merge(checkout, purchase, how = "left")
#Checking how many of the timestamps are null for the purchase_time column in the merged df
purchase_time_null = checkout_and_purchase_left[checkout_and_purchase_left.purchase_time.isnull()]
print(purchase_time_null)
#Finding the percentage of users who added something to their cart but did not purchase anything
print("{} percent of users did not purchase after checking out.".format((float(len(purchase_time_null)) / float(len(checkout_and_purchase_left))) * 100))
#The weakest step is the cart step which has the highest percentage of users not completing it or adding something to their cart with a percentage of 82.6%
#Calculating the average time it takes to purchase something
all_data["time_to_purchase"] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)
print("It takes averagely {} to purchase something from initial visit to the page.". format(all_data.time_to_purchase.mean()))