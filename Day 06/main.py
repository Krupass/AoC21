initial = [3,5,1,2,5,4,1,5,1,2,5,5,1,3,1,5,1,3,2,1,5,1,1,1,2,3,1,3,1,2,1,1,5,1,5,4,5,5,3,3,1,5,1,1,5,5,1,3,5,5,3,2,2,4,1,5,3,4,2,5,4,1,2,2,5,1,1,2,4,4,1,3,1,3,1,1,2,2,1,1,5,1,1,4,4,5,5,1,2,1,4,1,1,4,4,3,4,2,2,3,3,2,1,3,3,2,1,1,1,2,1,4,2,2,1,5,5,3,4,5,5,2,5,2,2,5,3,3,1,2,4,2,1,5,1,1,2,3,5,5,1,1,5,5,1,4,5,3,5,2,3,2,4,3,1,4,2,5,1,3,2,1,1,3,4,2,1,1,1,1,2,1,4,3,1,3,1,2,4,1,2,4,3,2,3,5,5,3,3,1,2,3,4,5,2,4,5,1,1,1,4,5,3,5,3,5,1,1,5,1,5,3,1,2,3,4,1,1,4,1,2,4,1,5,4,1,5,4,2,1,5,2,1,3,5,5,4,5,5,1,1,4,1,2,3,5,3,3,1,1,1,4,3,1,1,4,1,5,3,5,1,4,2,5,1,1,4,4,4,2,5,1,2,5,2,1,3,1,5,1,2,1,1,5,2,4,2,1,3,5,5,4,1,1,1,5,5,2,1,1]
showcase = [3,4,3,1,2] #3,4,3,1,2

def after_days(field, days):
    #print("Initial state: " + str(field))
    for day in range(days):
        for i in range(len(field)):
            if(field[i] == 0):
                field[i] = 6
                field.append(8)

            else:
                field[i] -= 1
        #print("After  " + str(day+1) + " days: " + str(field))
        print("After  " + str(day + 1) + " days")

def lanterfish_calculate(field, days):
    numbers = [0,0,0,0,0,0,0,0,0]
    for fish in field:
        numbers[fish] += 1

    print(numbers)

    for day in range(days):
        # print(numbers)
        temp = numbers.copy()
        for i in range(8, -1, -1):
            if (i == 8):
                numbers[i] = temp[0]
            elif (i == 6):
                numbers[i] = temp[7] + temp[0]
            else:
                numbers[i] = temp[i + 1]

    print(numbers)
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    print("\n\nSum: " + str(sum))

#after_days(showcase,256)
#print("Lanterfish in area: " + str(len(showcase)))
lanterfish_calculate(initial,256)
