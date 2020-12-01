
import random
import os
import time


n=int(input("ENTER n:"))
a=[[0]*n for i in range(n)]
b=[]
h=[0]


class Grid:


	#defining grid class
	def __init__(self,n,start,goal,myObstacles,myRewards):
		self.n=n
		self.start=start
		self.goal=goal
		self.myObstacles=myObstacles
		self.myRewards=myRewards

	def showGrid(self):

		#prints nxn grid with obstacles and rewards and start position and goal
		for i in range(n):
			for j in range(n):
				if (i,j)==self.start:
					a[i][j]="o"
				elif (i,j)==self.goal:
					a[i][j]="g"
				elif(i,j) in b:
					a[i][j]="x"

				if h[0]==0:
					for k in range(len(self.myObstacles)):
						if (i,j) == (self.myObstacles[k].x,self.myObstacles[k].y):
							a[i][j]="#"
					for q1 in range(len(self.myRewards)):			
						if (i,j) ==(self.myRewards[q1].x,self.myRewards[q1].y):
							a[i][j]=str(self.myRewards[q1].v)

					
				if a[i][j]==0:
					a[i][j]="."						
							
 		   							 
				
		#prints nested list in the form of a grid			
		for row in a:
			print(' '.join(row))


	def rotateClockwise(self,z):
		
		
		#first we find the transpose of the matrix
		
		r=len(a)
		c=len(a[0])

		for p in range(z):

			r=len(a)
			c=len(a[0]) 
			x=[]
			
			for i in range(c):
				
				w=[]
				for j in range(r):
					w.append(a[j][i])
				x.append(w)			
		#then we reverse the rows of the transpose matrix to make it rotate clockwise	
			for row in x:
				row.reverse()

			for i in range(len(x)):
				for j in range(len(x[0])):
					a[i][j]=x[i][j]	#changing the original grid list as per rotation

		for row in x:			
			print(' '.join(row))

		for i in range(len(x)):
			for j in range(len(x[0])):
				a[i][j]=x[i][j]	

		for i in a:
			if "o" in i:
				v=i.index("o")
				i[v]="."
			if "g" in i:
				m=i.index("g")
				i[m]="."
		
				
		for i in range(len(a)):
			for j in range(len(a[0])):
				if a[i][j]=="#":
					
					x1.append(obstacle(i,j))
				if a[i][j]!="." and a[i][j]!="#" and a[i][j]!="x" and a[i][j]!="o" and a[i][j]!="g":
					x2.append(Reward(i,j,int(a[i][j])))				
			
		
	

	def rotateAnticlockwise(self,z):
		
		r=len(a)
		c=len(a[0])

		for p in range(z):

			r=len(a)
			c=len(a[0]) 
			x=[]
			
			for i in range(c):
				
				w=[]
				for j in range(r):
					w.append(a[j][i])
				x.append(w)			
			
			
			x.reverse()

			for i in range(len(x)):
				for j in range(len(x[0])):
					a[i][j]=x[i][j]	

		for row in x:			
			print(' '.join(row))

		for i in range(len(x)):
			for j in range(len(x[0])):
				a[i][j]=x[i][j]	

		for i in a:
			if "o" in i:
				v=i.index("o")
				i[v]="."
			if "g" in i:
				m=i.index("g")
				i[m]="."
		
				
		for i in range(len(a)):
			for j in range(len(a[0])):
				if a[i][j]=="#":
					
					x1.append(obstacle(i,j))
				if a[i][j]!="." and a[i][j]!="#" and a[i][j]!="x" and a[i][j]!="o" and a[i][j]!="g":
					x2.append(Reward(i,j,int(a[i][j])))



class obstacle:
	def __init__(self,x,y):
		self.x=x
		self.y=y

class Reward:
	def __init__(self,x,y,v):
		self.x=x
		self.y=y
		self.v=v

		

