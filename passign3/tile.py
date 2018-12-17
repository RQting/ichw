    def change(x):       #x为方块的编号，x%m为横坐标，x//m为纵坐标
        t = []
        t.append(x%m)
        t.append(x//m)
        return t

    def brick(u,v,x):
        brick = []
        for i in range(u):
            for j in range(v):
                brick.append(x + i + m * j)
        return brick
    
    def judgebrick(u,v,x,p):
        if (change(x)[0]+u-1) >= m or (change(x,)[1]+v-1) >= n:
            return False
        for i in brick(u,v,x):
            for j in range(p):
                if i in solution[j]:
                    return False
        return True
    
    def brick_useable():   #检测砖块是否可铺满墙
        if m*n <= a*b:
            print('The brick is too big')  # 判断墙是否比砖块大
        if (m*n) % (a*b) != 0:
            print("The wall can't be paved completely")
        if m*n>=a*b and (m*n) %(a*b)==0:
            return True
        
    def conflict(x,p,solution):
        
        for i in range(p):
            if x in solution[i]:
                return True
        return False

    def solve(x,p):
        if p == m*n//(a*b):
            print(solution)
            tt.append(solution[:])
        else:
        
            if conflict(x,p,solution):
                solve(x+1,p)
            if not conflict(x,p,solution):
                if judgebrick(a,b,x,p):
                    solution[p] = brick(a,b,x)
                    solve(x+1,p+1)
                if judgebrick(b,a,x,p):
                    solution[p] = brick(b,a,x)
                    solve(x+1,p+1)
    def draw_wall():
        apen.speed(0)
        apen.pensize(8)     #绘制墙的外围
        apen.penup()
        apen.goto(-(m*30)/2,-(n*30)/2)
        apen.pendown()
        for l in range(2):   
            apen.fd(m*30)
            apen.lt(90)
            apen.fd(n*30)
            apen.lt(90)
        
    def draw_diamond():        #绘制墙中的方块
        apen.color('blue') 
        apen.pensize(3)
        for i in range(n-1):
            apen.penup()
            apen.goto((-m/2)*30,(-n/2+1+i)*30)
            apen.pendown()
            apen.fd(m*30)
        apen.rt(90)
        for i1 in range(m-1):
            apen.penup()
            apen.goto((-m/2+1+i1)*30,(n/2)*30)
            apen.pendown()
            apen.fd(n*30)
        
    def draw_number():  #绘制墙中方块的编号
        wall=[]    #对墙上表格（及方块）的编号
        k=0    # k 用于对表格的编号
        for i in range(n):
            wall.append([])
            for j in range(m):
                wall[i].append(k)
                k=k+1
        apen.penup()
        apen.color('purple')
        for i2 in range(n):
            apen.goto(((-m+1)/2)*30,((n-1)/2-i2)*30)
            for i3 in range(m):
                apen.goto(((-m+1)/2+i3)*30,((n-1)/2-i2)*30)
                apen.write(wall[i2][i3])
            
    def draw_brick():
        apen.color('brown')
        for z0 in tt[z-1]: 
            apen.penup()
            m2=z0[0] % m
            n2=z0[0] // m
            if z0[a-1]-z0[0]==a-1:
                apen.goto((m2-m/2)*30,(n/2-n2)*30)
                apen.pendown()
                for i in range(2):
                    apen.fd(a)
                    apen.rt(90)
                    apen.fd(b)
                    apen.rt(90)

            else:
                apen.goto((m2-m/2)*30,(n/2-n2)*30)
                apen.pendown()
                for i in range(2):
                    apen.fd(b)
                    apen.rt(90)
                    apen.fd(a)
                    apen.rt(90)   
    
    import turtle
    m=int(turtle.numinput("please input the wall's length",'wall length:',1,minval=0,maxval=100))  #输入墙的长宽 m,n 和砖块的长宽a,b
    n=int(turtle.numinput("please input the wall's width",'wall width:',1,minval=0,maxval=100))
    a=int(turtle.numinput("please input brick's length",'brick length:',1,minval=0,maxval=100))
    b=int(turtle.numinput("please input brick's width",'brick width:',1,minval=0,maxval=100))
    z=int(turtle.numinput("",'choose the solution you want to draw:',1,minval=0,maxval=1000))
    if brick_useable():
        apen=turtle.Turtle()
        draw_wall()
        draw_diamond()
        draw_number()
        tt=[]
        solution = [0 for i in range(m*n//(a*b))]
        print(solve(0,0))
        apen.lt(90)
        draw_brick()
