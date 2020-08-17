def solution(a, b):
    if len(a)>len(b): myStr=f"{b}{a}{b}"
    elif len(b)>len(a): myStr=f"{a}{b}{a}"
    return myStr
