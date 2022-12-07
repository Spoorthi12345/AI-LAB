import copy

inp=[[1,2,3],[4,-1,5],[6,7,8]]
out=[[1,2,3],[6,4,5],[-1,7,8]]

def move(temp, movement):
  if movement=="up":
    for i in range(3):
      for j in range(3):
        if(temp[i][j]==-1):
         
          if i!=0:
            temp[i][j]=temp[i-1][j]
            temp[i-1][j]=-1
          return temp

  if movement=="down":
    for i in range(3):
      for j in range(3):
        if(temp[i][j]==-1):
        
          if i!=2:
            temp[i][j]=temp[i+1][j]
            temp[i+1][j]=-1
          return temp

  if movement=="left":
    for i in range(3):
      for j in range(3):
        if(temp[i][j]==-1):
        
          if j!=0:
            temp[i][j]=temp[i][j-1]
            temp[i][j-1]=-1
          return temp

  if movement=="right":
    for i in range(3):
      for j in range(3):
        if(temp[i][j]==-1):
        
          if j!=2:
            temp[i][j]=temp[i][j+1]
            temp[i][j+1]=-1
          return temp
def ids():
  global inp
  global out
  global flag

  for limit in range(100):
    print('LIMIT -> '+str(limit))
    stack=[]
    inpx=[inp,"none"]
    stack.append(inpx)
   
    level=0
    while(True):
      if len(stack)==0:
        break
      puzzle=stack.pop(0)
      if level<=limit:
        print(str(puzzle[1])+" --> "+str(puzzle[0]))
        if(puzzle[0]==out):
          print("Found")
          print('Path cost='+str(level))
          flag=True
          return
        else:
          level=level+1
        
          if(puzzle[1]!="down"):
            temp=copy.deepcopy(puzzle[0])
            up=move(temp, "up")
            if(up!=puzzle[0]):
              upx=[up,"up"]
              stack.insert(0, upx)
          
          if(puzzle[1]!="right"):
            temp=copy.deepcopy(puzzle[0])
            left=move(temp, "left")
            if(left!=puzzle[0]):
              leftx=[left,"left"]
              stack.insert(0, leftx)
          
          if(puzzle[1]!="up"):
            temp=copy.deepcopy(puzzle[0])
            down=move(temp, "down")
            if(down!=puzzle[0]):
              downx=[down,"down"]
              stack.insert(0, downx)
          
          if(puzzle[1]!="left"):
            temp=copy.deepcopy(puzzle[0])
            right=move(temp, "right")
            if(right!=puzzle[0]):
              rightx=[right,"right"]
              stack.insert(0, rightx)
          


print('~~~~~~~~~~~~ IDS ~~~~~~~~~~~~')
ids()


