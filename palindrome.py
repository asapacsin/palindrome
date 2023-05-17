


def is_palindrome_middle(str,cur_index,max_size):
    left_index = cur_index-max_size
    right_index = cur_index+max_size
    while  left_index != right_index:
        if str[left_index] != str[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True
        
#case start from the both side

def is_palindrome_double(str,cur_index,max_size):
    equal_size = max_size-1
    left_index = cur_index-1-equal_size
    right_index = cur_index+equal_size
    
    while  right_index > left_index:
        if str[left_index] != str[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True

str = "abcba"
size = len(str)
record = str[0]
i = 0
max_middle_size = 0
max_double_size = 0
record_double = ''
flag = 0
while i <size-max_middle_size-1 or i<size-max_double_size:
    #trigger only the space is long enough:
    if i-max_middle_size-1 >= 0 and i+max_middle_size+1 < size:
        if is_palindrome_middle(str,i,max_middle_size+1):
            max_middle_size += 1
            #size = 2*max_middle_size+1 or 2*max_double_size, max_double_size only meaningful when max_double_size >= max_middle_size
            if 2*max_double_size < 2*max_middle_size+1:
                max_double_size = int((2*max_middle_size+1)/2)
            record = str[i-max_middle_size:i+max_middle_size+1]
            flag = 1
    #trigger only the space is long enough for double side
    #i-max_double_size>=0/i > max_double_size
    if i <size-max_double_size and i>max_double_size:
        if is_palindrome_double(str,i,max_double_size+1):
            print('hey!im here')
            max_double_size += 1
            record_double = str[i-max_double_size:i+max_double_size]
            if 2*max_double_size > 2*max_middle_size+1:
                max_middle_size = int((2*max_double_size-1)/2)
            flag = 1
    if flag == 0:
        i += 1
    flag = 0

#convert record to string


try:
    if len(record_double) > len(record):
        record = record_double
except:
    pass

print(record)