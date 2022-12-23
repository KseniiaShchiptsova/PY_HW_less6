# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = [4, 1, 6, 3, 5]

def multy_bi(lst):
    return [lst[i] * lst[len(lst)-1 -i] for i in range(len(lst)//2 + len(lst)%2)]

print(multy_bi(lst))