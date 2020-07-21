#source: http://safkaninsan.blogspot.com/2015/05/yeni-baslayanlar-icin-python-projeleri.html

def reverse(value, output=[]):
    #range(start, stop, step)
    for i in range(len(value) - 1, -1, -1):
        output.append(value[i])
    return "".join(output)

text = input("What's up: ")
print(f"Your reversed text is: {reverse(text)}")
