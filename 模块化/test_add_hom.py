# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:31:56 2015

@author: 旋宇
测试加法同态
decrypt(c1 + c2) = m1 + m2
"""

from decrypt  import *

def test_add_hom(add_m,a,b,p):#参数为两个密文
    '''将两个密文相加
    
    Args:
        a,b:ciphertext
        add_m:the addition of plaintext
        p:secrec key
    Returns:
        display the result of test
    '''
    print "密文相加为：",a + b
    if decrypt(a+b,p) == add_m % 2:
        print "加法同态测试通过！"
    else:
        print "加法同态测试失败！"