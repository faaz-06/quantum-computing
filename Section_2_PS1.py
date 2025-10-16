from math import *
from cmath import *
from random import *
H=[[1/sqrt(2),1/sqrt(2)],[1/sqrt(2),-1/sqrt(2)]]
X=[[0,1],[1,0]]
Y=[[0,-1j],[1j,0]]
Z=[[0,-1],[1,0]]
S=[[1,0],[0,1j]]
T=[[1,0],[0,1/sqrt(2)+1j/sqrt(2)]]
zero=[1,0]
one=[0,1]
def Hadamard(qubit):
    hdmr=[H[0][0]*qubit[0]+ H[0][1]*qubit[1], H[1][0]*qubit[0]+ H[1][1]*qubit[1]]
    return hdmr
def sgate(qubit):
    s=[S[0][0]*qubit[0]+ S[0][1]*qubit[1], S[1][0]*qubit[0]+ S[1][1]*qubit[1]]
    return s
def tgate(qubit):
    t=[T[0][0]*qubit[0]+ T[0][1]*qubit[1], T[1][0]*qubit[0]+ T[1][1]*qubit[1]]
    return t
def xgate(qubit):
    x=[X[0][0]*qubit[0]+ X[0][1]*qubit[1], X[1][0]*qubit[0]+ X[1][1]*qubit[1]]
    return x
def ygate(qubit):
    y=[Y[0][0]*qubit[0]+ Y[0][1]*qubit[1], Y[1][0]*qubit[0]+ Y[1][1]*qubit[1]]
    return y
def tensor_prod(q1,q2):
    prod=[a*b for a in q1 for b in q2]
    return prod
def quantumregister(n):
    state=[1+0j] + [0+0j]*(2**n - 1)
    return state
def cxgate(state, control, target, n):
    N = 2**n
    newstate = state.copy()
    for i in range(N):
        control_bit=(i//(2**control))%2
        target_bit=(i//(2**target))%2
        if control_bit==1 and target_bit==0:
            j = i + (2**target)   
            newstate[i], newstate[j] = newstate[j], newstate[i]
    return newstate
    
def cygate(state, control, target, n):
    N = 2**n
    newstate = state.copy()
    for i in range(N):
        control_bit=(i//(2**control))%2
        target_bit=(i//(2**target))%2
        if control_bit==1:
            if target_bit==0:
                j=i+(2**target)
                new_state[i]=0
                new_state[j]=1j*state[i]
            else:
                j=i-(2**target)
                newstate[i]=0
                newstate[j]+=-1j*state[i]
    return new_state


def single_qubit_gate(state, gate, target, n):
    newstate = state.copy()
    N=2**n  
    x=2**target
    for a in range(0, N, 2*x):      
        for b in range(x):      
            i = a + b
            j = i + x
            a0 = state[i]
            a1 = state[j]
            newstate[i] = gate[0][0]*a0 + gate[0][1]*a1
            newstate[j] = gate[1][0]*a0 + gate[1][1]*a1
    return newstate



def showstate(state, n, threshold=1e-10):
    for i, amp in enumerate(state):
        if abs(amp)>threshold:
            print(f"|{format(i, 'b').zfill(n)}> : {amp}")

def measure(state):
    probs=[abs(a)**2 for a in state]
    r=random()
    c=0
    for i, p in enumerate(probs):
        c+=p
        if r<c:
            result=format(i, 'b').zfill(int(round(log2(len(state)))))
            collapsed=[0]*len(state)
            collapsed[i]=1
            return result, collapsed


