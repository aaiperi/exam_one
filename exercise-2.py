deposit_amount = float(input('Введите сумму депозита: '))
total = float(input('Введите желаемую конечную сумму: '))
year_percent = float(input('Введите годовой процент: '))
month = 0

while deposit_amount < total:
    deposit_amount *= 1 + (year_percent / 12) / 100
    deposit_amount = int(12 * deposit_amount) / 12
    month += 1
    print(month)