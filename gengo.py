num = input('年数を入力してください(1926~2022)：')
num = int(num)

year_list = list(range(1926,2023))

if num not in year_list:
      raise Exception('範囲外の数値です')

if num >= 2019:
  print('令和:{}年です'.format(num - 2019 + 1))
elif num >= 1989:
  print('平成:{}年です'.format(num - 1989 + 1))
else:
  print('昭和:{}年です'.format(num - 1926 + 1))
