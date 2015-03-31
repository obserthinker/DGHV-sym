# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:58:12 2015

@author: 旋宇
"""

from random import *


def GenP(eta):
    '''随机生成密钥

    描述：通过给定的安全参数eta，生成在[2^(eta - 1) + 1, 2^eta)
    范围内的奇整数p作为密钥
    Args:
        eta:安全参数
    returns：
        p:secret key
    '''
    if 2**(eta-1) > 18:
        print 2**(eta-1)
        print "p is choosen from ",range(2**(eta - 1) + 1, 2**eta, 2)
        p = randrange(2**(eta - 1) + 1, 2**eta, 2)
    else:
        print 18
        print "p is choosen from ",range(19, 2**eta, 2)  
        p = randrange(19, 2**eta, 2)
    print "p = %r\n"%(p)
    return p


def GenR(eta, p):
    '''随机生成噪音
    
    产生加密时的噪音
    Args:
        eta:安全参数
        p:密钥
    Returns:
        r:噪音
    '''
    #r 为噪音，且满足r< (p-2)/4以保证解密成功
    print "r is choosen form %r"%(range(1,(p-2)//8+1/2,1))
    r = randrange(1,(p-2)//8+1/2,1)
    print "r = %r\n"%(r)
    return r

def GenQ(eta):
    '''产生密钥的倍数
    
    长生掩盖密钥用的倍数q
    Agrs:
        eta:安全参数
    Returns:
        q:c = qp + 2r + m
    '''
    #文献中 q 选取为值约为2^(eta^3)
    #q = 2**(eta**3)
    q = randrange(2**(eta+1),2**(eta+2))
    print "q = %r\n"%(q)
    return q
