f1 = open("sample.txt")

try: 
    f= open("abc.txt")
except Exception as e:
    print(e)


else:
    print("This will run in case Exception in not running")

finally:
    print("this will run in anyways....")
    f1.close()