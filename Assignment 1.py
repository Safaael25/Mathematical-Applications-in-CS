# Mathematical Applications in Computer Science
# Assignment 1



# Exercise 1

def prime_factors(n):
    result = ""
    divisor = 2  #smallest prime number is 2
    #loop until n is not 1 to find all the prime factors
    while n > 1:
        count = 0  #count the number of times n is divisible by the divisor
        while n % divisor == 0:
            count += 1
            n //= divisor  #divide n by the divisor to know how much times it divisible by the divisor number
        #add the divisor to the result if it is a factor
        if count > 0:
            if result:  #add a * before the divisor if it is not the first factor
                result += "*"
            if count > 1:  #add the count if it is greater than 1
                result += str(divisor) + "^" + str(count)
            else:  #  add the divisor if the count is 1
                result += str(divisor)
        divisor += 1 

    return result


# Exercise 2
# this function takes a list of store names and a list of profits for each store and returns the name of the store with the highest total profit
def best_store(names, profits):
    max_profit = -float('inf')  #initialize the maximum profit to minimum number cause profit can be zero
    max_name = ""
    #loop through the stores
    for i in range(len(names)):
        #calculate total profit for the every store
        total_profit = sum(profits[i])
        #update the max profit and the name of the store if it is greater than the current max profit 
        if total_profit > max_profit:
            max_profit = total_profit
            max_name = names[i]
    
    #tuple usagge to return the name and the profit of the best store like this (name, profit)
    return max_name, max_profit



# Exercise 3
def index_of(n, s):
    list_of_indexes = []
    #loop through the ID number to find the index of the number n
    for i in range(len(s)):
        if s[i] == n:
            list_of_indexes.append(i) # add the index to the list if the number is found
    return list_of_indexes         
    

# You can try your code here:



#print (f"This work is the work of:\n{full_name} ({student_ID})")
