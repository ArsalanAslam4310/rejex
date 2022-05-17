def mad_libs(string : str)->str:
    '''
    replace in string
    '''
    str=string.split()
    
    for i in range(len(str)):
        if str[i]=="ADJECTIVE":
            str[i]=input()
        if str[i]=="NOUN":
            str[i]=input()
        if str[i]=="VERB.":
            str[i]=input()
        sentence=" ".join(str)
    return sentence
       

mad_lib=open("madlibs.txt",'r')
content=mad_lib.read()
mad_lib.close()
print(mad_libs(content))
