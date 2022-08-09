# writing to file
file1 = open('data/full.json', 'w')

# Using readlines()
file2 = open('data/comments.json', 'r')
lines = file2.readlines()

for i in lines:
    file1.write(i[:-1]+","+"\n")
