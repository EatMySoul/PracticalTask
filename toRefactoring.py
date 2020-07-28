code = """n = int(input())
if n > 5:
    print("n>5")

else:
     print("n<5")
#end""" 
exec(code)
textio = code.split('\n')
def finder(block_scheme,text,tab = 0):
    print('ultradebug',block_scheme)
    i = 0
    itemp = 0
    print('deeper')
    for string in text:
        i += 1
        if i < itemp:
            continue
        if string[:tab] == tab*' ':
            if 'input' in string:
                block_scheme.append('input')
            elif 'print' in string:
                print('ill see it',string)
                block_scheme.append('print')
            elif 'if' in string:
                zveno = ['if']
                tab += 4
                temp = text[i:]
                zveno = finder(zveno,temp,tab)
                tab -= 4 
                itemp = len(zveno) + i
                block_scheme.append(zveno)
            elif 'else' in string: #like if + then
                print('hello')
                zveno = ['else']
                tab += 4
                print(zveno,'debug')
                temp = text[i:]
                print(temp)
                zveno = finder(zveno,temp,tab)
                tab -= 4
                print(zveno,'hmm')
                itemp = len(zveno) + i
                block_scheme.append(zveno)
        else:
            print("using return",string)
            return block_scheme
    return block_scheme

block_scheme1 = []
block_scheme1 = finder(block_scheme1,textio)
print(block_scheme1)
