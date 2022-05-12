for num in range(1,16):
  if num % 15 == 0:
    print('fizzbuzz')
  elif num % 5 == 0:
    print('buzz')
  elif num % 3 == 0:
    print('fizz')
  else:
    print(num)
