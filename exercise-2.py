deposit_amount = float(input('Введите сумму депозита: '))
final_total = float(input('Введите желаемую конечную сумму: '))
year_percent = float(input('Введите годовой процент: '))
month = 0

x = ((year_percent / 12) * deposit_amount)
x += deposit_amount

while x < final_total:
    x += ((year_percent / 12) * x)
    month += 1

print(month)