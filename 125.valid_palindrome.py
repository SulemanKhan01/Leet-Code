def isPalindrome(string):

    if len(string) == 1:
        return True

    # Spaces Removed
    rs_str = string.replace(" " , "")
    str = rs_str.lower()

    new_str = ""

    for char in str:
        if char.isalnum():
            new_str += char
    
    for i in range(len(new_str)):
        if new_str[i] != new_str[-i-1]:
            return False
    return True




print(isPalindrome("Was it a car or a cat I saw"))
print(isPalindrome("Was it a car or a cat I saw?"))
print(isPalindrome("0p"))