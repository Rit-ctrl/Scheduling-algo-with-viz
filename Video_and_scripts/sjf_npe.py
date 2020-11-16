from manimlib.imports import *
import os
import pyclbr

class SJF_NPE(ThreeDScene):
    
    def construct(self):

        heading=TextMobject("SJF NPE ")
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
    #processes=[[1,3,2],[2,2,4],[3,6,3],[4,8,1],[5,4,3],[6,5,4]] #[process_id,arrival time,burst_time]
    processes=[[1,6,1],[2,3,3],[3,4,6],[4,1,5],[5,2,2],[6,5,1]]
    num=len(processes)

    for i in range(num):
        a=[]
        a.append(int(0))
        a.append(int(0))
        a.append(int(0))
        processes[i].extend(a)
    seq=SJF(processes,num)
    return processes,seq

   
def swap(process,i,j):
	for k in range(6):
		process[i][k], process[j][k]=process[j][k], process[i][k]


def arrange_arrival_time(process,num):
	process.sort(key=lambda x: x[1])


def arrange_completion_time(process,num):
	process[0][3]=process[0][1]+process[0][2]  #Completion Time = Arrival Time + Burst Time
	process[0][5]=process[0][3]-process[0][1]  #Turnaround Time = Completion Time - Arrival Time
	process[0][4]=process[0][5]-process[0][2]  #Waiting Time = Turnaround Time - Burst Time
	completion_time=process[0][3]
	i=1
	while(i<num):
		temp=process[i-1][3]
		low=process[i][2]
		
		j=i
		val=i
		while(j<num):
			if(temp>=process[j][1]):
				if(low>process[j][2]):
					low=process[j][2]
					val=j
				elif(low==process[j][2]):
					if(process[val][1]>process[j][1]):
						low=process[j][2]
						val=j					
			
			j=j+1
		
		x=process[val][1]-completion_time
		if(x<=0):
			x=0	
		
		process[val][3]=temp+process[val][2]+x  #Completion Time = Arrival Time + Burst Time
		completion_time=process[val][3]
		process[val][5]=process[val][3]-process[val][1]  #Turnaround Time = Completion Time - Arrival Time
		process[val][4]=process[val][5]-process[val][2]  #Waiting Time = Turnaround Time - Burst Time
		
		swap(process,val,i)
		i=i+1


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



