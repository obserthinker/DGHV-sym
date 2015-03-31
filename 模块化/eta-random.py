# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:14:08 2015

@author: 旋宇
"""

from random import *
from parameter import *
from encrypt import *
from decrypt import *
from test_bit import *
from test_add_hom import *
from test_multi_hom import *

'''
参数设置
eta p q r
'''
print "*****************************************"
print "参数设置"
#eta为密钥参数，控制密钥大小，范围为[2^(eta-1),2^eta）
eta = 5 #[16,32) eta最好大于等于6
print "eta = %r\n"%(eta) 

p = GenP(eta)
q = GenQ(eta)
r = GenR(eta, p)

print "参数设置结束"


print "*****************************************\n"

#对明文 m 加密
m0 = 0
m1 = 1
c0 = encrypt(p,q,eta,m0)
c1 = encrypt(p,q,eta,m1)
print "加密结束"


print "*****************************************\n"
#单bit解密测试
print "单bit加密后解密测试"

test_bit(m0,c0,p)
test_bit(m1,c1,p)

print "*****************************************\n"
#加法同态测试
print "加法同态测试"
test_add_hom(m0+m1,c0,c1,p)
test_add_hom(m1+m1,c1,c1,p)
test_add_hom(m0+m0,c0,c0,p)

print "*****************************************\n"
#测试乘法同态
print "乘法同态测试"
test_multi_hom(m0*m1,c0, c1, p)
test_multi_hom(m1*m1,c1, c1, p)
test_multi_hom(m0*m0,c0, c0, p)