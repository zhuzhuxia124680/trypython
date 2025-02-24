total = 0
count = 0
user_input = input("请输入用于求平均值的数（如您已输入完成，请输入q）：")
while user_input != "q" :
   num = float(user_input)
   total += num
   count += 1
   user_input = input("请输入用于求平均值的数（如您已输入完成，请输入q）：")
if count == 0 :
   print("您输入的数字求平均值为0")
else :
   result = total / count
   print("您输入的数字求平均值为" + str(result) + "。")
