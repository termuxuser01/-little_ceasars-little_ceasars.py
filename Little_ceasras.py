import string
opt = input('enter "e" for encoding or "d" for decoding')
str_org = input("enter desired string:/n")
b_len = int(input("enter a text block size /n default value: 5/n"))
sub_key = int(input("enter a jump key: "))
map_dict = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

def option(ed):
    if ed == "e":
        print("going to encode funtion")
        enc()
    elif ed == "d":
        print("going to decoding funcrion")
        dec()
    else:
        opt = input('invalid option, enter "e" to encode or "d" to decode')
    
try:
    if opt != "e" or opt != "d":
        raise exception
except:
    opt = input('enter "e" for emcoding or "d" for decoding: ')
finally:
    option(opt)

#select encode or decode

#declaration 
#split into char
str_rem = ""
str_lst = list(str_org)
for x in str_lst:
    if x == " ":
        continue
    else:
        str_rem += x
print(str_rem)
#obtain index
#skip numbers
#pump chars


#decode
#obtain chars
#revese
