f = open("C:\\Users\\MICLAB\\Desktop\\demo.txt","r")
data = f.read()
lw = data.split()
print("Total number of words in a given file is :",len(lw))
print("Available words are :",lw)
