import numpy as np
import matplotlib.pyplot as mpl

##Esto simula un escalon
def escalon(ts,a,k):
    x=[]
    for t in ts:
        if t<k:
            x.append(0)
        else:
            x.append(a)
    return x

def seno(ts,a,f,theta):
    x=[]
    for t in ts:
        x.append(a*np.sin((2*np.pi*f*t)+theta))
    return x

def suma(s1,s2):
    x=[]
    for x1,y1 in zip(s1,s2):
        x.append(x1+y1)
    return x


def main(ini,fin,delta):
    ts=np.arange(ini,fin,delta)
    s1=seno(ts,-2/np.pi,2.5,0)
    s2=seno(ts,1/np.pi,5,0)
    s3=seno(ts,-3/(3*np.pi),7.5,0)
    s4=seno(ts,1/(2*np.pi),10,0)
    s5=seno(ts,-2/(5*np.pi),12.5,0)
    s6=seno(ts,1/(3*np.pi),15,0)
    s7=seno(ts,-2/(7*np.pi),17.5,0)
    tmp1=suma(s1,s2)
    tmp2=suma(tmp1,s3)
    tmp3=suma(tmp2,s4)
    tmp4=suma(tmp3,s5)
    tmp5=suma(tmp4,s6)
    x=suma(tmp5,s7)
    mpl.plot(ts,x)
    mpl.plot(ts,s1)
    mpl.plot(ts,s2)
    mpl.plot(ts,s3)
    mpl.plot(ts,s4)
    mpl.plot(ts,s5)
    mpl.plot(ts,s6)
    mpl.plot(ts,s7)
    mpl.grid()
    mpl.title('Aproximando X(T)')
    mpl.xlabel('Tiempo')
    mpl.ylabel('Respuesta')
    mpl.savefig('Proyecto_6.png',format='png',dpi=300)
    mpl.show()

if __name__ == '__main__':
    main(-0.2,0.2,0.01)