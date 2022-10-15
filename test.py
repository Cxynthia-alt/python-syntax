# # age = 19

# if age >= 21:
#   print('can drnik')
# elif age >= 18:
#   print('drive but no drink')
# else:
#   print('nope')

# count = 0
# while count < 10:
#   if count == 5:
#     break
#   count += 1
#   print(count)
# print('done')

# target = 20
# guess = None
# while guess != target:
#   guess = input('enter your guess')
#   if guess == 'q':
#     break
#   guess = int(guess)
# print('awesome stuff')

# nums = [1, 2, 3, 4, 5]
# for num in nums:
#   print(num)

# for char in 'character':
#   print(char)

def add_nums(a,b):
  sum = a + b
  print('math')
  return sum

def greet(person):
  return f'hello, {person}'

def divide(a,b):
  if type(a) is int and type(b) is int:
    return a/b
  return 'a and b must be integers :)'

def send_email(to_email, from_email, subject, body):
  email = f'''
    to: {to_email}
    from: {from_email}
    subject: {subject}
    -------------------
    body:{body}
    '''
  print(email)

send_email('my cat', 'me', 'check-in', 'I miss you')
send_email(to_email = 'my dog', from_email = 'me', subject = 'check-in', body ='I miss you')

def power(num, power=3):
  return num**power
