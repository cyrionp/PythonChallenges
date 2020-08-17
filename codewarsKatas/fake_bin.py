def fake_bin(x):
    myStr=""
    map_object = map(int, x)
    myList = list(map_object)
    for num in myList:
        if num<5:
            myStr+="0"
        else:
            myStr+="1"
    return myStr

def what_is(x):
    if x is 42:
        return 'everything'
    elif x is 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'

print(what_is(42))
print(what_is(2))
print(what_is(42*42))
