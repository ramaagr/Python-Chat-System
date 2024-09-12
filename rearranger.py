def renamer(n,m):
    final='~'+n+'~'+m
    return final
def denamer(m):
    k=0
    name=""
    message=""
    for i in range(1,len(m),1):
        if m[i]!="~" and k==0:
            name+=m[i]
        elif m[i]=="~":
            k=1
        else:
            message+=m[i]
    final=[name,message]
    return final
