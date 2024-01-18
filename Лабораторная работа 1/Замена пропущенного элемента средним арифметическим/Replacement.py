numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
item_index = 4

number_sum = sum(numbers[:item_index]) + sum(numbers[item_index+1:])
number_count = len(numbers)
numbers_average = number_sum / number_count

numbers[item_index] = numbers_average
print("Измененный список:", numbers)
