# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:14:17 2015

@author: 旋宇
加密
算法为 c = p*q + 2r + m
"""

from parameter import *

def encrypt(p,q,eta,m):
    '''加密明文
    
    Args:
        p:secret key
        q:times p
        eta:seurity parameter
        m:plaintext
    Retuens:
        c:ciphertext
    '''
    r = GenR(eta, p)
    print "其中噪音为：r = ", r
    c = p * q + 2 * r + m
    print "c = ",c
    return c
    
