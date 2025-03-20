a="Hello World"
char_count={}
for char in a:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
print(char_count)            