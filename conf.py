# -*- coding: utf-8 -*-


"""
五行对照表：
甲(木) 乙(木) 丙(火) 丁(火) 戊(土) 己(土) 庚(金) 辛(金) 壬(水) 癸(水)
子(水) 丑(土) 寅(木) 卯(木) 辰(土) 巳(火) 午(火) 未(土) 申(金) 酉(金) 戌(土) 亥(水)
"""


# 十大天干
tailnum = [4, 5, 6, 7, 8, 9, 0, 1, 2, 3] # 年代尾数
tiangan = [u'甲', u'乙', u'丙', u'丁', u'午', u'己', u'庚', u'辛', u'壬', u'癸']

# 十二地支
remainder = [4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3] # 年代除以12的余数
dizhi = [u'子', u'丑', u'寅', u'卯', u'辰', u'巳', u'午', u'未', u'申', u'酉', u'戌', u'亥']


def cal_year(year):
    _tiangan = tiangan[tailnum.index(year % 10)]
    _dizhi = dizhi[remainder.index(year % 12)]
    return u'%s：%s%s年' % (year, _tiangan, _dizhi)


if __name__ == '__main__':
    print cal_year(2012)
