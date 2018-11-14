# -*- coding: utf-8 -*-

"""
    抖音2.0之前的as, cp加密算法与协议, 本代码仅用于研究之用, HIDDEN_KEY具体值 请联系QQ: 3106195629 获取
    老版本价值不大, 不推荐研究使用
"""
import hashlib

class calcSig(object):
    key1 = 'HIDDEN_KEY1'
    key2 = 'HIDDEN_KEY2'
    rstr = 'HIDDEN_KEY3'

    def shuffle(self, p1, p2):
        p = ''
        p += p1[int(p2[0], 10) - 1]
        p += p1[int(p2[1], 10) - 1]
        p += p1[int(p2[2], 10) - 1]
        p += p1[int(p2[3], 10) - 1]
        p += p1[int(p2[4], 10) - 1]
        p += p1[int(p2[5], 10) - 1]
        p += p1[int(p2[6], 10) - 1]
        p += p1[int(p2[7], 10) - 1]
        return p.lower()

    # 生成 as和cp字段
    def ppp(self, u_md5, u_key1, u_key2):
        ascp = [0] * 36
        ascp[0] = 'a'
        ascp[1] = '1'
        for i in range(0, 8):
            ascp[2 * (i + 1)] = u_md5[i]
            ascp[2 * i + 3] = u_key2[i]
            ascp[2 * i + 18] = u_key1[i]
            ascp[2 * i + 1 + 18] = u_md5[i + 24]
        ascp[-2] = 'e'
        ascp[-1] = '1'

        return ''.join(ascp)

    # 解析url参数
    def parseURL(self, url):
        param_index = url.find('?')
        param = url[param_index + 1:]
        param_list = param.split('&')
        param_list.append('rstr='+self.rstr)
        param_list = sorted(param_list)
        result = ''
        for a in param_list:
            tmp = a.split('=')
            tmp[1] = tmp[1].replace('+', 'a')
            tmp[1] = tmp[1].replace(' ', 'a')
            result += tmp[1]
        return result

    # 计算md5
    def calcMD5(self, str_encode):
        m = hashlib.md5()
        m.update(str_encode.encode('utf-8'))
        return m.hexdigest()

    def work(self, url, curtime):
        url_param = self.parseURL(url)
        p_md5 = self.calcMD5(url_param)
        if curtime & 1:
            p_md5 = self.calcMD5(p_md5)
        hexTime = hex(curtime)[2:]
        aa = self.shuffle(hexTime, self.key1)
        bb = self.shuffle(hexTime, self.key2)
        sig = self.ppp(p_md5, aa, bb)
        return ('%s&as=%s&cp=%s' % (url, sig[:18], sig[18:]))
        # return (sig[:18], sig[18:])

    
def main():
    c = calcSig()
    url = '/aweme/v1/comment/list/?aweme_id=6506468984865426696&cursor=0&count=20&comment_style=2&ts=1516946960&app_type=normal&os_api=23&device_type=HUAWEI NXT-AL10&device_platform=android&ssmix=a&iid=22634572655&manifest_version_code=166&dpi=480&uuid=863336037384660&version_code=166&app_name=aweme&version_name=1.6.6&openudid=3f4f9a09bd6ea55e&device_id=46408460323&resolution=1080*1812&os_version=6.0&language=zh&device_brand=HUAWEI&ac=wifi&update_version_code=1662&aid=1128&channel=aweGW&_rticket=1516946961275'
    t = 1516946960
    print(c.work(url,t))


if __name__ == "__main__":
    main()
