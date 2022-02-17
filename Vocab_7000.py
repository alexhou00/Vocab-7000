from tkinter import filedialog, Tk, OptionMenu, StringVar, Label, Frame, Button, Scale, LabelFrame, Text, Radiobutton, messagebox, Toplevel
from random import randint, shuffle
from webbrowser import open as bopen

def start():
    global lvltext2, dictionary, lvlscrollbar, explanation, opts, nextQ, showKK, showKK_txt, subframes
    global records, modevar, qtvar, correctcount, MODES, QTYPE, word, func8, funcg, clearRecord, optframe
    
    root = Tk()
    root.title("高中英文7000單字練習系統 - Windows版")
    root.resizable(False, False)
    root.config(bg=BGCOLOR)
    #root.maxsize(WINWIDTH, 1000)
    #root.minsize(WINWIDTH, 0)
    root.wm_iconbitmap('p/logo.ico')
    
    title = Label(root, text="高中英文7000單字練習系統", bg=BGCOLOR, font=("微軟正黑體", 16))
    title.pack(padx=10, pady=10)
    mainFrame = Frame(root, bg=BGCOLOR)
    mainFrame.pack()
    subframes = [Frame(mainFrame, bg=BGCOLOR) for x in range(3)]
    for i in range(3): subframes[i].grid(row=0, column=i)

    lblframe = LabelFrame(subframes[0], text='答題紀錄', bg=BGCOLOR, padx=10)
    lblframe.pack(padx=20, pady=0)
    records = Text(lblframe, bg=BGCOLOR, width=14, wrap='none', state='disabled')
    records.pack()
    clearRecord = Button(lblframe, text='清空答題紀錄', bg=BGCOLOR, width=14,
                         activebackground=OYELLOW, relief='groove', command=clearRecords)
    clearRecord.pack()
    expRecord = Button(lblframe, text='匯出答題紀錄', bg=BGCOLOR, width=14,
                         activebackground=OYELLOW, relief='groove', command=fileSave)
    expRecord.pack()

    funcframe = LabelFrame(subframes[2], text='功能表區', bg=BGCOLOR, padx=10)
    funcframe.pack(padx=20, pady=0)
    

    modevar = StringVar()
    modevar.set(MODES[0])
    qtvar = StringVar()
    qtvar.set(QTYPE[1])
    
    framemode = Frame(funcframe, bg=BGCOLOR)
    framemode.pack(pady=5)
    frametype = Frame(funcframe, bg=BGCOLOR)
    frametype.pack(pady=(5,10))
    Label(framemode, text="模式", bg=BGCOLOR).grid(row=0, column=0, rowspan=2, padx=3)
    Label(frametype, text="題型", bg=BGCOLOR).grid(row=2, column=0, rowspan=3, padx=3)
    
    for i, mode in enumerate(MODES):
        b = Radiobutton(framemode, text=mode, variable=modevar, value=mode, relief='groove',
                        bg=BGCOLOR, indicatoron=0, selectcolor=DRKYLLW, activebackground=OYELLOW)
        b.grid(row=i, column=1)
        
    for j, qt in enumerate(QTYPE):
        b = Radiobutton(frametype, text=qt, variable=qtvar, value=qt, relief='groove', command=lambda:createOpts(1), 
                        bg=BGCOLOR, indicatoron=0, selectcolor=DRKYLLW, activebackground=OYELLOW)
        b.grid(row=j+2, column=1)
    
    #wtf are those variable names
    func7 = Button(funcframe, text='練習不熟的單字', height=2, bg=DRKYLLW, width=14, activebackground=DRKYLLW,
                   relief='groove', highlightbackground=DRKYLLW)
    func7.pack()
    func9 = Button(funcframe, text='編輯不熟的單字', bg=OYELLOW, width=14, activebackground=DRKYLLW,
                   relief='groove', highlightbackground=OYELLOW)
    func9.pack()
    func9 = Button(funcframe, text='變更練習的範圍', bg=OYELLOW, width=14, activebackground=DRKYLLW,
                   relief='groove', highlightbackground=OYELLOW)
    func9.pack()
    funcsen = Button(funcframe, text='我要看範例造句', bg=OYELLOW, width=14, activebackground=DRKYLLW,
                   relief='groove', highlightbackground=OYELLOW)
    funcsen.pack(pady=(5,0))
    func8 = Button(funcframe, text='查詢該單詞詞源', bg=OYELLOW, width=14, activebackground=DRKYLLW,
                   relief='groove', highlightbackground=OYELLOW, command=lambda:bopen('https://www.etymonline.com/search?q='+word))
    func8.pack(pady=(5,0))
    funcg = Button(funcframe, text='開啟Google翻譯', bg=OYELLOW, width=14, activebackground=DRKYLLW,
                   relief='groove', highlightbackground=OYELLOW, command=lambda:bopen('https://translate.google.com.tw/?hl=zh-TW&sl=en&tl=zh-TW&text='+word))
    funcg.pack()
    funcc = Button(funcframe, text='聯絡開發團隊', bg=OYELLOW, width=14, activebackground=DRKYLLW,
                   relief='groove', highlightbackground=OYELLOW, command=contactUs)
    funcc.pack(pady=(5,5))
    
    #btn = Button(funcframe, bg=BGCOLOR, width=14, height=2)
    #btn.pack()
    
    lvlframe = Frame(subframes[1], bg=BGCOLOR)
    lvlframe.pack()
    lvltext = Label(lvlframe, text="選擇等級：", bg=BGCOLOR, font=("微軟正黑體", 9))
    lvltext.grid(row=1, column=0)
    lvltext2 = Label(lvlframe, text=1, bg=BGCOLOR, font=("微軟正黑體", 10))
    lvltext2.grid(row=1, column=1)
    lvlscrollbar = Scale(lvlframe, orient='horizontal', bg=BGCOLOR, troughcolor=BGCOLOR, from_=1, to=6, width=20, 
                         activebackground=BGCOLOR, highlightbackground=BGCOLOR, command=scaleValue, showvalue=0)
    lvlscrollbar.grid(row=1, column=2)
    
    explanation = Label(subframes[1], text='', bg=BGCOLOR, font=("微軟正黑體", 12))
    explanation.pack(pady=10)
    
    optframe = Frame(subframes[1], bg=BGCOLOR)
    optframe.pack()
    createOpts()
        
    #btns below options
    framebtns = Frame(subframes[1], bg=BGCOLOR, width=500)
    framebtns.pack(expand=True)
    
    markUnskilled = Button(framebtns, text='標記為不熟', bg=OYELLOW, activebackground=DRKYLLW, padx=5, pady=4, width=12,
                    font=("微軟正黑體", 10), command=markAsUnskilled)
    markUnskilled.grid(row=0, column=0, pady=5)
    nextQ = Button(framebtns, text="下一題", bg=DRKYLLW, activebackground=DRKYLLW, padx=5, pady=6, highlightbackground=DRKYLLW, 
                   font=("微軟正黑體", 13), command=nextQuestion, width=8)
    nextQ.grid(row=0, column=1, pady=5, padx=5)
    showKK_txt = '顯示KK音標' if database.get()[:3] == '[1]' else '顯示國際音標'
    showKK = Button(framebtns, text=showKK_txt, bg=OYELLOW, activebackground=DRKYLLW, padx=5, pady=4, width=12,
                    font=("微軟正黑體", 10), command=showKKphonics)
    showKK.grid(row=0, column=2, pady=5, sticky="w")
    showKK.grid_columnconfigure(2,minsize=500)
    
    #text count corrects
    correctcount = Label(subframes[1], text='答對題數：0', bg=BGCOLOR, font=("微軟正黑體", 12))
    correctcount.pack()
    Label(subframes[1], text=' '*100, bg=BGCOLOR, font=("微軟正黑體", 12)).pack()

    Label(root, text='Copyright Ⓒ 2021 alexhou00. All rights reserved.', bg=BGCOLOR, fg='#999999', font=("微軟正黑體", 7)).pack(anchor='e')
    
    refreshOptions()

    
