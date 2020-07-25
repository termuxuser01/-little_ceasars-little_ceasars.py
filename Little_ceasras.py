import string


opt = input('enter "e" for encoding or "d" for decoding')
str_org = input("enter desired string:/n")
b_len = int(input("enter a text block size /n default value: 5/n"))
sub_key = int(input("enter a shift key: "))

map_dict = dict()

for i, l in enumerate(string.ascii_lowercase):
  map_dict[i+1] = l


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
