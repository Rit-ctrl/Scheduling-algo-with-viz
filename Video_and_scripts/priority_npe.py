from manimlib.imports import *
import os
import pyclbr

class priority(ThreeDScene):
    
    def construct(self):

        heading=TextMobject("PRIORITY NPE")
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
    processes=[[1,3,2,1],[2,1,4,2],[3,6,3,3],[4,8,1,4],[5,4,3,5],[6,5,4,6]]
    processes,seq=findWaitingTime(processes)
    return processes,seq

# Python code to sort the tuples using second element 
# of sublist Inplace way to sort using sort() 
def Sort(sub_li, index, rev): 

	# reverse = None (Sorts in Ascending order) 
	# key is set to sort using second element of 
	# sublist lambda has been used 
	sub_li.sort(key = lambda x: x[index], reverse=rev) 
	return sub_li 

def maxIndex(li):
    if(len(li)>0):
        return li.index(max(li, key = lambda x : x[3]))
    else:
        return 0


seq = []
time = 0

# Function to find the waiting 
# time for all processes

def findWaitingTime(processes):
    Sort(processes,1,False)
    print(processes)

    empty = 1

    if processes[0][1]==0:
        time = 0
    else:
        empty = 0
        time = processes[0][1]
    
    dummy = processes
    Sort(dummy,3,True)

    if(empty==0):
        seq.append([-1,time])

    for i in range(0,len(processes)):
        j = 0
        while(dummy[j][1] > time):
            j += 1
        
        seq.append([dummy[j][0],dummy[j][2]])
        time += dummy[j][2]
        dummy.pop(j)

    print(seq)
    return processes,seq
    
        
                        



