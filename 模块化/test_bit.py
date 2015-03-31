# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:11:09 2015

@author: 旋宇
"""

from decrypt import *

def test_bit(m,c,p):
    '''测试单个bit加密正确性
    
    Args:
        m:plaintext
        c:ciphertext
        p:secret key
    Returns:
        Display Whether the decryption of m
        is right
    '''
    rlt = decrypt(c,p)
    if  rlt == m:
        print "单bit",m,"测试成功！"
    