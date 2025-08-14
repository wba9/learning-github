#get user input
#find the roman equivalent of all integers
# add them together
print('-----------------------------------')
print('Roman Numerals to Integer Converter')
print('-----------------------------------')
integer = input('What is the number you want to convert? \n').lower()

def roman_to_int(number):
    final_answer = 0
    if 'cm' in number:
        final_answer += 900
        number = number.replace('cm', '')
    if 'cd' in number:
        final_answer += 400
        number = number.replace('cd', '')
    if 'xc' in number:
        final_answer += 90
        number = number.replace('xc', '')
    if 'xl' in number:
        final_answer += 40
        number = number.replace('xl', '')
    if 'ix' in number:
        final_answer += 9
        number = number.replace('ix', '')
    if 'iv' in number:
        final_answer += 4
        number = number.replace('iv', '')
        
    for i in number:
        if i == 'm':
            final_answer += 1000
        elif i == 'd':
            final_answer += 500
        elif i == 'c':
            final_answer += 100
        elif i == 'l':
            final_answer += 50
        elif i == 'x':
            final_answer += 10
        elif i == 'v':
            final_answer += 5
        elif i == 'i':
            final_answer += 1
    print(f'The roman numeral you entered is: {final_answer}')


roman_to_int(integer)



