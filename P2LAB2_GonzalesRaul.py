num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4


formatted_product_int = f'{product:.0f}'
formatted_average_int = f'{average:.0f}'
formatted_product_float = f'{product:.3f}'
formatted_average_float = f'{average:.3f}'

print(f'{formatted_product_int} {formatted_average_int}')
print(f'{formatted_product_float} {formatted_average_float}')