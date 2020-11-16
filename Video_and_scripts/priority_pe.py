from manimlib.imports import *
import os
import pyclbr

class RR(ThreeDScene):
    
    def construct(self):

        heading=TextMobject("Priority PE")
        heading.to_edge(UP+LEFT)
        self.play(Write(heading),run_time=2)

        
        p,seq,q=sim()
        self.animate(heading,seq,q)

    def animate(self,heading,seq,q):

        time=0
        text1=[]
        text2=[]
        clk=TextMobject("time ={}".format(str(time)))
        clk.next_to(heading,DOWN,buff=0.5)
        clk.scale(0.8)
        self.add(clk)
        self.play(Write(clk))
        r_text=TexMobject("Ready queue")
        r_text.to_corner(RIGHT+UP)
        r_text.scale(0.5)

        rq=q
        
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
                self.play(Transform(clk,TextMobject("time ={}".format(str(time))).next_to(heading,DOWN,buff=0.5).scale(0.8)))
                self.play(Write(text1[i]))

            
                
                self.play(Transform(r_text,TextMobject("Ready queue "+str(rq[time-1])).to_corner(RIGHT+UP).scale(0.5)))
                #print(r)
                #print("\n")                   
                counter+=1
                

            self.play(Write(text2[i]))
            #self.move_camera(frame_center=[2,0,0])     
            #self.move_camera(frame_center=(0,0,0))
            self.wait(2)

def index(e):
    return e[1]
def priority(e):
    return e[3]

def sim():
    processes=[[1,1,4,4],[2,2,2,5],[3,2,3,7],[4,3,5,8],[5,3,1,5],[6,4,2,6]] #[process_id,arrival time,burst_time,pr]
    #processes=[[1,1,4,5],[2,2,5,2],[3,3,6,6],[4,0,1,4],[5,4,2,7],[6,5,3,8]]
    seq,q=calcwaitingtime(processes,len(processes))
    
    print(seq)
    print(q)
    return processes,seq,q

def calcwaitingtime(processes,n):
    
    seq=[]
    rq=[]
    q=[]
    #sort based on arrival time
    processes.sort(key=index)
    time=0
    ptr=0
    done=0
    while done!=n: # execute until all processes are done
        for i in range(ptr,n,1): #add all processes which have arrived 
            if(processes[i][1]<=time):
                q.append(processes[i])
                ptr+=1
        if len(q)==0: #if no process has arrived
            if len(seq)>0 and seq[-1][0]==-1:
                seq[-1][1]+=1
            else:
                seq.append([-1,1])
            rq.append([])
        else:
             # sort processes based on priority ; higher no higher priority
            q.sort(key=priority,reverse=True)
            
            if len(q)>1:
                l=[]
                for i in range(1,len(q)):
                    l.append(q[i][0])
                rq.append(l)
            else:
                rq.append([])    
            
            q[0][2]+=-1
            
            if len(seq)!=0 and seq[-1][0]==q[0][0]:
                seq[-1][1]+=1
            else:
                seq.append([q[0][0],1])
            
            if(q[0][2]==0):
                q.pop(0)
                done+=1
            
        time+=1
        #print(time,q,seq)
    return seq,rq

if __name__=="__main__":
    sim()