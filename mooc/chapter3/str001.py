# 字符串操作函数

# 字符串截取
s = "python 语言 程序设计"
s1 = s[0:]
s2 = s[:len(s)]
s3 = s[1:3]
s4 = s.split(" ")
s5 = s4 * 2
print("s1=" + s1)
print("s2=" + s2)
print("s3=" + s3)
print("s4=" + str(s4)) # s4=['python', '语言', '程序设计']
print("s5=" + str(s5)) # s5=['python', '语言', '程序设计', 'python', '语言', '程序设计']

b = "python \v" * 3
print("b=" + b)

f = 3.22
# print("f="+f) 错误,无法将float类型直接与字符串拼接
print("f=" + str(f))  # 正确

##凯撒密码
source = "abcdefghijklmnopqrstuvwxyz"
for p in source:
    if ord("a") <= ord(p) <= ord("z"):
        print(chr(ord("a") + (ord(p) - ord("a") + 3) % 26), end="")
    else:
        print(p, end='')
print("\n")
# 字符串常用方法
source1 = source.upper()
source2 = source1.split(" ")
source3 = source1.join(" ")
print("source1=" + source1)
print("source1 is number:" + str(source1.isnumeric()))
print("source2 split=" + str(source2))
print("source3 join=" + str(source3))
# 在Python中，字符串比较是基于字典序（lexicographical order）进行的，
# 这意味着字符串中的每个字符会被逐个比较，比较依据是字符的Unicode码点值
print(str('abcd' < 'ad'))  # True
# 在Python中，当比较两个字符串时，如 'abc' 和 'abcd'，比较是基于字典序的。
# 如果前缀完全相同，那么较短的字符串被认为是较小的。这是因为较长的字符串会在比较完所有相同前缀后的下一个字符时，
# 由于短字符串在那个位置上实际上是“空字符”（或者说，相当于字符串结束），而被视作较大。
print(str('abc' < 'abcd'))  # false
# 在Python中，当你比较一个空字符串 '' 和一个非空字符串，比如 'a'，比较的规则基于字符串的长度和内容。
# 由于空字符串没有任何字符，而 'a' 有至少一个字符，因此在字典序比较中，空字符串被视为小于任何非空字符串。
# 这符合字典序比较的基本原则，即较短的字符串（在此处为空字符串）在字典序上小于任何非空字符串。
print(str('' < 'a'))  # True
# 在Python中，字符串的比较是基于Unicode码点值的字典序比较。
# 大写字母和小写字母在Unicode中的码点值是不同的，大写字母的码点值小于小写字母的码点值。
print(str('Hello' > 'hello'))  # False


# format 格式化输出
print("{}{}{}".format(s,s1,s2))