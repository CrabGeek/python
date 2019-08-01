from Student import Student
def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('haha', 15)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()
    stu1.score  = 10

    stu2 = Student.name = 'haha'



if __name__ == '__main__':
    main()