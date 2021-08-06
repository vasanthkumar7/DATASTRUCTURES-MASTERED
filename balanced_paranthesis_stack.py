def balanced_paranthesis(exp):
    stack=[]
    opens=["(","[","{"]
    close=[")","]","}"]
    if exp[0] in close:
        return False
    lastopened=exp[0]
    stack.append(exp[0])
    for i in range(1,len(exp)):
        if exp[i] in close:
            if lastopened:
                if opens.index(lastopened) == close.index(exp[i]) :
                    stack.pop()
                    if len(stack)!=0:
                        lastopened=stack[-1]
                    else:
                        lastopened= False 
            else:
                return False
        else:
            lastopened=exp[i]
            stack.append(exp[i])

    if len(stack)!=0:
        return False
    return True

if balanced_paranthesis("{{{}}}") :
    print("balanced")
