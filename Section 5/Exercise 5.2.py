largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        i_num = int(num)
        if largest == None or largest < i_num:
            largest = i_num

        if smallest == None or smallest > i_num:
            smallest = i_num
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
