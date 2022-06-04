def hello():
    print("hello")


def pack(item_one, item_two, item_three):
    return [item_one, item_two, item_three]


def eat_lunch(input_list):
    if len(input_list) != 0:
        for i in range(0, len(input_list)):
            if i == 0:
                print("First I eat "+input_list[i])
            else:
                print("Next I eat "+input_list[i])
    else:
        print("My lunchbox is empty!")


hello()

print(pack("cheese", "ham sandwich", "cookie"))

eat_lunch(["a ham sandwich", "a slice of cheese", "a cookie"])
