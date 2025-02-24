num_dict = {"a":1,"b":2,"c":3,"d":4}
for zimu,count in num_dict.items():
    # zimu_input = str(input("请输入你想查询的字母："))
    # print(num_dict[zimu_input])
    print(f"{zimu}:{count}")

def data(height,weight):
    BMI = weight / ( height ** 2)
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI <= 25:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    return BMI,category


while True :
    try:
        height = 1
        weight = 1
        height,weight = map(float,input("请输入您的身高与体重：").split())
        BMI,category = data(height,weight)
        print(f"你当前的BMI指数为：{BMI:.2f}，属于{category}水平")
        command = input("输入'q'退出，按回车继续：").strip().lower()
        if command == 'q' :
            break
        elif command != 'q' :
            break
    except ValueError:
        print("输入错误，你这个蠢猪，请重新输入：")
        


class Student:
    def __init__(self,student_name,student_sid):
        self.name = student_name
        self.sid = student_sid
        self.grade = {"数学":0, "英语":0, "语文":0}

    def set_grade(self,grades):
         for course, grade in grades.items():
            if course in self.grade:
                self.grade[course] = grade
    def print_grade(self):
        for course in self.grade:
            print(self.grade[course])
zhu = Student("朱",124680)
zhu.set_grade({"数学":95, "语文":8,"英语":7})
zhu.print_grade()
        
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def print_info(self):
        print(f"姓名：{self.name},工号：{self.id}")
class FullTimeEmployee(Employee):
    def __init__(self, name, id,salary):
        super().__init__(name, id)
        self.monthly_salary = salary
    def calculate_monthly_pay(self):
        print(f"您的月薪为： {self.monthly_salary}")
class PartTimeEmployee(Employee):
    def __init__(self, name, id,salary,days,):
        super().__init__(name, id)
        self.daily_salary = salary
        self.work_days = days
    def calculate_monthly_pay(self):
        monthly_salary = self.daily_salary * self.work_days
        print(f"您的月薪为：{monthly_salary}")

zhu = FullTimeEmployee("zhu",124680,80000)
zhu.print_info()
zhu.calculate_monthly_pay()
xiaozhu = PartTimeEmployee("xiaozhu",86421,2000,30)
xiaozhu.print_info()
xiaozhu.calculate_monthly_pay()

#python06
f = open("C:/Users/Administrator/Desktop/新建文本文档.txt","r",encoding="utf-8")
print(f.read())

#python07
with open("./poem.txt","w",encoding="utf-8") as f:
    f.write("我欲乘风归去，\n")
    f.write("又恐琼楼玉宇，\n")
    f.write("高处不胜寒。\n")
with open("./poem.txt","a",encoding="utf-8") as f:
    f.write("起舞弄清影，\n")
    f.write("何似在人间。\n")
f = open("./poem.txt","r",encoding="utf-8")