import string

def preference(a):
    l={"+":1,
        "-":1,
        "*":2,
        "/":2,
        "^":3,
       "(":4,
       ")":5}
    return l[a]

def check_operator(a):
    if a in string.ascii_lowercase:
        return False
    return True


def infix_to_postfix(infix):
    mainstack=[]
    operator=[]
    for i in infix:
        if check_operator(i):
            if len(operator)==0:
                operator.append(i)
            else:
                if i==")":
                    x=operator.pop()
                    while x!="(":
                        mainstack.append(x)
                        x=operator.pop()
                else:
                    if i=="(":
                        operator.append(i)
                    else:
                        if operator[-1]=="(":
                            operator.append(i)
                        else:
                            if preference(operator[-1])<=preference(i):
                                operator.append(i)
                            else:
                                while preference(operator[-1])>=preference(i) and operator[-1]!="(":
                                    mainstack.append(operator.pop())
                                    if len(operator)==0:
                                        break
                                operator.append(i)
        else:
            mainstack.append(i)

    if len(operator)!=0:
        while len(operator)!=0:
            mainstack.append(operator.pop())
    print(mainstack)

exp = "a+b*(c^d-e)^(f+g*h)-i"
infix_to_postfix(exp)
                        
                    
                    
