import add_elem_in_array, modify_elem_array, certain_properties, obtain_from_list, filter_values

main_list = []
undo_stack = []


def read_from_file():
    fin = open("input.txt", "r")
    str_list = []
    str_list = fin.read()
    for elem in str_list.split(","):
        main_list.append(int(elem))
    fin.close()


def write_to_file():
    fout = open("output.txt", "w")
    fout.write(str(main_list))
    fout.close()


# run test here
add_elem_in_array.test_add1()
add_elem_in_array.test_add2()
certain_properties.test_odd()
certain_properties.test_prime()
filter_values.test_filter_negative()
filter_values.test_filter_prime()
modify_elem_array.test_remove1()
modify_elem_array.test_remove2()
modify_elem_array.test_replace()
obtain_from_list.test_gcd()
obtain_from_list.test_max()
obtain_from_list.test_sum()


def UI():  # this is the menu
    global undo_stack
    print(
        """
    The menu:

    7. Data

    1. Add number to array 
    2. Modify number in the array 
    3. Get the number that has certain properties 
    4. Obtain different characteristics from sub-array 
    5. Filter values 
    6. Undo
    0. Exit

    """
    )
    print("your list is:", main_list, "\n\n")

    ok = True

    while ok:
        path = input("Which path do you want to go? (1-6): ")
        if validate_path(path, 1):
            path = int(path)
            if path == 0:  # 0. exit
                ok = False
                print("exit...")
                return
            elif path == 1:  # 1. add number to array
                path1()
                undo_stack.append(main_list[:])
            elif path == 2:  # 2. modify array
                path2()
                undo_stack.append(main_list[:])
            elif path == 3:  # 3. properties of list
                path3()
                undo_stack.append(main_list[:])
            elif path == 4:  # 4. obtain from list
                path4()
            elif path == 5:  # 5. filter values
                path5()
                undo_stack.append(main_list[:])
            elif path == 6:  # 6. undo
                path6()
            elif path == 7:  # 7. data
                path7()
                undo_stack.append(main_list[:])


def validate_path(path, valid_range):  # path and type of path
    try:
        path = int(path)
        if (path < 0 or path > 7) and valid_range == 1:
            print("Value out of range, please try again")
            return False
        elif valid_range == 2 and (path < 0 or path > 2):
            print("Value out of range, please try again")
            return False
        elif valid_range == 3 and (path < 0 or path > 3):
            print("Value out of range, please try again")
            return False
    except ValueError:
        print("Invalid input, please try again")
        return False
    return True


def path1():  # path 1.
    global main_list, undo_stack
    print(
        """
    1. Add element to list
    2. Insert element to index"""
    )
    subpath = input("What subpath do you want to follow?: ")
    if validate_path(subpath, 2):
        subpath = int(subpath)
        if subpath == 1:
            value_to_add = int(input("Value to add to list: "))
            main_list = add_elem_in_array.add1(main_list, value_to_add)
            print("List with the new element:", main_list)
        elif subpath == 2:
            value_to_add = int(input("Value to add to list: "))
            index_to_add = int(input("Index to add at: "))
            main_list = add_elem_in_array.add2(main_list, index_to_add, value_to_add)
            print("List with the new element at index:", main_list)


def path2():  # path 2.
    global main_list
    print(
        """
1. Remove element at index
2. Remove elements from an index to another 
3. Replace old value with new one"""
    )

    subpath = input("What subpath do you want to follow?: ")
    if validate_path(subpath, 3):
        subpath = int(subpath)
        if subpath == 1:
            index = int(input("Remove element at index: "))
            main_list = modify_elem_array.remove1(main_list, index)
            print("The list without that index is:", main_list)
        elif subpath == 2:
            first_index = int(input("Remove from index: "))
            last_index = int(input("Remove to index: "))
            main_list = modify_elem_array.remove2(main_list, first_index, last_index)
            print("The list with the element between indexes removed:", main_list)
        elif subpath == 3:
            print(main_list)
            old_values = []
            new_values = []
            value_replace = input("What value to replace?: ")
            oldd_values = value_replace.split()
            for elem in oldd_values:
                old_values.append(int(elem))

            value_replace_new = input("Replacement: ")
            neww_values = value_replace_new.split()
            for elem in neww_values:
                new_values.append(int(elem))

            main_list = modify_elem_array.replace(main_list, old_values, new_values)
            print("The list with the old values replaced:", main_list)


