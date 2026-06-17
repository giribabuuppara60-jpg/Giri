str1 = "HELLO"
str2 = "BYE"

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagram")
else:
    print("Not Anagram")