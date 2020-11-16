from manimlib.imports import *
import os
import pyclbr

class RR(ThreeDScene):
    
    def construct(self):

        heading=TextMobject("Round robin")
        heading.to_edge(UP+LEFT)
        self.play(Write(heading),run_time=2)

        time=0
        p,seq,q=sim()

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
                self.play(Write(text1[i].scale(0.8)))

            
                
                self.play(Transform(r_text,TextMobject("Ready queue "+str(rq[i])).to_corner(RIGHT+UP).scale(0.5)))
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
    processes=[[1,3,2],[2,2,4],[3,6,3],[4,8,1],[5,4,3],[6,5,4]] #[process_id,arrival time,burst_time]
    processes,seq,q=calcwaitingtime(processes,len(processes),2)
    return processes,seq,q

def calcwaitingtime(processes,n,quantum):
    rem_time=[0]*n
    seq=[]
    #print(seq)
    
 
    processes.sort(key=index)

    for i in range(n):  
      rem_time[i] = processes[i][2] 

    t=0
    arrival=0
    q=[]

    rq=[]
    while True:
        done = True
        check = False
        last_guy=-1
        for i in range(n):
            if rem_time[i]>0:
                done=False
                #print("hi")
                if processes[i][1] <= t: #check if process should be in rq or not
                    if(check==False):    # check if some process hasn't already eaten up this time quantum
                        if len(rq) == 0 or rq[0]==processes[i][0]: #if rq is empty or rq head is process i
                            if(rem_time[i]>quantum):
                                t+=quantum
                                rem_time[i]-=quantum
                                seq.append([processes[i][0],quantum])
                                last_guy=processes[i][0]
                                #rq.append(i)
                            else:
                                t+=rem_time[i]
                                seq.append([processes[i][0],rem_time[i]])
                                rem_time[i]=0
                            if(len(rq)>1):
                                rq.remove(processes[i][0])
                            check=True
                    else:
                        if processes[i][0] not in rq: 
                            rq.append(processes[i][0])
        #print("iter ")
        if done == True:
            print("op")
            print(seq)
            print(q)
            return processes,seq,q
            #break
        if last_guy !=-1:
            rq.append(last_guy)
        
        q.append(rq[:])
        

        if len(rq)==0:
            seq.append([-1,quantum])
            t+=quantum

        
                        




              

# if __name__ == '__main__':
    
#     #calcwaitingtime(processes,len(processes),2) #time quantum 2
#     t=RR()
#     #t.construct(processes,len(processes))


