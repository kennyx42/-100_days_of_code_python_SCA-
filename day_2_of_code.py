#If the bill was $150.00, split between 5 people, with 12% tip. 

print('There\'s no need to argue!, let\'s help split that bill!')

Bill=int(input('How much is the bill?$ '))

tip=int(input('Enter tip to leave:$ '))

num_of_friends=int(input('Enter the number of people: '))

#Each person should pay (150.00 / 5) * 1.12 = 33.6

tip_in_percent=float(tip)/100

new_bill=Bill+tip_in_percent



bill_per_person=(new_bill/num_of_friends)
#
#Format the result to 2 decimal places 

rounded_bill_per_person=round(bill_per_person,2)

print(f'Each person will pay ${rounded_bill_per_person}')