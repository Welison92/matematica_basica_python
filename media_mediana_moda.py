from statistics import mode


values = [3, 5, 7, 9, 12, 14, 17]
mean = sum(values) / len(values)
print("Média: ", mean)

values_sorted = sorted(values)
mid = len(values_sorted) // 2
if len(values_sorted) % 2 == 0:
    median = (values_sorted[mid - 1] + values_sorted[mid]) / 2
else:
    median = values_sorted[mid]
print("Mediana: ", median)

mode = mode(values)
print("Moda: ", mode)
