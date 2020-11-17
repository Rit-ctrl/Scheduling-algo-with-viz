from manimlib.imports import *
import os
import pyclbr

class hrrn(ThreeDScene):
    
    def construct(self):

        heading=TextMobject("HRRN ")
        heading.to_edge(UP+LEFT)
        self.play(Write(heading),run_time=2)

        
        p,seq=sim()
        self.animate(heading,seq,q=None)

    def animate(self,heading,seq,q):

        time=0
        text1=[]
        text2=[]
        clk=TextMobject("time ={}".format(str(time)))
        clk.next_to(heading,DOWN,buff=0.5)
        clk.scale(0.8)
        self.add(clk)
        self.play(Write(clk))
        # r_text=TexMobject("Ready queue")
        # r_text.to_corner(RIGHT+UP)
        # r_text.scale(0.5)

        #rq=q
        
        for i in range(len(seq)):
            if(seq[i][0]==-1):
                text1.append(TextMobject("E"))
            else:
                text1.append(TextMobject("P{}".format(str(seq[i][0]))))
            text2.append(TextMobject(str(seq[i][1])))
        
        
        for i in range(len(seq)):
            if i==0:
                text1[i].to_edge(LEFT)
                text2[i].next_to(text1[i],DOWN,buff=0.8)
            else:
                text1[i].next_to(text1[i-1],RIGHT,buff=0.8)
                text2[i].next_to(text1[i],DOWN,buff=0.8)
            
            counter=0
            while(counter<seq[i][1]):
                time+=1
                self.play(Transform(clk,TextMobject("time ={}".format(str(time))).next_to(heading,DOWN,buff=0.5)))
                self.play(Write(text1[i]))

            
                
                #self.play(Transform(r_text,TextMobject("Ready queue "+str(rq[i])).to_corner(RIGHT+UP).scale(0.5)))
                #print(r)
                #print("\n")                   
                counter+=1
                

            self.play(Write(text2[i]))
            #self.move_camera(frame_center=[2,0,0])     
            #self.move_camera(frame_center=(0,0,0))
            self.wait(2)

def index(e):
    return e[1]

def sim():
    #processes=[[1,0,3],[2,2,6],[3,4,4],[4,6,5],[5,8,2]] #[process_id,arrival time,burst_time]
    processes=[[1,1,1],[2,4,2],[3,5,6],[4,6,2],[5,7,4]]
    num=len(processes)

    for i in range(num):
        a=[]
        a.append(int(0))
        a.append(int(0))
        a.append(int(0))
        a.append(int(0))
        processes[i].extend(a)
    seq=HRRN(processes,num)
    return processes,seq

   
def swap(process,i,j):
	
	for k in range(7):
		process[i][k], process[j][k]=process[j][k], process[i][k]


def sort_arrival_time(process,num):
	
	for i in range(num):
		for j in range(num-i-1):
			if(process[j][1]>process[j+1][1]):
				swap(process,j,j+1)
	

def update_completion_time(process,num,time):
	for i in range(num):
		if(process[i][6]!=1):
				process[i][3]+=time


def HRRN(process,num):
	sum_bt=0
	
	print("\nBefore Arrange...\n")
	print("Process ID\tArrival Time\tBurst Time\n")
	
	for i in range(num):
		print(process[i][0],"\t\t",process[i][1],"\t\t",process[i][2])
		sum_bt+=process[i][2]
		
	sort_arrival_time(process,num)
	print("\n")
	
	t=0
	completion_time=0
	print("\nAfter Arrange...\n")
	print("Process ID\tCompletion Time\n")
	
	seq=[]
	while(t<sum_bt):
		hrr=-1
		flag=0
		for i in range(num):
			if(process[i][6]!=1):
				if(completion_time>=process[i][1]):
					flag=1
					temp=float(float((completion_time-process[i][1])+process[i][2])/process[i][2])
					if(temp>hrr):
						hrr=temp
						loc=i
		if(flag==0):
			i=0
			while(i<num):
				if(process[i][6]!=1):
					break
				i=i+1
			time=process[i][1]-completion_time
			update_completion_time(process,num,time)
			completion_time+=time
			print(-1,"\t\t",completion_time)
			seq.append([-1,time])			
		else:
			t+=process[loc][2]
			completion_time+=process[loc][2]
			process[loc][4]=completion_time-process[loc][1]-process[loc][2]
			process[loc][5]=completion_time-process[loc][1]
			update_completion_time(process,num,process[loc][2])
			process[loc][6]=1
			print(process[loc][0],"\t\t",process[loc][3])
			seq.append([process[loc][0],process[loc][2]])
	print(seq)
	return seq

def SJF (process,num):
	print("\nBefore Arrange...\n")
	print("Process ID\tArrival Time\tBurst Time\n")
	
	for i in range(num):
		print(process[i][0],"\t\t",process[i][1],"\t\t",process[i][2])
	
	arrange_arrival_time(process,num)
	arrange_completion_time(process,num)
	completion_time=0
	print("\nAfter Arrange...\n")
	print("Process ID\tCompletion Time\n")
	
	i=0
	seq=[]
	while(i<num):
		if(process[i][1]<=completion_time):
			print(process[i][0],"\t\t",process[i][3])
			completion_time=process[i][3]
			seq.append([process[i][0],process[i][2]])
			i=i+1
		else:
			print(-1,"\t\t",process[i][1])
			completion_time=process[i][1]
			seq.append([-1,process[i][1]])
	return seq
	

#process=[[1,6,1,0,0,0],[2,3,3,0,0,0],[3,4,6,0,0,0],[4,1,5,0,0,0],[5,2,2,0,0,0],[6,5,1,0,0,0]]



