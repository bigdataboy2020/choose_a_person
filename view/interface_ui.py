from tkinter import ttk, Tk, LabelFrame, Frame, Button, Label, Scrollbar, RIGHT, mainloop, StringVar

class UI(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('抽人软件 联系QQ：876545500')
        self.root.resizable(0,0) #阻止GUI的大小调整

        self.labelName = StringVar()  # 选取的名字
        self.labelName.set('未初始化！！！')

        self.functionFrame = LabelFrame(self.root, text='操作区')
        self.functionFrame.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

        self.show = LabelFrame(self.root)
        self.show.grid(row=0, column=1, padx=5)
        self.treeScroll = Frame(self.root)
        self.treeScroll.grid(row=1, column=1, padx=0, pady=0)

        self.btn_initialize = Button(self.functionFrame, text='初始化', command=self.initialize)
        self.btn_initialize.grid(row=1, column=0, padx=5, pady=10)
        self.btn_girl = Button(self.functionFrame, text='选女生', command=self.chooseGirl)
        self.btn_girl.grid(row=2, column=0, padx=5, pady=10)
        self.btn_girl['state'] = 'disabled'
        self.btn_boy = Button(self.functionFrame, text='选男生', command=self.chooseBoy)
        self.btn_boy.grid(row=3, column=0, padx=5, pady=10)
        self.btn_boy['state'] = 'disabled'
        self.btn_choose = Button(self.functionFrame, text='随机选择', command=self.choose)
        self.btn_choose.grid(row=4, column=0, padx=5, pady=10)
        self.btn_choose['state'] = 'disabled'

        Label(self.show, textvariable=self.labelName, height=3, width=18, font=("黑体", 18, 'bold'), anchor='center').pack(padx=5,
                                                                                                               pady=5)
        self.scroll = Scrollbar(self.treeScroll)
        self.scroll.pack(side=RIGHT, fill='y')
        self.tree = ttk.Treeview(self.treeScroll, column=('num', 'name'), selectmode='browse', height=5,
                            yscrollcommand=self.scroll.set,
                            show='headings')
        self.tree.pack()
        self.scroll.config(command=self.tree.yview)
        head_width = [('num', '50'), ('name', '184')]
        for head_index, width in head_width:
            self.tree.column(head_index, width=width, anchor='center')  # 通过 索引 设置列宽 文字居中

        head_text = [('num', 'num'), ('name', 'name')]
        for head_index, head_name in head_text:
            self.tree.heading(head_index, text=head_name)  # 通过 索引 表头
        mainloop()

    # 初始化
    def initialize(self):
        pass

    # 选择女生
    def chooseGirl(self):
        pass

    # 选择男生
    def chooseBoy(self):
        pass

    # 随机选择
    def choose(self):
        pass

if __name__ == '__main__':
    ui = UI()