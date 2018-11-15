#! -*- coding:utf-8 -*-
import os
import sys

class AbstractDouyinSign(object):
    def work(self, url):
        pass

'''
    使用在线服务生成签名
'''
class OnlineDouyinSign(AbstractDouyinSign):
    def __init__(self):
        pass
    
    def work(self, url):
        return url
    
    
        
     
'''
    离线服务生成签名, 算法只分析签名逻辑, 暂不提供key
'''
class OfflineDouyinSign(AbstractDouyinSign):
    def __init__(self, HK1, HK2, HK3, HK4):
        self.HIDDEN_KEY1 = HK1
        self.HIDDEN_KEY2 = HK2
        self.HIDDEN_KEY3 = HK3
        self.HIDDEN_KEY4 = HK4
    
   `'''
        com.ss.android.common.applog.k.a(byte[] barr) 方法
    '''
    def evident_6041(self, input_bytes):
        if input_bytes is None:
            return None
        else:
            pass
            
        
    '''
        libcms.so sub_26750逻辑
    '''
    def sub_26750(self, ts, arr, devid):
        pass
    
    
    '''
        libcms.so sub_2f1c8逻辑
    '''
    def sub_2f1c8(self, barr):
        pass
    
    
    '''
        生成最终的带签名url
    '''
    def work(self, url, param):
        pass
    
 

class DouyinSDK(object):
    
    def __init__(self, signer):
        self.signer = signer
        
    
    
