s = set("aeiou")
l = [ "aeiou" , "getatier", "getaeiou"]
newl  = [ele for ele in l if s.issubset(ele) ]
print(newl)
