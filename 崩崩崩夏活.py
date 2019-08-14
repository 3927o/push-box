# 推箱子
# 辣鸡蹦蹦蹦夏活推箱子卡我半天

# 0:people
# 1:box
# 2;board
# 3:slip_board
# 4;barrier

# 输入地图
Map = [[0, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2]]

def getplace(Map):  # 获取人物坐标
    global width,length
    for x in range(width):
        for y in range(length):
            if Map[x][y] == 0:
                return x, y

def willgo(x, y):  # 便于理解
    return Map[x][y]

def move():
    global width,length
    ls=[0,1,2,3]
    x, y = getplace(Map)
    #排除无法进行的移动
    delete=[]
    if x+1>=width or Map[x+1][y]==4: #人物碰到箱子或障碍
        delete.append(0)
    elif x+2>=width and Map[x+1][y]==1: #箱子推出地图边界
        delete.append(0)
    elif Map[x+1][y]==1 and Map[x+2][y]==4: #箱子碰到障碍
        delete.append(0)
    elif Map[x+1][y]==1 and Map[x+2][y]==1: #箱子碰到箱子（两个箱子连在一起）
        delete.append(0)
    if x-1<0 or Map[x-1][y]==4:
        delete.append(1)
    elif x-2<0 and Map[x-1][y]==1:
        delete.append(1)
    elif Map[x-1][y]==1 and Map[x-2][y]==4:
        delete.append(1)
    elif Map[x-1][y]==1 and Map[x-2][y]==1:
        delete.append(1)
    if y+1>=length or Map[x][y+1]==4:
        delete.append(2)
    elif y+2>=length and Map[x][y+1]==1:
        delete.append(2)
    elif Map[x][y+1]==1 and Map[x][y+2]==4:
        delete.append(2)
    elif Map[x][y+1]==1 and Map[x][y+2]==1:
        delete.append(2)
    if y-1<0 or Map[x][y-1]==4:
        delete.append(3)
    elif y-2<0 and Map[x][y-1]==1:
        delete.append(3)
    elif Map[x][y-1]==1 and Map[x][y-2]==4:
        delete.append(3)
    elif Map[x][y-1]==1 and Map[x][y-2]==1:
        delete.append(3)
    for i in delete:
        ls.remove(i)
    #排除无法进行的移动
    #随机移动
    import random
    num = random.choice(ls)
    a = x
    b = y
    if num == 0:
        x += 1
        act = "↓"  # 向下
    elif num == 1:
        x -= 1
        act = "↑"  # 向上
    elif num == 2:
        y += 1
        act = "→"  # 向右
    elif num == 3:
        y -= 1
        act = "←"  # 向左
    if willgo(x,y)==1 and bord[x][y]==3:
        x_box=x
        y_box=y
        m=1
        while m!=0:
            if act=="↓":
                if x_box+1>=width or Map[x_box+1][y_box] in [1,4]:
                    break
                x_box+=1
                if Map[x_box][y_box]==2:    break
            elif act=="↑":
                if x_box-1<0 or Map[x_box-1][y_box] in [1,4]:
                    break
                x_box-=1
                if Map[x_box][y_box] == 2:    break
            elif act=="→":
                if y_box>=length or Map[x_box][y_box+1] in [1,4]:
                    break
                y_box+=1
                if Map[x_box][y_box] == 2:    break
            elif act=="←":
                if y_box-1<0 or Map[x_box][y_box-1] in [1,4]:
                    break
                y_box-=1
                if Map[x_box][y_box] == 2:    break
        Map[x_box][y_box]=1
        Map[x][y]=bord[x][y] #推箱子时人物位置未变化
        return act
    elif willgo(x,y)==1:
        x_box=x
        y_box=y
        if act=="↓":
            Map[x_box+1][y_box]=1
        elif act=="↑":
            Map[x_box-1][y_box]=1
        elif act=="→":
            Map[x_box][y_box+1]=1
        elif act=="←":
            Map[x_box][y_box-1]=1
        Map[x][y]=bord[x][y]
        return act
    if willgo(x,y)==3: #人滑块
        m=1
        while m!=0:
            if act == "↓":
                if x+1>=width or Map[x+1][y] in [1,4]:
                    break
                x+=1
                if Map[x][y] == 2:    break
            elif act=="↑":
                if x-1<0 or Map[x-1][y] in [1,4]:
                    break
                x-=1
                if Map[x][y]==2:    break
            elif act=="→":
                if y+1>=length or Map[x][y+1] in [1,4]:
                    break
                y+=1
                if Map[x][y] == 2:    break
            elif act=="←":
                if y-1<0 or Map[x][y-1] in [1,4]:
                    break
                y-=1
                if Map[x][y] == 2:    break
    Map[x][y] = 0
    Map[a][b] = bord[a][b]  # 离开该格子后，该格子属性由0变为原属性
    return act

def goto(x, y):
    a,b= getplace(Map)
    cnt = 0
    t = 2
    Step = ""
    while a != x or b != y:
        step = move()
        cnt += 1
        Step += step
        a,b= getplace(Map)
        if cnt>=100:
            break
    return cnt, Step

Min = 99999
for i in range(1000):
    Map = [[4, 4, 2, 2, 2, 2, 2, 2],
           [4, 2, 2, 2, 2, 2, 2, 2],
           [4, 2, 2, 2, 4, 2, 2, 2],
           [2, 2, 2, 4, 3, 3, 4, 2],
           [2, 2, 3, 3, 3, 3, 2, 2],
           [2, 2, 3, 3, 3, 3, 2, 2],
           [2, 2, 3, 3, 3, 3, 2, 2],
           [0, 1, 3, 4, 3, 4, 2, 2],
           [2, 2, 2, 4, 2, 4, 4, 2]]#物块类型数据
    bord =[[2, 2, 2, 2, 2, 2, 2, 2],
           [4, 2, 2, 2, 2, 2, 2, 2],
           [4, 2, 2, 2, 4, 2, 2, 2],
           [2, 2, 2, 4, 3, 3, 4, 2],
           [2, 2, 3, 3, 3, 3, 2, 2],
           [2, 2, 3, 3, 3, 3, 2, 2],
           [2, 2, 3, 3, 3, 3, 2, 2],
           [2, 2, 3, 4, 3, 4, 2, 2],
           [2, 2, 2, 4, 2, 4, 4, 2]] #地板类型数据
    width=len(Map)
    length=len(Map[0])
    cnt, Step = goto(8, 4)
    if cnt < Min:
        Min = cnt
        Step0 = Step
        Map0 = Map
print(Min, Step0)
print(Map0)

# 代码复现严重，结构极差


# 有待添加块:
# # 用户图形界面
# # 用户输入界面
#
# # 缺点：模间耦合度高

# Map = [[2, 1, 2, 2, 2, 2, 1, 2],
#            [2, 4, 1, 1, 7, 1, 4, 2],
#            [2, 2, 2, 2, 2, 2, 2, 2],
#            [2, 4, 4, 4, 4, 4, 4, 2],
#            [0, 4, 2, 2, 2, 2, 4, 2]]多个箱子推一个到（4，7）

# Map = [[4, 2, 1, 1, 1, 2, 1, 2, 2, 2],
#        [2, 4, 2, 1, 1, 1, 1, 2, 1, 2],
#        [4, 4, 2, 1, 2, 2, 2, 2, 1, 2],
#        [4, 4, 1, 2, 1, 1, 1, 2, 1, 1],
#        [0, 2, 2, 1, 1, 2, 2, 1, 1, 1]]垃圾场地图（0，8）
