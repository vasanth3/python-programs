def isIsomorphic (s, t):
    dict_s = {}
    dict_t = {}

    for i, value in enumerate(s):
        dict_s[value] = dict_s.get(value, []) + [i]


    for j,value in enumerate(t):
        dict_t[value] = dict_t.get(value, []) + [j]

    if sorted(dict_s.values()) == sorted(dict_t.values()):
        return True
    else:
        return False

print(isIsomorphic("egg", "add"));
print(isIsomorphic("bar", "foo"));
print(isIsomorphic("paper", "title"));
print(isIsomorphic("fry", "sky"));
print(isIsomorphic("apples", "apple"));

            


                            