def refreshOptions():
    global lvlscrollbar, dictionary, explanation, opts, word, lstshuffle, index, nextQ, showKK, answerable, func8, funcg, showKK_txt
    global QTYPE, qtvar
    answerable = True
    for i in range(len(opts)): opts[i].config(state='normal')
    pickRandomWord()
    
    if QTYPE.index(qtvar.get()) == 1:
        without_item = [x for i,x in enumerate(dictionary[lvlscrollbar.get()-1]) if x[0][0]!=word]
        lstshuffle = [word,]
        #Look for all similar words
        lstsimilar = []    
        for j in range(3, 0, -1):
            lstsimilar_iter = [i[0][0] for i in without_item if i[0][0].startswith(word[:j].lower())]
            shuffle(lstsimilar_iter)
            lstsimilar.extend(lstsimilar_iter)
        #Remove duplicates
        seen = set()
        seen_add = seen.add
        lstsimilar = [x for x in lstsimilar if not (x in seen or seen_add(x))]
        #Add other random 3 fake options from all similar words
        if len(lstsimilar)>=3:
            for i in range(3):
                lstshuffle.append(lstsimilar[i])
        else:
            for i in range(3):
                lstshuffle.append(without_item[i][0][0])
        shuffle(lstshuffle)
        #Refresh buttons
        for i in range(len(opts)): opts[i].config(text=lstshuffle[i])
    elif QTYPE.index(qtvar.get()) == 0:
        opts[0].config(text=word)
    
    nextQ.config(state='disabled')
    showKK.config(text=showKK_txt, state='disabled')
    func8.config(state='disabled')
    funcg.config(state='disabled')

