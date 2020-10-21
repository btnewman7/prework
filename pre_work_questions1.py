#Question 1

def hello_name(user_name):
    username = input(user_name)
    print("hello_" + username.upper() + "!")

hello_name('What is your user name?')

#Derek's Answer

def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")
hello_name('USERNAME')

#Question 2

for value in range(1,200):
    if value % 2 != 0:
        print(value)

#Derek's Answer 

def first_odds(n):
    i = 1
    odd_nums = 0

    while i <= n:
        if odd_nums % 2 != 0:
            print(f"{i}:{odd_nums}")
            i+=1
        odd_nums += 1

first_odds(100)

#Question 3

def max_num_in_list(a_list):
    print(max(a_list))   

#Derek's Alternative Answer
'''sorted(a_list)[-1]'''
#or
'''sorted(a_list, reverse=True)[0]'''

#Question 4

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return "Is a leap year!"
            else:
                return "Is not a leap year!"
        else:
            return "Is a leap year!"
    else:
        return "Is not a leap year!"
print(is_leap_year(400))

#Derek's Answer

def get_leap_years():
    current_iteration = 1
    year = 2000

    while year < 3001:
        if year%4==0 and year%100!=0 or year%400 == 0:
            print(f"{current_iteration}: {year}")
            current_iteration += 1
        year += 1

get_leap_years()

#Question 5

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list),max(a_list)+1))
lst = [12, 13, 11, 14, 15] 
print(is_consecutive(lst))

#Derek's Answer

def is_consecutive(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i] + 1 != a_list[i+1]:
            return False
    return True