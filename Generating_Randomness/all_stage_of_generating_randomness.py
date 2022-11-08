########################## Stage 1/4: Input processing ##########################

def calculate():
    print("Print a random string containing 0 or 1:")
    a = input()
    count = [n for n in a if n == "0" or n == "1"]
    while len(count) < 100:
        print(f"Current data length is {len(count)}, {100 - len(count)} symbols left")
        print("Print a random string containing 0 or 1:")
        print("")
        take = [n for n in input() if n == "0" or n == "1"]
        count.extend(take)
    print("Final data string:")
    print(*count, sep = "") 

calculate()


######################### Stage 2/4: Analyzing user input #########################

binary_3bit = ['000', '001', '010', '011', '100', '101', '110', '111']

def count_(a, b):
    count_0 = 0
    count_1 = 0
    binary_check_list = []
    for i in range(len(a)):
        binary_check_list.append(a[i])
        if len(binary_check_list) == 3:
            if "".join(binary_check_list) == b:
                binary_check_list.pop(0)
                if i < len(a) - 1:
                    if a[i + 1] == "0":
                        count_0 += 1
                    else:
                        count_1 += 1
            else:
                binary_check_list.pop(0)
    print(f"{b}: {count_0},{count_1}")

def calculate():
    print("Print a random string containing 0 or 1:")
    a = input()
    count = [n for n in a if n == "0" or n == "1"]
    while len(count) < 100:
        print(f"Current data length is {len(count)}, {10 - len(count)} symbols left")
        print("Print a random string containing 0 or 1:")
        print("")
        take = [n for n in input() if n == "0" or n == "1"]
        count.extend(take)
    print("Final data string:")
    print("".join(count)) 
    return count

random_input = calculate()

print('')
for i in binary_3bit:
    count_(random_input, i)


######################################### Stage 3/4: Predicting future input #################################

import random

binary_3bit = ['000', '001', '010', '011', '100', '101', '110', '111']
traid_data = dict()


def count_(a, b):
    count_0 = 0
    count_1 = 0
    binary_check_list = []
    for i in range(len(a)):
        binary_check_list.append(a[i])
        if len(binary_check_list) == 3:
            if "".join(binary_check_list) == b:
                binary_check_list.pop(0)
                if i < len(a) - 1:
                    if a[i + 1] == "0":
                        count_0 += 1
                    else:
                        count_1 += 1
            else:
                binary_check_list.pop(0)
    # print(f"{b}: {count_0},{count_1}")
    traid_data[b] = [count_0, count_1]


def calculate():
    print("Print a random string containing 0 or 1:")
    a = input()
    count = [n for n in a if n == "0" or n == "1"]
    while len(count) < 100:
        print(f"Current data length is {len(count)}, {100 - len(count)} symbols left")
        print("Print a random string containing 0 or 1:")
        print("")
        take = [n for n in input() if n == "0" or n == "1"]
        count.extend(take)
    print("Final data string:")
    print("".join(count))
    return count


def predict(test_string, traid_data):
    predict_string = [test_string[0], test_string[1], test_string[2]]
    for i in range(len(test_string) - 3):
        check = "".join([test_string[i], test_string[i+1], test_string[i+2]])
        if traid_data[check][0] > traid_data[check][1]:
            predict_string.append("0")
        elif traid_data[check][0] < traid_data[check][1]:
            predict_string.append("1")
        else:
            predict_string.append(random.choice(["0", "1"]))
    return predict_string


random_input = calculate()
print('')
for i in binary_3bit:
    count_(random_input, i)

test_string = list(input("Please enter a test string containing 0 or 1:\n\n"))

predicted_string = predict(test_string, traid_data)
cont = 0
for i in range(3, len(test_string)):
    if predicted_string[i] == test_string[i]:
        cont += 1

print("prediction:")
print("".join(predicted_string))
print(f"Computer guessed right {cont} out of {len(test_string) - 3} symbols ({(cont / (len(test_string) - 3)) * 100} %)")


########################################## Stage 4/4: ”Generate randomness” game ###################

import random

binary_3bit = ['000', '001', '010', '011', '100', '101', '110', '111']
traid_data = dict()


def count_(a, b):
    count_0 = 0
    count_1 = 0
    binary_check_list = []
    for i in range(len(a)):
        binary_check_list.append(a[i])
        if len(binary_check_list) == 3:
            if "".join(binary_check_list) == b:
                binary_check_list.pop(0)
                if i < len(a) - 1:
                    if a[i + 1] == "0":
                        count_0 += 1
                    else:
                        count_1 += 1
            else:
                binary_check_list.pop(0)
    # print(f"{b}: {count_0},{count_1}")
    traid_data[b] = [count_0, count_1]


def calculate():
    print("Print a random string containing 0 or 1:")
    a = input()
    count = [n for n in a if n == "0" or n == "1"]
    while len(count) < 100:
        print(f"Current data length is {len(count)}, {100 - len(count)} symbols left")
        print("Print a random string containing 0 or 1:")
        print("")
        take = [n for n in input() if n == "0" or n == "1"]
        count.extend(take)
    print("Final data string:")
    print("".join(count))
    return count


def predict(test_string, traid_data):
    predict_string = [test_string[0], test_string[1], test_string[2]]

    for i in range(len(test_string) - 3):

        check = "".join([test_string[i], test_string[i+1], test_string[i+2]])

        if traid_data[check][0] > traid_data[check][1]:
            predict_string.append("0")
        elif traid_data[check][0] < traid_data[check][1]:
            predict_string.append("1")
        else:
            predict_string.append(random.choice(["0", "1"]))

    return predict_string


print("""
Please give AI some data to learn...
The current data length is 0, 100 symbols left""")

random_input = calculate()
print('')
for i in binary_3bit:
    count_(random_input, i)

dollar = 1000
print('''
You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!''')

while True:
    test_string = list(input("Print a random string containing 0 or 1::\n\n"))
    if "".join(test_string) == 'enough':
        break
    elif "0" not in test_string or "1" not in test_string:
        continue
    predicted_string = predict(test_string, traid_data)
    cont = 0
    for i in range(3, len(test_string)):
        if predicted_string[i] == test_string[i]:
            cont += 1

    print("prediction:")
    print("".join(predicted_string))
    print(f"Computer guessed right {cont} out of {len(test_string) - 3} symbols ({(cont / (len(test_string) - 3)) * 100} %)")
    dollar = dollar - cont + ((len(test_string) - 3) - cont)
    print(f'Your balance is now ${dollar}')

print("Game over!")