def createOpts(haveToDestroy=0):
    global opts, subframes, optframe
    if haveToDestroy:
        for i in opts:
            i.destroy()
    #create options
    modeLocal = QTYPE.index(qtvar.get())
    if modeLocal == 1:
        for q in range(4):
            opts[q] = Button(optframe, text='', width=14, height=2, bg=OYELLOW, relief='groove', bd=3, 
                             font=("微軟正黑體", 13), activebackground=DRKYLLW, command=lambda q=q:optClicked(q))
            opts[q].grid(row=q//2, column=q%2, padx=4, pady=4)
    elif modeLocal == 0:
        opts = [[] for x in range(3)]
        opts[0] = Label(optframe, font=("微軟正黑體", 14), bg=BGCOLOR)
        opts[0].grid(row=0, columnspan=2, pady=5)
        for q in range(1, 3):
            opts[q] = Button(optframe, text=('O', "X")[q-1], width=14, height=4, bg=OYELLOW, relief='groove', bd=3, 
                             font=("微軟正黑體", 13), activebackground=DRKYLLW, command=lambda q=q:optClicked(q))
            opts[q].grid(row=1, column=q-1, padx=4, pady=4)
            
    if haveToDestroy: refreshOptions()
    
def optClicked(option):
    global word, lstshuffle, explanation, answerable
    if answerable:
        if lstshuffle[option] == word:
            explanation.after(0, lambda:showCorrect(1, 0, option))
        else:
            explanation.after(0, lambda:showCorrect(0, 0, option))

def markAsUnskilled():
    global isFirstTimeMark
    if isFirstTimeMark:
        messagebox.showinfo("操作提示","標記此單字為不熟後，並累積足夠的不熟單字，"+\
                            "即可點選右邊的「練習不熟的單字」，把不熟悉的單字加以練習以達到精熟。")
        isFirstTimeMark = False

def clearRecords():
    global records, clearRecord
    records.config(state='normal')
    records.delete(1.0, "end")
    clearRecord.config(text='已清空✔', fg='green')
    clearRecord.after(1000, lambda:clearRecord.config(text='清空答題紀錄', fg='black'))
    records.config(state='disabled')

def contactUs():
    top = Toplevel()
    top.resizable(False, False)
    top.config(bg=BGCOLOR)
    top.grab_set()
    top.wm_iconbitmap("p/logo.ico")
    
    Label(top, text='聯絡開發團隊', bg=BGCOLOR, font=("微軟正黑體", 14)).pack(padx=10, pady=10)
    Label(top, text='版本 Ver.1.0.3', bg=BGCOLOR, font=("微軟正黑體", 10)).pack(pady=5)
    problemF = Frame(top, bg=BGCOLOR)
    problemF.pack()
    Label(problemF, text='遇到困難了嗎？ 點', bg=BGCOLOR, font=("微軟正黑體", 10)).pack(padx=(10,0), pady=5, side='left')
    here = Label(problemF, text='這裡', bg=BGCOLOR, font=("微軟正黑體", 10, 'underline'), fg='blue')
    here.pack(side='left')
    here.bind("<Button-1>", lambda x:bopen("https://google.com"))
    Label(problemF, text='以獲取更多幫助', bg=BGCOLOR, font=("微軟正黑體", 10)).pack(padx=(0,20), pady=5, side='left')
    Label(top, text='有更多問題可以聯絡 alexhou00@gmail.com', bg=BGCOLOR, font=("微軟正黑體", 10)).pack(padx=10, pady=10)
    introtxt = "備註：\n說是開發團隊啦，可是作者只有一位可憐的高中生，"+\
                "寫這份程式的時候作者只是一位建中某班的小高一\n因為苦於背單字以及對臺灣英文教育的不喜愛而建立此系統\n"+\
                "有更多程式的建議也可以聯絡上述電子郵件 \n"+\
                "我覺得整體程式的介面也是很有復古風，可以算是特色嗎 \n然後本作品僅作為個人用途使用喔"
    Label(top, text=introtxt, bg=BGCOLOR, font=("微軟正黑體", 10), justify='left').pack(padx=10, pady=10)
    
    top.mainloop()

def fileSave():
    f = filedialog.asksaveasfile(filetypes=[("文字文件(*.txt)", "*.txt")], mode='w', defaultextension=".txt")
    if f is None: 
        return
    text2save = str(records.get(1.0, 'end'))
    f.write(text2save)
    f.close() 

def nextQuestion():
    global records, word, correctcount, counts, modevar, qtvar, MODES, QTYPE
    records.config(state='normal')
    records.insert('1.0', word+'\n')
    records.config(state='disabled')
    correctcount.config(text='答對題數：'+str(counts[MODES.index(modevar.get())+QTYPE.index(qtvar.get())*2])+
                        "題 於 ("+''.join(modevar.get().split())+''.join(qtvar.get().split())+'的Lv.'+str(lvlscrollbar.get())+')')
    refreshOptions()

def showKKphonics():
    global showKK, item
    showKK.config(text=item[1].replace("ˋ","`"))

def showCorrect(isCorrect, haveShown, optChosen):
    global explanation, word, lstshuffle, nextQ, showKK, opts, answerable, chinese_, counts, func8, funcg
    global MODES, QTYPE, modevar, qtvar
    answerable = False
    if haveShown == 0:
        if isCorrect == 1:
            explanation.config(text="\n你答對了\n", fg='green')
            a = MODES.index(modevar.get())+QTYPE.index(qtvar.get())*2
            counts[a] += 1
            for i in range(len(opts)):
                if i != optChosen: opts[i].config(state='disabled')
                else: opts[i].config(state='normal')
            #explanation.after(500, lambda:showCorrect(1, 1))
        else:
            explanation.config(text=f"你答錯了\n題目：{chinese_} \n正確答案：{word}   你的回答：{lstshuffle[optChosen]}", fg='red')
            for i in range(len(opts)):
                if QTYPE.index(qtvar.get()) == 1:
                    if i != lstshuffle.index(word): opts[i].config(state='disabled')
                    else: opts[i].config(state='normal')
                else:
                    for thing in opts: thing.config(state='disabled')
            #explanation.after(2000, lambda:showCorrect(0, 1))
        nextQ.config(state='normal')
        showKK.config(state='normal')
        func8.config(state='normal')
        funcg.config(state='normal')
    #else:
        #refreshOptions()
    pass

def pickRandomWord():
    global word, index, chinese_, dictionary, item
    index = randint(0, len(dictionary[lvlscrollbar.get()-1])) #index of correct answer
    item = dictionary[lvlscrollbar.get()-1][index] # ITEM: correct answer: (("word",), "KKphonics", "explanation")
     
    chinese_ = item[2]
    chinese_ = chinese_.replace("*換行*", "\n")
    explanation.config(text='\n'+chinese_.rstrip('[')+'\n', fg='#000000')
    word = item[0][0]
    
    
def scaleValue(val):
    global lvltext2, counts
    counts = [0 for x in range(6)]
    lvltext2.config(text=val)
    refreshOptions()

def confirmCMD():
    global dictionary, database
    win.destroy()
    
    if database.get()[:3] == '[0]': #extract data from Database[0]
        with open("p/senior_7000_0.dat", "r", encoding="utf-8") as f:
            level = 0
            for line in f:
                if (not("====" in line)) and line.strip()!='':
                    words = line.split('@')
                    words[0] = (words[0],)
                    words[2] = ''.join([i for i in words[2] if not i.isdigit()])
                    dictionary[level-1].append(words)
                elif "====" in line:
                    level += 1
                
                
    elif database.get()[:3] == '[1]': #extract data from Database[1]
        with open("p/extracted_7000_1_edited.dat", "r", encoding="utf-8") as f1:
            level = 0
            for line in f1:
                if (not("大考中心" in line)) and line.strip()!='':
                    idx = line.find("[")
                    word = line[:idx]
                    word = word.replace("*換行*", "\n")
                    idx2 = line.find("]")
                    while ('/' in line[idx2:idx2+4]):
                        idx2 = line.find("]", idx2+1)
                    while (line[idx2+1] == '[' or line[idx2+1:idx2+3] == ' ['):
                        idx2 = line.find("]", idx2+1)
                    phonics = line[idx:idx2+1]
                    chinese = line[idx2+1:]
                    phonics = phonics.replace(" ", '')
                    chinese = ' '.join(chinese.split())
                    dictionary[level-1].append((tuple(word.strip().split('/')), phonics.strip(), chinese.strip()))
                elif "大考中心" in line:
                    level += 1
        #[print(i) for i in dictionary[4] if "AI" in i[0]]
    start()

def welcomeWindow():
    global database
    win.title("高中英文7000單字練習系統歡迎畫面 - Windows版")
    win.resizable(False, False)
    win.config(bg=BGCOLOR)
    win.wm_iconbitmap('p/logo.ico')
    
    lstDatabase = ("[0] 臺南市私立港明高級中學學習資源_高中7000單字表_格式整齊",
                   "[1] 桃園市立桃園國民中學整理之高中英文參考詞彙表_精準中譯",
                   "[2] 大學入學考試中心基金會《91高中英文參考詞彙表》_舊課綱",
                   "[3] 大學入學考試中心基金會《108高中英文參考詞彙表》_新課綱",
                   "[4] 自訂題庫A_儲存名稱1",
                   "[5] 自訂題庫B_儲存名稱2",
                   "[6] 自訂題庫C_儲存名稱3",)
    
    database = StringVar(win)
    database.set(lstDatabase[1])
    
    
    #Title and select database
    title = Label(win, text="高中英文7000單字練習系統", bg=BGCOLOR, font=("微軟正黑體", 16))
    title.pack(padx=10, pady=10)
    databaseFrame = Frame(win, bg=BGCOLOR)
    databaseFrame.pack(padx=10)
    dblbl = Label(databaseFrame, text="選擇題庫：", bg=BGCOLOR)
    dblbl.grid(row=0, column=0, pady=10)
    dbmenu = OptionMenu(databaseFrame, database, *lstDatabase)
    dbmenu.grid(row=0, column=1, pady=10)
    dbmenu.config(bg=BGCOLOR, width=50, activebackground=BGCOLOR, highlightbackground=BGCOLOR)
    dbmenu["menu"].config(bg=BGCOLOR, bd=0)
    confirm = Button(win, bg=DRKYLLW, text="確認", font=("微軟正黑體", 11), command=confirmCMD, 
                     activebackground=DRKYLLW, pady=1, padx=1)
    confirm.pack(pady=10)

    win.mainloop()

#Some constants    
BGCOLOR = "#ffffcc"
OYELLOW = "#F6E56F"
DRKYLLW = "#ffdd44"
#WINWIDTH = 688

dictionary = [[] for x in range(6)]
opts = [[] for x in range(4)]
counts = [0 for x in range(6)]

MODES = [" 中 翻 英 ", " 填 例 句 "]
QTYPE = [" 是 非 題 ", " 選 擇 題 ", " 填 充 題 "]

#global variable declaration
lvltext2 = 0
lvlscrollbar = 0
explanation = 0
word = ""
lstshuffle = []
index = 0
nextQ = showKK = 0
answerable = True
chinese_ = ''
item = tuple()
database = 0
records = 0
modevar = qtvar = 0
correctcount = 0
func8 = funcg = 0
clearRecord = 0
isFirstTimeMark = True
showKK_txt = ''
subframes = []
optframe = 0

win = Tk()
welcomeWindow()


