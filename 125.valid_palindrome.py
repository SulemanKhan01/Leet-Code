def isPalindrome(string):

    # Spaces Removed
    rs_str = string.replace(" " , "")
    str = rs_str.lower()
    if len(str) == 1:
        return True
    for i in range(len(str)//2):
        if str[i] != str[-i-1]:
            return False
    return True




print(isPalindrome("Was it a car or a cat I saw"))
print(isPalindrome("Was it a car or a cat I saw on the road"))
