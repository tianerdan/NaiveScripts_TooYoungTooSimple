import numpy as npy
#from scipy import integrate
import matplotlib.pyplot as plt

def Rayleigh_Plesset(t_begin,t_end,err):
    # 有限差分法求解Rayleigh–Plesset方程
    #*#########常数
    R0=5*1e-6 #8*1e-7
    P0=1e+5
    Pa=4*1e+5 # 
    Sigma=7.275*1e-2 # 液体表面张力系数，这里选取水的
    #f1=15*1e+6
    #f2=4.8*1e+6
    Rho=1*1e+3 # 液体密度
    #Omega=2*np.pi/f
    Gamma=1 # 气体压缩率
    Omega=R0/npy.sqrt(3*Gamma/Rho*(P0+2*Sigma/R0)) # 气泡的共振频率
    #*##########
    E=2*err
    R_len=1
    temp=[-1]
    while E>err:
        R_len*=2
        h=(t_end-t_begin)/R_len
        R=npy.ones(R_len)
        R[0]=R0
        R[1]=R0+6*h*Sigma/(Rho*R0**2)
        for i in range(1,R_len-1):
            R[i+1]=(6*R[i]-3*R[i-1]-2*R[i]**2*R[i-1]+2*R[i]**3+2*h**2/Rho*((P0+2*Sigma/R[i])*((R0/R[i])**3-1)+Pa*npy.sin(Omega*h*i)))/(3+2*R[i]**2-2*R[i-1]*R[i])
        #E=npy.abs(deltaF).max()
        E=npy.abs(temp-R[-1])
        temp=R[-1]
        print(E)
    return (R,R_len)

#*模拟0.25s，可以续1s
t_begin=0
t_end=0.25
(R,R_len)=Rayleigh_Plesset(t_begin,t_end,1e-2)
t=npy.linspace(t_begin,t_end,R_len)
#plt.plot(t,R/R[0],color='black')
#plt.ylabel(r"Radius $\frac{R}{R_0}$")
plt.plot(t,R,color='black')

'''R1,R_len1=Rayleigh_Plesset(t_begin,t_end,1e-2)
t1=npy.linspace(t_begin,t_end,R_len1)
plt.plot(t1,R1,color='blue')'''

plt.ylabel(r"Radius $R$")
plt.xlabel("time")

#title='$R='+str(R[0])+'$ and $\dot{R_0}=0$'
title='$R='+str(R[0])+'$'
plt.title(title)
#plt.show()
plt.savefig('R='+str(R[0])+'.pdf',transparent=True)
