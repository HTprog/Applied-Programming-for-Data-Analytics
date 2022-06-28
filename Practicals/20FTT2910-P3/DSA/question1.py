#Muhammad Hidayat Hidayat Bin Mohd Yusof
#20FFTT2910
#DA3306 DATA STRUCTURES AND ALGORITHMS

def factorial(number):
    if number==0: #the base case is 0
        return 1
    else:
        return number*factorial(number-1)

#print('factorial of',factorial(5))
print('factorial of 5 is',factorial(5))