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
    for x in range(5):
        for y in range(9):
            if Map[x][y] == 0:
                return x, y


def willgo(x, y):  # 便于理解
    return Map[x][y]


def move():
    ls=[0,1,2,3]
    x, y = getplace(Map)
    #排除无法进行的移动
    delete=[]
    if x+1>4 or Map[x+1][y]==4: #人物碰到箱子或障碍
        delete.append(0)
    elif x+2>4 and Map[x+1][y]==1: #箱子推出地图边界
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
    if y+1>8 or Map[x][y+1]==4:
        delete.append(2)
    elif y+2>8 and Map[x][y+1]==1:
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
    if willgo(x,y)==1:
        if act=="↓":
            Map[x+1][y]=1
        elif act=="↑":
            Map[x-1][y]=1
        elif act=="→":
            Map[x][y+1]=1
        elif act=="←":
            Map[x][y-1]=1
    Map[x][y] = 0
    Map[a][b] = bord[a][b]  # 离开该格子后，该格子属性由0变为原属性
    return act


#    elif willgo(x,y)==4: #遇到障碍
#       move()
#    elif willgo(x,y)==3: #滑块

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
        if cnt>=30:
            break
    return cnt, Step


Min = 99999
for i in range(10000000000):
    Map = [[4, 2, 1, 1, 1, 2, 1, 2, 2],
           [2, 4, 2, 1, 1, 1, 1, 2, 4],
           [4, 4, 2, 1, 2, 2, 2, 2, 4],
           [4, 4, 1, 2, 1, 1, 1, 2, 4],
           [0, 2, 2, 1, 1, 2, 2, 4, 4]]#物块类型数据
    bord =[[4, 2, 2, 2, 2, 2, 2, 2, 2],
           [2, 4, 2, 2, 2, 2, 2, 2, 4],
           [4, 4, 2, 2, 2, 2, 2, 2, 4],
           [4, 4, 2, 2, 2, 2, 2, 2, 4],
           [2, 2, 2, 2, 2, 2, 2, 4, 4]] #地板类型数据
    cnt, Step = goto(0, 8)
    if cnt < Min:
        Min = cnt
        Step0 = Step
        Map0 = Map
print(Min, Step0)
print(Map0)

# 极待添加：滑块，推箱子等动作


# 有待添加块:
# # 用户图形界面
# # 用户输入界面
#
# # 缺点：模间耦合度高

