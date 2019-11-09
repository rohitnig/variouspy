# input has been taken for you

'''
Basic understanding:
    The list will always be properly sorted either to the right of the cursor or left of it
    We have to understand which side of the cursor is the list sorted
    We have to pick which direction we need to proceed and which list part we need to dump
'''

input_list = [ 3, 2, 1, 14, 15, 16, 17, 20, 24, 27, 29, 31, 33, 36, 39]
key = 14

l=0; r=len(input_list)-1

found= False
cursor = (l+r)//2

while (l<r):
    cursor = (l+r)//2
    if key == input_list[cursor]:
        found=True
        break
    elif key == input_list[l]:
        cursor = l
        found=True
        break
    elif key == input_list[r]:
        cursor = r
        found = True
        break
    elif cursor==l or cursor==r:
        print ('Not found')
        break
    elif input_list[cursor-1] > input_list[cursor] and input_list[cursor] < input_list[cursor+1]: # right in the middle
        print ('Middle!')
        if key > input_list[cursor]:
            print ('.. Going left')
            r = cursor - 1
        else:
            print ('.. Going right')
            l = cursor + 1
    elif input_list[cursor-1] < input_list[cursor] and input_list[cursor] < input_list[cursor+1]: # cursor is in a ascending part of the list
        print ('Ascending')
        if key > input_list[cursor]:
            print ('.. Going right')
            l = cursor + 1        
        else:
            r = cursor - 1
            print ('.. Going left')
    elif input_list[cursor-1] > input_list[cursor] and input_list[cursor] > input_list[cursor+1]: # cursor is in a descending part of the list
        print ('Descending')
        if key > input_list[l]: # then the key is not in the descending list, must be at the rightmost section
            print ('.. Going right: 1')
            l = cursor+1
        elif key > input_list[cursor]: # good, the key is somewhere in this list leftwards
            print ('.. Going left')
            r = cursor-1
        else: # okay, the key is at the rightwards
            print ('.. Going right: 2')
            l = cursor+1
    
print (found, cursor)
