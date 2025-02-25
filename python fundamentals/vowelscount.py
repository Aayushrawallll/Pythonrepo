a="Hello World I Am Here"
vowels_count={}
vowels="aeiouAEIOU"
for char in a:
    if char in vowels:
        if char in vowels_count:
            vowels_count[char]+=1
        else:
            vowels_count[char]=1    

print(vowels_count)            