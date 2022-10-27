def searcher():
    print("Reading the File wait for a while")
    with open("sample.txt") as file:
        names = file.read()
        print("File Readed !!")
    
    while(True):
        text = (yield)
        if text in names:
            print("Your Name is Found in the File.")
        else:
            print("Your Name is not Found in the File.")

name = input("Enter the Name you want to Search - ")
search = searcher()
print("Search Started")
next(search)
search.send(name)

#basically code ko adha chlane ke kaam ata h