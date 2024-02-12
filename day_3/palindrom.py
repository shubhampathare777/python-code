a = input("Enter the word or letter to check palindrome: ")
copy_a = list(a)
copy_a.reverse()

if "".join(copy_a) == a:
    print("Palindrome")
else:
    print("Not a palindrome")
