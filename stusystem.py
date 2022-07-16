#Engineer: HuMu
#CreatTime: 2022/7/14 13:50
import os.path
stufile = 'students.txt'

def menu():
    print('学生信息管理系统'.center(57, '*'))
    print('功能菜单'.center(60, '-'))
    # print(' '.center(22), end='')
    print(' '.center(18), '1.录入学生信息(清除原有信息)')
    print(' '.center(18), '2.查找学生信息')
    print(' '.center(18), '3.删除学生信息')
    print(' '.center(18), '4.修改学生信息(ID不存在则自动添加)')
    print(' '.center(18), '5.对学生信息进行排序')
    print(' '.center(18), '6.统计学生总人数')
    print(' '.center(18), '7.显示所有学生信息')
    print(' '.center(18), '0.退出系统')
    print(''.center(63, '-'))

def save(lst_dir): # 将学生信息保存到文件中
    with open('students.txt', 'w', encoding='utf-8') as file:
        for i in lst_dir:
            # file.write('id：' + str(i['id']) + '\t')
            # file.write('name：' + str(i['姓名']) + '\t')
            # file.write('C++成绩：' + str(i['C++成绩']) + '\t')
            # file.write('Python成绩：' + str(i['Python成绩']) + '\t')
            # file.write('Java成绩：' + str(i['Java成绩']) + '\t')
            # file.write('\n')
            file.write(str(i) + '\n')

def insert(): # 录入学生信息
    stu = []
    while True:
        # 输入学生的信息
        id_num = input('请输入学生学号：')
        while not id_num:
            print('输入错误，请重新输入学生学号：')
            id_num = input('请输入学生学号：')
        # 防止出现学号相同的情况
        id_exist = False
        for i in stu:
            if i['id']==id_num:
                id_exist = True
        if id_exist:
            print('该ID的学生信息已录入，请输入其他ID')
            continue
        name = input('请输入学生姓名：')
        while not name:
            print('输入错误，请重新输入学生姓名')
            name = input('请输入学生姓名：')
        score1 = input('请输入C++成绩：')
        while not score1.isdecimal():
            score1 = input('输入错误，请重新输入C++成绩：')
        score1 = int(score1)
        score2 = input('请输入Python成绩：')
        while not score2.isdecimal():
            score2 = input('输入错误，请重新输入Python成绩：')
        score2 = int(score2)
        score3 = input('请输入Java成绩：')
        while not score3.isdecimal():
            score3 = input('输入错误，请重新输入Java成绩：')
        score3 = int(score3)

        # 将学生的信息放到字典中
        stu.append({'id':id_num, '姓名':name, 'C++成绩':score1, 'Python成绩':score2, 'Java成绩':score3})

        # 判断是否继续录入信息
        judge = input('是否继续录入信息？y/n ')
        while judge!='y' and judge!='Y' and judge!='n' and judge!='N':
            judge = input('是否继续录入信息？y/n ')
        if judge=='n' or judge=='N':
            break
        else:
            continue

    # 保存学生信息到文本文件当中
    save(stu)
    print('学生信息录入完毕！！！')

def serach(): # 查找学生信息
    if os.path.exists(stufile):
        while True:
            # 读取学生信息，并将其转化成字典列表
            stu_dir = []
            with open(stufile, 'r', encoding='utf-8') as rfile:
                stu_str = rfile.readlines()
            for i in stu_str:
                stu_dir.append(eval(i))

            # 用户输入查找模式
            ser_mode = input('按ID查找请输入1，按姓名查找请输入2：')
            while ser_mode!='1' and ser_mode!='2':
                ser_mode = input('输入错误！按ID查找请输入1，按姓名查找请输入2：')

            # 用户输入查找内容
            if ser_mode=='1':
                ser_info = input('请输入要查找的ID：')
                while not ser_info:
                    ser_info = input('输入无效！请输入要查找的ID：')
            else:
                ser_info = input('请输入要查找的姓名：')
                while not ser_info:
                    ser_info = input('输入无效！请输入要查找的姓名：')

            # 查找信息
            stu_res = [] # 查找的结果
            find_flag = False
            if ser_mode=='1':
                for i in stu_dir:
                    if i['id']==ser_info:
                        stu_res.append(i)
                        find_flag = True
            else:
                for i in stu_dir:
                    if i['姓名']==ser_info:
                        stu_res.append(i)
                        find_flag = True
            if not find_flag:
                print('您输入的信息未查询到！')
            else:
                print('您输入的信息已查到!')

            # 展示查询到的信息
            format_title = '{:^6}\t{:^6}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'
            print(format_title.format('ID', '姓名', 'C++成绩', 'Python成绩', 'Java成绩', '总成绩'))
            for i in stu_res:
                print(format_title.format(i['id'], i['姓名'],
                      i['C++成绩'], i['Python成绩'], i['Java成绩'],
                      i['C++成绩']+i['Python成绩']+i['Java成绩']))

            # 询问是否继续
            con_flag = input('是否继续查询？y/n ')
            while con_flag!='y' and con_flag!='Y' and con_flag!='n' and con_flag!='N':
                con_flag = input('输入错误！是否继续查询？y/n ')
            if con_flag=='y' or con_flag=='Y':
                continue
            else:
                break
    else:
        print('还未保存过学生信息！！')
        return

