def add_func(*args):
    sum=0
    for arg in args:
        sum=sum+arg
    return sum


def factorial_func(num):
    fac=1
    for i in range(1,num+1):
        fac*=i
    return fac


def tempconv_func(temp, unit):
    if unit.lower() =='c':
        return (temp - 32) * 5/9
    else:
        return (temp * 9/5) + 32


# Remove all odd numbers
# Double every remaining number
# Sum all the modified numbers

def listmanipulation_func(list):
    return sum([list[i]*2 for i in range(len(list)) if i%2==0])


def pyramid_func(num):
    for i in range(1,num+1):
        print(" "*(num-i), end='')
        print("#"*i)


def wordfreq_dic(string):
    dict={}
    lis=list(string)
    for alpha in lis:
        if alpha.isalpha():
            dict[alpha]=dict.get(alpha,0)+1

    return dict

#print(wordfreq_dic("Hello World! 123")) #Edit to set each function