def path3():  # path 3.
    global main_list
    print(
        """
1. Get prime numbers from index to another
2. Get odd numbers from index to another"""
    )

    prime_numberes = []
    odd_numbers = []

    subpath = input("What subpath do you want to follow?: ")
    if validate_path(subpath, 2):
        subpath = int(subpath)
        if subpath == 1:
            first_index = int(input("Search from index: "))
            last_index = int(input("Stop search at index: "))
            prime_numberes = certain_properties.prime(
                main_list, first_index, last_index
            )
            print("The prime numbers between indexes are:", prime_numberes)
        elif subpath == 2:
            first_index = int(input("Search from index: "))
            last_index = int(input("Stop search at index: "))
            odd_numbers = certain_properties.odd(main_list, first_index, last_index)
            print("The odd numbers between indexes are:", odd_numbers)


def path4():  # path 4.
    global main_list
    print(
        """
1. Get sum of numbers from index to another
2. Get greatest common divisor of numbers from index to another          
3. Get maximum of numbers from index to another"""
    )

    sum_elements_between_index = 0
    greatest_common_divisor_between_index = 0
    max_between_index = 0

    subpath = input("What subpath do you want to follow?: ")
    if validate_path(subpath, 3):
        subpath = int(subpath)
        if subpath == 1:
            first_index = int(input("Search from index: "))
            last_index = int(input("Stop search at index: "))
            # testsum
            # sum = obtain_from_list.sum()
            sum_elements_between_index = obtain_from_list.sum(
                main_list, first_index, last_index
            )
            print("The sum between those indexes is:", sum_elements_between_index)
        elif subpath == 2:
            first_index = int(input("Search from index: "))
            last_index = int(input("Stop search at index: "))
            greatest_common_divisor_between_index = obtain_from_list.gcd(
                main_list, first_index, last_index
            )
            print(
                "The greatest common divisor between these indexes is:",
                greatest_common_divisor_between_index,
            )
        elif subpath == 3:
            first_index = int(input("Search from index: "))
            last_index = int(input("Stop search at index: "))
            max_between_index = obtain_from_list.maxx(
                main_list, first_index, last_index
            )
            print("The maximum element between the indexes is:", max_between_index)


def path5():  # path 5.
    global main_list
    print(
        """
1. Filter the prime numbers in list
2. Filter the negative numbers in list        
"""
    )

    only_prime = []
    only_negative = []

    subpath = input("What subpath do you want to follow?: ")
    if validate_path(subpath, 2):
        subpath = int(subpath)
        if subpath == 1:
            only_prime = filter_values.filter_prime(main_list)
            print("Only the prime numbers in the list:", only_prime)
        elif subpath == 2:
            only_negative = filter_values.filter_negative(main_list)
            print("Only the negative numbers in the list:", only_negative)


def path6():  # path 6.
    global main_list, undo_stack
    if len(undo_stack) > 1:
        undo_stack.pop()
        main_list = undo_stack[-1][:]
        print("\nUndo successful. Current list:", main_list)
    else:
        print("\nNo actions to undo.\n")


def path7():  # path 7.
    print("1. Read data\n2. Write data")
    subpath = int(input("What subpath do you want to go?: "))
    if subpath == 1:
        read_from_file()
        print("Your list is:", main_list)
    elif subpath == 2:
        write_to_file()
        print("The values are in output.txt file")


UI()
