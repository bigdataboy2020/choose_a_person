from view import UI
from tkinter import END, messagebox
import random
import xlrd


class Main(UI):
    index = 0  # 表格计数

    i = 1  # 初始化状态 0： 初始化成功，1 未初始化

    def __init__(self):
        super().__init__()

    def initialize(self):
        """
        初始化：重载数据，设置按钮为可用状态，清空表格
        :return:
        """
        self.boyList = list()  # 男生列表
        self.girlList = list()  # 女生列表
        [self.tree.delete(item) for item in self.tree.get_children()] # 初始化清空表格
        # 加载数据
        try:
            table = xlrd.open_workbook("./data.xlsx").sheet_by_index(0)
        except FileNotFoundError:
            self.labelName.set('初始化失败 ！！！')
            self.btn_girl['state'],self.btn_boy['state'],self.btn_choose['state'] = 'disabled','disabled','disabled'
            messagebox.showerror(title="错误提示",message=f"没有发现数据文件，请检查数据文件是否存在，或者名称是否是 “data.xlsx”")
        else:
            for r in range(table.nrows):
                v = table.row(r)
                if v[1].value == "男":
                    self.boyList.append(v[0].value) # 男生列表
                elif v[1].value == "女":
                    self.girlList.append(v[0].value) # 女生列表

            print(self.boyList)
            print(self.girlList)
            self.i = 0
            self.labelName.set('初始化成功 ！！！')
            self.btn_girl['state'], self.btn_boy['state'], self.btn_choose['state']= 'normal', 'normal', 'normal'

    def chooseGirl(self):
        girlNum = len(self.girlList) - 1  # 获取女生列表人数
        if girlNum == -1:
            self.labelName.set('女生抽完了,歇口气！')
            self.btn_girl['state'] = 'disabled'
            if len(self.boyList) == 0:
                self.btn_choose['state'] = 'disabled'
                self.labelName.set('没人可抽了,歇口气！')
        else:
            num = random.randint(0, girlNum)  # 生成随机数
            name = self.girlList[int(num)]  # 取出名字
            self.labelName.set(name)
            self.index += 1
            self.tree.insert("", END, values=(self.index, name))  # 加入表格
            self.girlList.pop(num)  # 删除已取出女生名字

    def chooseBoy(self):
        boyNum = len(self.boyList) - 1  # 获取男生列表人数
        if boyNum == -1:
            self.labelName.set('男生抽完了,歇口气！')
            self.btn_boy['state'] = 'disabled'
            if len(self.girlList) == 0:
                self.btn_choose['state'] = 'disabled'
                self.labelName.set('没人可抽了,歇口气！')

        else:
            num = random.randint(0, boyNum)  # 生成随机数
            name = self.boyList[num]  # 取出名字
            self.labelName.set(name)
            self.index += 1
            self.tree.insert("", END, values=(self.index, name))
            self.boyList.pop(num)

    def choose(self):
        peopleList = self.girlList + self.boyList
        random.shuffle(peopleList)
        peopleNum = len(peopleList) - 1  # 获取所剩人数
        if peopleNum == -1:
            self.labelName.set('没人可抽了,歇口气！')
            self.btn_girl['state'],self.btn_boy['state'],self.btn_choose['state'] = 'disabled','disabled','disabled'
        else:
            num = random.randint(0, peopleNum)  # 生成随机数
            name = peopleList[num]  # 取出名字
            self.labelName.set(name)
            self.index += 1
            self.tree.insert("", END, values=(self.index, name))
            # 删除 取出了的 名字
            try:
                self.girlList.remove(name)
                print(self.girlList)
            except ValueError as e:
                self.boyList.remove(name)
                print(self.boyList)

if __name__ == '__main__':
    main = Main()
