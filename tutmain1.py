def printhar(str):
    print(f"My name is {str}")

def add(num1 , num2):
    return num1+num2+5


#adding main in the python file so that if file import this file than my function inside main will not get execute
if __name__ == '__main__':
    o=add(4,5)
    print(f"This is the total sum {o}")