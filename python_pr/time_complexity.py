def print_first_item_them_first_half_then_say_hi_100_times(item):
    print(item[0])

    middle_index = len(item) // 2
    index = 0
    while index < middle_index:
        print(item[index])
        index += 1

    for time in range(100):
        print("Hi")

# this is 0(big oh)(1+n/2+100) 