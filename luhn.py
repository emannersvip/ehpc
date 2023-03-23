# Luhn's Algorithm
# https://en.wikipedia.org/wiki/Luhn_algorithm
cc_num = '5122-3041-6932-2854'
cc_index = 0
cc_luhn = ''

def remove_check_digit(card_num):
   #print(card_num[:-1])
   return card_num[:-1]

def double_and_sum(digit):
    digit_double = int(digit) * 2
    #print('DD: ' + str(digit_double))
    if int(digit_double) > 9:
        digit_sum = int(str(digit_double)[0]) + int(str(digit_double)[1])
        #print('DS: ' + str(digit_sum))
        return digit_sum
    else:
        return digit_double

print('CC#: ' + cc_num)
cc_payload = remove_check_digit(cc_num)
print('Payload: ' + cc_payload)

cc_check_digit = cc_num[-1]
print('Check Digit: ' + cc_check_digit)

# PART 2 - Double every other number beginning from the rightmost digit
for i in reversed(cc_payload):
    if i == '-':
        cc_luhn = cc_luhn + '-'
        continue
    if cc_index % 2 == 0:
        cc_sum = double_and_sum(i)
        print(cc_sum)
        cc_luhn=cc_luhn+str(cc_sum)
    else:
        cc_luhn=cc_luhn+i
    cc_index=cc_index+1

foo=''
bob=reversed(cc_luhn)
cc_luhn=foo.join(bob)
print(cc_luhn)