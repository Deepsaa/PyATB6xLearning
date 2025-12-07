def print_mul_arg(*deepsa_list):
    # args - List
    for i in deepsa_list:
        print(i)


print_mul_arg("deepsa")
print_mul_arg(2, 3, 1, 4, 3, 2, 2, 2, 2, 2, 2)
print_mul_arg("deepsa", "sahu")
print_mul_arg("deepsa", "sahu", "third")
print_mul_arg("deepsa", "sahu", "third", 3.14)
print_mul_arg("deepsa", "sahu", "third", 3.14, True)