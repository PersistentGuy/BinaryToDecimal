print('Input your binary: ')
binary = list(input('Binary: '))

i = 0

for num in range (len(binary)):
        digit = binary.pop()
        if digit == '1':
            i = i + pow(2, num)
print('the decimal of your binary', i)
	


	

	
	
	