class Player:
	def __init__(self,x,y,energy):
		self.x=x
		self.y=y
		self.energy=energy



	def makeMove(self,S):
		S=S.upper()

		global g1
		x1=g1.myObstacles
		x2=g1.myRewards
		global h
		h=[1]
		print(h)
		z1=[]
		z2=[]
		for i in range(len(S)):
			if S[i].isalpha():
				z1.append(S[i])

		for j in range(len(z1)):
			if z1[j]!=z1[-1]:
				x=S.index(z1[j])
			

				y=S.index(z1[j+1])
				p=S[x+1:y]
				z2.append(z1[j])
				z2.append(int(p))
			else:
				x=S.index(z1[j])
				p=S[x+1:]
				z2.append(z1[j])
			
				z2.append(int(p))
			
		for i in z2:		
			if i == "R":
				u=z2.index("R")
				v=z2[u+1]
				for i in range(1,v+1):

					
					h=[1]	
					self.y+=1
					self.energy-=1
					if self.y>n-1:
						self.y=0
					if self.y<0:
						self.y=n-1	
					if self.x>n-1:
						self.x=0
					if self.x<0:
						self.x=n-1

							
					a[self.x][self.y]="o"
					for i in range(len(x1)):
						if (self.x,self.y)==(x1[i].x,x1[i].y):
							self.energy-=4*n
					for j in range(len(x2)):
						if (self.x,self.y)==(x2[j].x,x2[j].y):
							self.energy+=x2[j].v*n		

					a[self.x][self.y-1]="x"
					os.system('cls' if os.name=='nt' else 'clear')
					g1=Grid(n,(self.x,self.y),(n-1,s2),x1,x2)
					g1.showGrid()
					print("ENERGY:"+str(self.energy))
					
					time.sleep(0.5)
					


					
			
			elif i=="D":
				h=[1]
				u=z2.index("D")
				v=z2[u+1]
				for i in range(1,v+1):
					
					
					self.x+=1
					self.energy-=1
					if self.y>n-1:
						self.y=0
					if self.y<0:
						self.y=n-1	
					if self.x>n-1:
						self.x=0
					if self.x<0:
						self.x=n-1
					a[self.x][self.y]="o"
					for i in range(len(x1)):
						if (self.x,self.y)==(x1[i].x,x1[i].y):
							self.energy-=4*n
					for j in range(len(x2)):
						if (self.x,self.y)==(x2[j].x,x2[j].y):
							self.energy+=x2[j].v*n

					a[self.x-1][self.y]="x"
					os.system('cls' if os.name=='nt' else 'clear')
					
					g1=Grid(n,(0,self.x,self.y),(n-1,s2),x1,x2)
					g1.showGrid()
					print("ENERGY:"+str(self.energy))
					
					time.sleep(0.5)
					

			elif i=="L":
				u=z2.index("L")
				v=z2[u+1]
				for i in range(1,v+1):
					

					self.y-=1
					self.energy-=1
					if self.y>n-1:
						self.y=0
					if self.y<0:
						self.y=n-1	
					if self.x>n-1:
						self.x=0
					if self.x<0:
						self.x=n-1
					a[self.x][self.y]="o"
					for i in range(len(x1)):
						if (self.x,self.y)==(x1[i].x,x1[i].y):
							self.energy-=4*n
					for j in range(len(x2)):
						if (self.x,self.y)==(x2[j].x,x2[j].y):
							self.energy+=x2[j].v*n
					if self.y>=n-1:
						a[self.x][0]="x"
					else:			
						a[self.x][self.y+1]="x"
					os.system('cls' if os.name=='nt' else 'clear')
					u=[1]
					g1=Grid(n,(self.x,self.y),(n-1,s2),x1,x2)
					g1.showGrid()
					print("ENERGY:"+str(self.energy))
					
					time.sleep(0.5)
					

			elif i=="U":
				u=z2.index("U")
				v=z2[u+1]
				for i in range(1,v+1):
					

					self.x-=1
					self.energy-=1
					if self.y>n-1:
						self.y=0
					if self.y<0:
						self.y=n-1	
					if self.x>n-1:
						self.x=0
					if self.x<0:
						self.x=n-1
					a[self.x][self.y]="o"
					for i in range(len(x1)):
						if (self.x,self.y)==(x1[i].x,x1[i].y):
							self.energy-=4*n
					for j in range(len(x2)):
						if (self.x,self.y)==(x2[j].x,x2[j].y):
							self.energy+=x2[j].v*n
					if self.x>=n-1:		
						a[0][self.y]="x"
					else:
						a[self.x+1][self.y]="x"	
					os.system('cls' if os.name=='nt' else 'clear')
					
					g1=Grid(n,(0,s1),(n-1,s2),x1,x2)
					g1.showGrid()
					print("ENERGY:"+str(self.energy))
					
					time.sleep(0.5)

		if S[0]=="C":



			k=int(S[1])
			z=0
			g1.rotateClockwise(k)
			for r in range(len(x1)):

				if (p1.x,p1.y)==(x1[r].x,x1[r].y):
					z+=1

			if z>0:
				
				os.system('cls' if os.name=='nt' else 'clear')

				g1.rotateAnticlockwise(k)
				print("Grid can't be rotated")
			else:
				self.energy-=n//3
				g1.rotateAnticlockwise(k)
				os.system('cls' if os.name=='nt' else 'clear')			
				x1=[]
				x2=[]	
				g1.rotateClockwise(k)
				os.system('cls' if os.name=='nt' else 'clear')
				h=[1]
				g1=Grid(n,(p1.x,p1.y),(n-1,s2),x1,x2)
				(g1.showGrid())
				print("ENERGY:" + str(p1.energy))

		elif S[0]=="A":
			k=int(S[1])
			z=0
			g1.rotateAnticlockwise(k)
			for r in range(len(x1)):

				if (p1.x,p1.y)==(x1[r].x,x1[r].y):
					z+=1

			if z>0:
				
				os.system('cls' if os.name=='nt' else 'clear')

				g1.rotateClockwise(k)

				print("Grid can't be rotated")
			else:
				self.energy-=n//3
				g1.rotateClockwise(k)
				os.system('cls' if os.name=='nt' else 'clear')			
				x1=[]
				x2=[]	
				g1.rotateAnticlockwise(k)
				os.system('cls' if os.name=='nt' else 'clear')
				h=[1]
				g1=Grid(n,(p1.x,p1.y),(n-1,s2),x1,x2)
				(g1.showGrid())
				print("ENERGY:" + str(p1.energy))
				

		










