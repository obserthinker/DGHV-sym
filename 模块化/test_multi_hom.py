# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:34:54 2015

@author: 旋宇
"""

from decrypt import *

def test_multi_hom(prd_of_m,c0,c1,p):
    '''测试乘法同态
    
    Args:
        prd_of_m:the product of plaintext
        c0,c1:ciphertexts
        p:secret kry
    Returns:
        the result of test
    '''
    prd_of_c = c0 * c1

    if decrypt(prd_of_c,p) == prd_of_m % 2:
        print "乘法同态通过！"
    else:
        print "乘法同态失败！"

print "*****************************************\n"