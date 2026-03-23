m = input("Nhập danh sách các số")
numbers = [int(x) for x in m.split()]

even_numbers = []
total_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        total_sum += num
print("Các số chẵn trong danh sách:", even_numbers)
print("Tổng các số chẵn là:", total_sum)
