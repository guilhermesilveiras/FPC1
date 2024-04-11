# 2 lacos
# str = input()
# for i in range(len(str)+1):
#     print(str[0:i].strip())
#     for j in range(len(str), 0, -1):
#         print(str[i:j].strip())


# #1 laco
# str = input()
# x = len(str)
# i = 0
# n = len(str[0])
# while i < len(str):
#     print(str[n:i+1])
#     n += 1
#     i += 1

str = "heloisa"
x = len(str) 
t = 0 
while t != (len(str)+ 1): 
    print(str[t])
    print(str[t:x + 1])
    x -= 1 
    if x == 0: 
        x = len(str)
        t += 1