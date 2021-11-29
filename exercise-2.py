# deposit_sum = []
# final_desired_sum = []
# yearly_percent = []
# future_value = []
#
# def calc_percent(sum, total_sum, year_percent):
#     for months in range(13):
#     month =
#     yearly_percent/12* deposit_sum + deposit_sum

deposit_amount = float(input('Введите сумму депозита: '))
total = float(input('Введите желаемую конечную сумму: '))
year_percent = float(input('Введите годовой процент: '))
month = 0

while deposit_amount < total:
    deposit_amount *= 1 + (year_percent / 12) / 100
    deposit_amount = int(12 * deposit_amount) / 12
    month += 1
    print(month)


