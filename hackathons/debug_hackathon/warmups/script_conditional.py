def find_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:  # Set a conditional breakpoint here: `num == 4`
            print(f"Found an even number: {num}")
            return num
    return None

my_numbers = [1, 3, 5, 2, 4, 6]
even_num = find_even_number(my_numbers)
print(f"First even number found: {even_num}")
