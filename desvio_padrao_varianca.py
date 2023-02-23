from statistics import stdev, variance


values = [3, 5, 7, 9, 12, 14, 17]
std_dev = stdev(values)
print("Desvio padrão: ", std_dev)

var = variance(values)
print("Variância: ", var)
