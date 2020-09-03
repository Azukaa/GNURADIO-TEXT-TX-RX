# this module will be imported in the into your flowgraph

# this module will be imported in the into your flowgraph
import numpy as np
def pamampt(sps, ptype, pparms= []):
    if ptype == "rect":
        nn = np.arange(sps)
        pt = np.ones(len(nn))

    elif ptype == 'tri':
        nn = np.arange(-sps, sps)
        pt = 1 + nn/float(sps)
        ix = np.where(nn>=0)[0]
        pt[ix] = 1 - nn[ix]/float(sps)

    elif ptype == 'sinc':
        k = 5 # default k
        if len(pparms) > 0:
            k = pparms[0]
        nk = round(k*sps)
        nn = np.arange(-nk, nk)
        pt = np.sinc(nn/float(sps))
        if len(pparms) > 1:
            pt = pt * np.kaiser(len(pt), pparms[1])

    elif ptype=='rrcf':
        # Root raised cosine in freq
        nk = round(pparms[0]*sps)
        nn = np.arange(-nk,nk)
        alfa = pparms[1]
        # Rolloff parameter
        atFB = pparms[1]/float(sps)*nn
        atFB2 = np.power(4*atFB,2.0)
        falf =  4*alfa/float(sps) #4*alfa*FB
        pt = (1-alfa+4*alfa/np.pi)*np.ones(len(nn))
        ix = np.where(np.logical_and(nn!=0,atFB2!=1.0))[0]
        pt[ix] = np.sin((1-alfa)*np.pi/float(sps)*nn[ix])
        pt[ix] = pt[ix]+falf*nn[ix]*np.cos((1+alfa)*np.pi/float(sps)*nn[ix])
        pt[ix] = float(sps)/(np.pi)*pt[ix]/((1-np.power(falf*nn[ix],2.0))*nn[ix])
        ix = np.where(atFB2 == 1.0)[0]
        pt[ix] = (1+2/np.pi)*np.sin(np.pi/(4*alfa))+(1-2/np.pi)*np.cos(np.pi/(4*alfa))
        pt[ix] = alfa/np.sqrt(2.0)*pt[ix]
            
    elif ptype == "rcf":
        nk = round(pparms[0]*sps)
        nn = np.arange(-nk,nk)
        pt = np.sinc(nn/float(sps))
        if len(pparms) > 1:
            p2t = 0.25 * np.pi*np.ones(len(nn))
            atFB = pparms[1]/float(sps)*nn
            atFB2 = np.power(2*atFB,2.0)
            ix = np.where(atFB2 != 1) [0]
            p2t[ix] = np.cos(np.pi*atFB[ix])
            p2t[ix] = p2t[ix]/(1-atFB2[ix])
            pt = pt*p2t
        else:
            pt = np.ones(1) # Default value
    return pt

    

def pamhRt(sps,ptype,pparms = []):
    pt = pamampt(sps,ptype,pparms)
    hRt = pt[::-1]  # h_R(t) = p(-t)
    hRt = 1.0/sum(np.power(pt,2.0)) * hRt
    return hRt





