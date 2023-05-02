# KAPREKARS CONSTANT

def kaprekars_constant(number = int(input("Enter a 4 digit number: "))):
  counter = 0
  while len(str(number)) != 4:
    number = int(input("\nMake sure number is 4 digits: "))
    
  while number != 6174:
    if number == 0:
      return 'not possible'
    len1 = len(str(number))
    list1 = []
    big_list = []
    small_list = []
    number = str(number)
    big = ''
    small = ''
    for i in range(0,len1):
      list1.append(number[i])
    for i in list1:
      big_list.append(i)
    for i in list1:
      small_list.append(i)
  
    for i in range(0,len(big_list)):
      big_list[i] = int(big_list[i])
    for i in range(0,len(small_list)):
      small_list[i] = int(small_list[i])
    big_list.sort(reverse=True)
    small_list.sort()
    for i in big_list:
      big += str(i)
    for i in small_list:
      small += str(i)
    number = int(big) - int(small)
    counter += 1
    
    
  return str(counter) + str(" iterations") + ' to 6174'
print(kaprekars_constant())

def kaprekar_iterations():
  for i in range(1000,9999):
    print(f'{i}: {kaprekars_constant(i)}')
# remove the # below and put a # at beggining of line 40 to run all possible iterations
#print(kaprekar_iterations())
