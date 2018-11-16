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
    
    
        

class DouyinSDK(object):
    
    def __init__(self, signer):
        self.signer = signer
        
    
    
