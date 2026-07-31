# WAP to input any alphabet and check whether it is vowel or consonant.

char = input("Enter a alphabet = ")

if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
    print(f"{char} is Vowel")

else:
    print(f"{char} is Consonant")