def delete(): # 删除学生信息
    while True:
        id_num = input('请输入要删除的学生的ID：')
        while not id_num:
            print('ID输入格式错误，请重新输入：')
            id_num = input('请输入要删除的学生的ID：')

        # 读取文件中的内容
        if os.path.exists(stufile):
            with open(stufile, 'r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()
        else:
            print('暂未保存过数据！！')
            return

        # 将不删除的信息重新覆盖写入文件
        find_id = False
        if student_old:
            with open(stufile, 'w', encoding='utf-8') as wfile:
                for i in student_old:
                    sing_stu = eval(i)
                    if sing_stu['id']!=id_num:
                        wfile.write(i) # 将字符串转换成字典
                    else:
                        find_id = True
        else:
            print('学生信息为空！')
            return

        # 显示是否删除
        if find_id:
            print('ID为{0}的学生信息已删除！'.format(id_num))
        else:
            print('未找到ID为{0}的学生信息！'.format(id_num))

        # 重新显示所有学生信息
        show()

        # 询问是否要继续删除
        conti_del = input('是否继续删除学生信息？y/n ')
        while conti_del!='y' and conti_del!='Y' and conti_del!='N' and conti_del!='n':
            conti_del = input('输入错误，是否继续删除学生信息？y/n ')
        if conti_del=='y' or conti_del=='Y':
            continue
        else:
            break
    return

def modify(): # 修改学生信息
    stu_dir = []
    while True:
        # 判断文件是否存在
        if os.path.exists(stufile):
            # 读取文件全部信息
            with open(stufile, 'r', encoding='utf-8') as rfile:
                stu_lst = rfile.readlines()
            for i in stu_lst:  # 将列表内的字符串元素转化成字典元素
                stu_dir.append(eval(i))

            # 用户输入学生信息
            id_num = input('请输入学生学号：')
            while not id_num:
                print('输入错误，请重新输入学生学号：')
                id_num = input('请输入学生学号：')
            name = input('请输入学生姓名：')
            while not name:
                print('输入错误，请重新输入学生姓名')
                name = input('请输入学生姓名：')
            score1 = input('请输入C++成绩：')
            while not score1.isdecimal():
                score1 = input('输入错误，请重新输入C++成绩：')
            score1 = int(score1)
            score2 = input('请输入Python成绩：')
            while not score2.isdecimal():
                score2 = input('输入错误，请重新输入Python成绩：')
            score2 = int(score2)
            score3 = input('请输入Java成绩：')
            while not score3.isdecimal():
                score3 = input('输入错误，请重新输入Java成绩：')
            score3 = int(score3)

            # 判断学生ID是否存在，不存在就添加
            id_exist = False
            for i in stu_dir:
                if i['id']==id_num:
                    id_exist = True
                    stu_dir.remove(i)
                    stu_dir.append({'id':id_num, '姓名':name, 'C++成绩':score1, 'Python成绩':score2, 'Java成绩':score3})
            if not id_exist:
                stu_dir.append({'id':id_num, '姓名':name, 'C++成绩':score1, 'Python成绩':score2, 'Java成绩':score3})

            # 保存学生信息
            save(stu_dir)

            # 显示学生信息
            show()

            # 询问是否继续
            con_judge = input('是否继续修改学生信息？y/n ')
            while con_judge!='Y' and con_judge!='y' and con_judge!='N' and con_judge!='n':
                con_judge = input('输入错误！是否继续修改学生信息？y/n ')
            if con_judge=='Y' or con_judge=='y':
                continue
            else:
                break # 当然return也行
        else:
            print('学生信息文件不存在！')
            break

def sort():   # 排序
    show()
    if os.path.exists(stufile):
        while True:
            # 读取全部信息并转换成字典列表
            stu_lst = []
            with open(stufile, 'r', encoding='utf-8') as rfile:
                stu_lst = rfile.readlines()
            if not stu_lst:
                print('还未录入学生信息！！')
                return
            else:
                stu_dir = []
                for i in stu_lst:
                    stu_dir.append(eval(i))

            # 计算每个学生的总成绩
            stu_dir_whole = []
            for i in stu_dir:
                i['总成绩']=i['C++成绩'] + i['Python成绩'] + i['Java成绩']
                stu_dir_whole.append(i)

            # 用户选择排序类型及排序方式
            sort_tip = '排序依据提示'.center(12,'-') + \
                       '\n1.按ID排序\n' \
                       '2.按姓名排序\n' \
                       '3.按C++成绩排序\n' \
                       '4.按Python成绩排序\n' \
                       '5.按Java成绩排序\n' \
                       '6.按总成绩排序\n' + \
                       ''.center(16, '-') + \
                       '\n请输入排序依据：'
            sort_col = input(sort_tip)
            while sort_col not in['1','2','3','4','5','6']:
                  sort_col = input('输入错误！\n' + sort_tip)
            sort_mode = input('升序排序请输入1，降序排序请输入2：')
            while sort_mode!='1' and sort_mode!='2':
                sort_mode = input('输入错误！升序排序请输入1，降序排序请输入2：')

            # 进行排序操作
            if sort_col=='1':
                stu_dir_whole.sort(key=lambda x: x['id'], reverse=sort_mode=='2')
            elif sort_col=='2':
                stu_dir_whole.sort(key=lambda x: x['姓名'], reverse=sort_mode=='2')
            elif sort_col=='3':
                stu_dir_whole.sort(key=lambda x: x['C++成绩'], reverse=sort_mode == '2')
            elif sort_col=='4':
                stu_dir_whole.sort(key=lambda x: x['Python成绩'], reverse=sort_mode=='2')
            elif sort_col=='5':
                stu_dir_whole.sort(key=lambda x: x['Java成绩'], reverse=sort_mode=='2')
            elif sort_col=='6':
                stu_dir_whole.sort(key=lambda x: x['总成绩'], reverse=sort_mode=='2')
            else:
                print('出现了未能预知的错误！重启吧')
                return

            # 保存信息并展示
            save(stu_dir_whole)
            print('排序结果为：')
            show()

            # 询问是否继续排序
            con_flag = input('是否继续排序？y/n ')
            while con_flag!='n' and con_flag!='N' and con_flag!='y' and con_flag!='Y':
                con_flag = input('输入错误！是否继续排序？y/n ')
            if con_flag=='y' or con_flag=='Y':
                continue
            else:
                return
    else:
        print('还未录入学生信息！！')
        return

def total():  # 统计学生总人数
    if os.path.exists(stufile):
        # 读取学生信息
        with open(stufile, 'r', encoding='utf-8') as rfile:
            stu_lst = rfile.readlines()

        # 输出统计结果
        stu_num = len(stu_lst)
        if stu_num==0:
            print('还未录入学生信息！！')
        else:
            print('学生总人数为 {}'.format(stu_num))
    else:
        print('还未录入学生信息！！')
        return

def show():   # 显示所有学生信息
    if os.path.exists(stufile):
        # 读取所有信息
        stu_lst = []
        with open(stufile, 'r', encoding='utf-8') as rfile:
            stu_lst = rfile.readlines()

        # 将读取的信息转化成字典列表并打印显示
        if stu_lst:
            stu_dir = []
            for i in stu_lst:
                stu_dir.append(eval(i))

            print('以下为所有的学生信息：')
            format_title = '{:^6}\t{:^6}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'
            print(format_title.format('ID', '姓名', 'C++成绩', 'Python成绩', 'Java成绩', '总成绩'))
            for i in stu_dir:
                print(format_title.format(i['id'],
                                          i['姓名'],
                                          i['C++成绩'],
                                          i['Python成绩'],
                                          i['Java成绩'],
                                          i['C++成绩'] + i['Python成绩'] + i['Java成绩']))
            print('所有学生信息显示完毕！！')
            return
        else:
            print('还未录入学生信息！！')
            return
    else:
        print('还未保存学生信息！！')
        return

def main():
    while True:
        menu()
        while True:
            choice = input('请选择功能序号：')
            if choice.isdecimal():
                choice = int(choice)
                if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
                    break
                else:
                    continue
            else:
                continue
        if choice == 0:
            answer = input('您确定要退出系统吗？y/n ')
            if answer=='y' or answer=='Y':
                print('感谢您的使用！！')
                break
            else:
                continue
        elif choice == 1:
            insert() # 录入学生信息
        elif choice == 2:
            serach() # 查找学生信息
        elif choice == 3:
            delete() # 删除学生信息
        elif choice == 4:
            modify() # 修改学生信息
        elif choice == 5:
            sort()   # 排序
        elif choice == 6:
            total()  # 统计学生总人数
        elif choice == 7:
            show()   # 显示所有学生信息

if __name__ == '__main__':
    main()

