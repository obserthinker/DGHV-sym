# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:20:29 2015

@author: 旋宇
解密单{0，1}的密文测试
算法为 m = (c mod p) mod 2
"""

def decrypt(c,p):
    '''decrypt ciphertext
    
    Args:
        c:ciphertext
        p:secrec key
    Returns:
        plaictext:plaintext
    '''
    plaintext = (c % p) % 2
    print "plaintext = ", plaintext
    return plaintext



