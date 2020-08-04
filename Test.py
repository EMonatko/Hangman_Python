Path = 'Words.txt'
file = open(Path)
count = 0
for line in file:
    word = line.strip().split(" ")
file.close()
bad_value = False
#word = list(word)
while not bad_value:
    index = input(f'Please input a number between 1 - {len(word)} :')
    bad_value = index.isdigit()

index = int(index) % int(len(word))
print(index)
print(word[index])
