valid = "!@$%^*(){}[];\'\",.<>/?-=_`~ "

answer = str(input("请输入进行异或构造的字符串："))

tmp1, tmp2 = '', ''
for c in answer:
  for i in valid:
    for j in valid:
      if (ord(i) ^ ord(j) == ord(c)):
        tmp1 += i
        tmp2 += j
        break
    else:
      continue
    break
print("tmp1为:",tmp1)
print("tmp2为:",tmp2)