# Write a Program to Count Vowels


# input_string = "hello, world!"
input_string = input("Enter a sentence: ")

vowels = "aeiou"

vowels_count = 0

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count + 1

print(vowels_count)
