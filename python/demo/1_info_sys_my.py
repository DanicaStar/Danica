list_teacher=[
    {"tea_name":"tea1","grade":"八年级","_class":"2班","subject":"语文"},
    {"tea_name":"tea2","grade":"七年级","_class":"1班","subject":"数学"},
    {"tea_name":"tea3","grade":"九年级","_class":"4班","subject":"英语"},
    {"tea_name":"tea4","grade":"八年级","_class":"3班","subject":"物理"},
]
list_student=[
    {"stu_name":"stu1","grade": "八年级", "age":13,"_class":"2班"},
    {"stu_name":"stu2","grade": "七年级", "age":12,"_class":"1班"},
    {"stu_name":"stu3","grade": "九年级", "age":13,"_class":"2班"},
    {"stu_name":"stu4","grade": "八年级", "age":13,"_class":"3班"},
]

class  Grade:
    def __init__(self,grade):
        self.grade = grade
    def __str__(self):
        return grade

class Class:
    def __init__(self,_class):
        self._class=_class
    def __str__(self):
        return grade
class Teacher(Grade,Class):
    def __init__(self, grade, _class, subject,tea_name):
        Grade.__init__(self,grade)
        Class.__init__(self,_class)
        self.subject=subject
        self.tea_name=tea_name
    def run(self):
        print("{}老师是{}{}的{}老师".format(self.tea_name,self.grade,self._class,self.subject))

class Student(Grade, Class):
    def __init__(self,stu_name,grade,age,_class):
        Grade.__init__(self,grade)
        Class.__init__(self,_class)
        self.stu_name=stu_name
        self.age=age
    def run(self):
        print("{}同学今年{}岁，在{}{}".format(self.stu_name, self.age,self.grade,self._class))

while True:
    print("*" * 10 + "信息类型" + "*" * 10)
    print("1、学生信息\n2、老师信息\n3、退出")
    answer = int(input("请输入想要查询的信息类型对应的数字："))
    if answer==1:
        while True:
            print("请输入学生姓名：",end='')
            for student_info in list_student:
                name = input()
                if name==student_info["stu_name"]:
                    grade=student_info["grade"]
                    age=student_info['age']
                    _class=student_info['_class']
                    stu=Grade(grade)
                    stu=Class(_class)
                    stu=Student(name,grade,age,_class)
                    stu.run()
                else:
                    print("该学生姓名不存在,",end='')
                break
        break



    elif answer==2:
        while True:
            print("请输入老师姓名：", end='')
            for teacher_info in list_teacher:
                name = input()
                if name == teacher_info['tea_name']:
                    grade = teacher_info["grade"]
                    _class = teacher_info['_class']
                    subject = teacher_info['subject']
                    tea=Teacher(name,grade,_class,subject)
                    tea.run()
                else:
                    print("该老师姓名不存在,",end='')
                break
        break
    elif answer == 3:
        print("欢迎下次使用系统")
        break




