"""
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
duplicate.sort(reverse=True)
print(Remove(duplicate))
"""
"""
def para_function(**kwargs):
    return kwargs['salary'],kwargs['Hero']

print(para_function(Hero='Rajni',salary=300000))
"""
"""
n=int(input())
a=hex(n).replace("0x","").upper()
print(a)
"""

def sumVowel(string):
    a=input()
    n = len(string(a))
    sum = 0
    string = string.lower()
    for i in range(0, n):
        s = string[i]
    if (s=="a" or s == "e" or s == "i" or s == "o" or s == "u"):
        sum += ((n - i) * (i + 1))
        return sum
