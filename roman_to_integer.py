def romanToInt(string):

    hash_set= {'I':1,
              'IV':4,
              'V':5,
              'XI':9,
              'X':10,
              'L':50,
              'C':100,
              'CD':400,
              'D':500,
              'CM':900,
              'M':1000 }
   
    convert = list(string)

    result = 0
    for char in convert:
        num = hash_set[char]
        result +=num
    return result


string = 'LXVI'
print(romanToInt(string))