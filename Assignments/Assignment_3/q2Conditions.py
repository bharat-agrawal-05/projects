#part a

#the following code checks if the input is a positive number or not
q2part_a=int(input('Enter a number: '))
if q2part_a>0:
    print(q2part_a)

else:
    pass

# part b

#the following code does what the question asks for

q2part_b=input('Enter a number: ')
if q2part_b.isnumeric() or q2part_b[1:].isnumeric():
    if q2part_b[0] == '-' :
        print(-1)

    elif q2part_b[0] != '-' and q2part_b!='0':
        print(1)

    else:
        print(0)

else:
    print("Kindly Enter a number and try again")

#part c
#the following code checks the string type and prints the result accordingly
q2part_c=input('Enter string: ')

if q2part_c.isdigit():      #checks if the string contains only digits
    print(q2part_c,'contains only digits')

elif q2part_c.isalpha():    #checks if the string contains only alphabets
    print(q2part_c,'contains only alphabets')

elif q2part_c.isalnum():    #checks if the string contains both digits and alphabets
    print(q2part_c,'contains both digits and alphabets')


#part-d

q2part_d=input("q4 part d input (string):")
list1=["january", "march", "may", "july", "august", "october", "december"]
list2=["april","june","september","november"]
if q2part_d.lower() in list1:
    print("31 days")
elif q2part_d.lower() in list2:
    print("30 days")
elif q2part_d.lower()=="february":
    year=int(input(("Write the year: ")))
    if year%4==0:
        if year%400==0:
            print("29 days")
        elif year%100==0:
            print("28 days")
        else:
            print("29 days")
    else:
        print("28 days")
else:
    print("wrong input! Kindly run the code again")


# part-e

a=int(input('Enter a number: '))
b=int(input('Enter a number: '))
c=int(input('Enter a number: '))
print(max(a,b,c))