def generate_plane(plane_size, num_pts):
   
    
    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i%plane_size[0] + 1, i//plane_size[1] + 1) for i in gen]

    return random_points



  
num_pts1 = n//2+1
num_pts2 = n//2+1

plane_size = (n-1, n-1) 
plane1 = generate_plane(plane_size, num_pts1)
plane2 = generate_plane(plane_size, num_pts2)
    

myObstacles=plane1

myRewards=plane2
m=[]
j=[]
for i in myRewards:
	

	j.append(random.randint(1,9))
	l=dict(zip(myRewards,j))


x1=[]
for i in range(len(plane1)):
	x1.append(obstacle(plane1[i][0],plane1[i][1]))



x2=[]
c1=list(dict.items(l))
for i in range(len(c1)):
	x2.append(Reward(c1[i][0][0],c1[i][0][1],c1[i][1]))




s1=random.randint(0,n-1)
s2=random.randint(0,n-1)
g1=Grid(n,(0,s1),(n-1,s2),x1,x2)
g1.showGrid()
print()




print("Energy: "+ str(2*n))


p1=Player(0,s1,2*n)
while (p1.x,p1.y)!=g1.goal:

	

	
	if p1.energy>0:
		S=input()
		p1.makeMove(S)
	else:
		break	

print("Game Over")


