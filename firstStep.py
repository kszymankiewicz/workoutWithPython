name = ''
while True:
    print('Please type your name ')
    name = input()
    if name == 'your name':
        break
    else: 
        print('Try again.')

print('Thank you')

total = 0
for num in range(101):
    total = total + num
print('sum: '+ str(num) + ' total: ' + str(total))