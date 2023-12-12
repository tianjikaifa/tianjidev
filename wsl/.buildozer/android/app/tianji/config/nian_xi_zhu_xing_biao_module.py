#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/13 22:45
# @Author  : huangfujue
# @File    : nian_xi_zhu_xing_biao_module.py
# @Date    : 2023/11/13 
"""
根据年干确定星耀位置，
根据年干确定四化星是什么星耀
根据年支确定星耀

"""

# ----------------------------------------------------------------------------------------------------------------------
from tianji.config.shi_er_di_zhi_biao_module import di_zhi, Di_Zhi_Iter
from tianji.config.ming_gong_shen_gong_module import Ming_Shen_Gong
from tianji.config.yu_gong_biao_module import Yu_Gong

# 根据年干确幸星耀位置
nian_gan_xing_biao = {
    "甲": {
        "禄存": "寅",
        "擎羊": "卯",
        "陀罗": "丑",
        "天魁": "丑",
        "天钺": "未",
        "天官": "未",
        "天福": "酉",
        "天厨": "巳",
    },
    "乙": {
        "禄存": "卯",
        "擎羊": "辰",
        "陀罗": "寅",
        "天魁": "子",
        "天钺": "申",
        "天官": "辰",
        "天福": "申",
        "天厨": "午",
    },
    "丙": {
        "禄存": "巳",
        "擎羊": "午",
        "陀罗": "辰",
        "天魁": "亥",
        "天钺": "酉",
        "天官": "巳",
        "天福": "子",
        "天厨": "子",
    },
    "丁": {
        "禄存": "午",
        "擎羊": "未",
        "陀罗": "巳",
        "天魁": "亥",
        "天钺": "酉",
        "天官": "寅",
        "天福": "亥",
        "天厨": "巳",
    },
    "戊": {
        "禄存": "巳",
        "擎羊": "午",
        "陀罗": "辰",
        "天魁": "丑",
        "天钺": "未",
        "天官": "卯",
        "天福": "卯",
        "天厨": "午",
    },
    "己": {
        "禄存": "午",
        "擎羊": "未",
        "陀罗": "巳",
        "天魁": "子",
        "天钺": "申",
        "天官": "酉",
        "天福": "寅",
        "天厨": "申",
    },
    "庚": {
        "禄存": "申",
        "擎羊": "酉",
        "陀罗": "未",
        "天魁": "丑",
        "天钺": "未",
        "天官": "亥",
        "天福": "午",
        "天厨": "寅",
    },
    "辛": {
        "禄存": "酉",
        "擎羊": "戌",
        "陀罗": "申",
        "天魁": "午",
        "天钺": "寅",
        "天官": "酉",
        "天福": "巳",
        "天厨": "午",
    },
    "壬": {
        "禄存": "亥",
        "擎羊": "子",
        "陀罗": "戌",
        "天魁": "卯",
        "天钺": "巳",
        "天官": "戌",
        "天福": "午",
        "天厨": "酉",
    },
    "癸": {
        "禄存": "子",
        "擎羊": "丑",
        "陀罗": "亥",
        "天魁": "卯",
        "天钺": "巳",
        "天官": "午",
        "天福": "巳",
        "天厨": "亥",
    },
}

# 根据年干确定四化星是什么
si_hua_xing_biao = {
    "甲": {
        "化禄": "廉贞",
        "化权": "破军",
        "化科": "武曲",
        "化忌": "太阳",
    },
    "乙": {
        "化禄": "天机",
        "化权": "天梁",
        "化科": "紫微",
        "化忌": "太阴",
    },
    "丙": {
        "化禄": "天同",
        "化权": "天机",
        "化科": "文昌",
        "化忌": "廉贞",
    },
    "丁": {
        "化禄": "太阴",
        "化权": "天同",
        "化科": "天机",
        "化忌": "巨门",
    },
    "戊": {
        "化禄": "贪狼",
        "化权": "太阴",
        "化科": "右弼",
        "化忌": "天机",
    },
    "己": {
        "化禄": "武曲",
        "化权": "贪狼",
        "化科": "天梁",
        "化忌": "文曲",
    },
    "庚": {
        "化禄": "太阳",
        "化权": "武曲",
        "化科": "太阴",
        "化忌": "天同",
    },
    "辛": {
        "化禄": "巨门",
        "化权": "太阳",
        "化科": "文曲",
        "化忌": "文昌",
    },
    "壬": {
        "化禄": "天梁",
        "化权": "紫微",
        "化科": "左辅",
        "化忌": "武曲",
    },
    "癸": {
        "化禄": "破军",
        "化权": "巨门",
        "化科": "太阴",
        "化忌": "贪狼",
    },
}

# 根据年支确定的星耀
nian_zhi_xing_biao = {
    "子": {
        "天马": "寅",
        "解神": "戌",
        "天哭": "午",
        "天虚": "午",
        "龙池": "辰",
        "凤阁": "戌",
        "红鸾": "卯",
        "天喜": "酉",
        "孤辰": "寅",
        "寡宿": "戌",
        "蜚廉": "申",
        "破碎": "巳",
        "天空": "丑",
        "月德": "巳"},
    "丑": {
        "天马": "亥",
        "解神": "酉",
        "天哭": "巳",
        "天虚": "未",
        "龙池": "巳",
        "凤阁": "酉",
        "红鸾": "寅",
        "天喜": "申",
        "孤辰": "寅",
        "寡宿": "戌",
        "蜚廉": "酉",
        "破碎": "丑",
        "天空": "寅",
        "月德": "午"},
    "寅": {
        "天马": "申",
        "解神": "申",
        "天哭": "辰",
        "天虚": "申",
        "龙池": "午",
        "凤阁": "申",
        "红鸾": "丑",
        "天喜": "未",
        "孤辰": "巳",
        "寡宿": "丑",
        "蜚廉": "戌",
        "破碎": "酉",
        "天空": "卯",
        "月德": "未"},
    "卯": {
        "天马": "巳",
        "解神": "未",
        "天哭": "卯",
        "天虚": "酉",
        "龙池": "未",
        "凤阁": "未",
        "红鸾": "子",
        "天喜": "午",
        "孤辰": "巳",
        "寡宿": "丑",
        "蜚廉": "巳",
        "破碎": "巳",
        "天空": "辰",
        "月德": "申"},
    "辰": {
        "天马": "寅",
        "解神": "午",
        "天哭": "寅",
        "天虚": "戌",
        "龙池": "申",
        "凤阁": "午",
        "红鸾": "亥",
        "天喜": "巳",
        "孤辰": "巳",
        "寡宿": "丑",
        "蜚廉": "午",
        "破碎": "丑",
        "天空": "巳",
        "月德": "酉"},
    "巳": {
        "天马": "亥",
        "解神": "巳",
        "天哭": "丑",
        "天虚": "亥",
        "龙池": "酉",
        "凤阁": "巳",
        "红鸾": "戌",
        "天喜": "辰",
        "孤辰": "申",
        "寡宿": "辰",
        "蜚廉": "未",
        "破碎": "酉",
        "天空": "午",
        "月德": "戌"},
    "午": {
        "天马": "申",
        "解神": "辰",
        "天哭": "子",
        "天虚": "子",
        "龙池": "戌",
        "凤阁": "辰",
        "红鸾": "酉",
        "天喜": "卯",
        "孤辰": "申",
        "寡宿": "辰",
        "蜚廉": "寅",
        "破碎": "巳",
        "天空": "未",
        "月德": "亥"},
    "未": {
        "天马": "巳",
        "解神": "卯",
        "天哭": "亥",
        "天虚": "丑",
        "龙池": "亥",
        "凤阁": "卯",
        "红鸾": "申",
        "天喜": "寅",
        "孤辰": "申",
        "寡宿": "辰",
        "蜚廉": "卯",
        "破碎": "丑",
        "天空": "申",
        "月德": "子"},
    "申": {
        "天马": "寅",
        "解神": "寅",
        "天哭": "戌",
        "天虚": "寅",
        "龙池": "子",
        "凤阁": "寅",
        "红鸾": "未",
        "天喜": "丑",
        "孤辰": "亥",
        "寡宿": "未",
        "蜚廉": "辰",
        "破碎": "酉",
        "天空": "酉",
        "月德": "丑"},
    "酉": {
        "天马": "亥",
        "解神": "丑",
        "天哭": "酉",
        "天虚": "卯",
        "龙池": "丑",
        "凤阁": "丑",
        "红鸾": "午",
        "天喜": "子",
        "孤辰": "亥",
        "寡宿": "未",
        "蜚廉": "亥",
        "破碎": "巳",
        "天空": "戌",
        "月德": "寅"},
    "戌": {
        "天马": "申",
        "解神": "子",
        "天哭": "申",
        "天虚": "辰",
        "龙池": "寅",
        "凤阁": "子",
        "红鸾": "巳",
        "天喜": "亥",
        "孤辰": "亥",
        "寡宿": "未",
        "蜚廉": "子",
        "破碎": "丑",
        "天空": "亥",
        "月德": "卯"},
    "亥": {
        "天马": "巳",
        "解神": "亥",
        "天哭": "未",
        "天虚": "巳",
        "龙池": "卯",
        "凤阁": "亥",
        "红鸾": "辰",
        "天喜": "戌",
        "孤辰": "寅",
        "寡宿": "戌",
        "蜚廉": "丑",
        "破碎": "酉",
        "天空": "子",
        "月德": "辰"},
}

"""
用来计算表示天寿星的位置的类，传入月份，时辰和年支
用来计算表示天才星和天寿星的位置
"""


class Tian_Cai_Tian_Show_xing:
    def __init__(self, yue, shi_zhi, nian_zhi):
        """
        根据月份，时辰和年支计算天才、天寿星位置

        :param yue:
        :param shi_zhi:表示时支
        :param nian_zhi:
        """
        ming_shen = Ming_Shen_Gong(yue, shi_zhi)
        self.shen_gong = ming_shen.shen

        self.yu_gong_iter = Yu_Gong(ming_shen.ming)  # 获取所有宫所在的位置
        self.__shi_zhi = shi_zhi
        self.__nian_zhi = nian_zhi
        self.__tian_cai_gong_biao = {
            "子": "命",
            "丑": "父母",
            "寅": "福德",
            "卯": "田宅",
            "辰": "事业",
            "巳": "友仆",
            "午": "迁移",
            "未": "疾厄",
            "申": "财帛",
            "酉": "子女",
            "戌": "夫妻",
            "亥": "兄弟"
        }

    def get_tian_cai_loaction(self):
        gong = self.__tian_cai_gong_biao.get(self.__nian_zhi)
        flag = True
        location = "子"
        for temp in di_zhi.values():
            yu_gong = self.yu_gong_iter.__getattribute__(temp)
            if yu_gong == gong:
                location = temp
                flag = False
                break
        if flag:
            raise Exception("为能找到天才星的位置，也许是参数错了，时辰是用1-12表示的")
        return location

    def get_tian_show_loaction(self):

        flag = True
        di_zhi_iter = Di_Zhi_Iter(-1)  # 从子开始

        for temp in di_zhi.values():

            if temp == self.shen_gong:
                flag = False
                break

            di_zhi_iter.next()

        if flag:
            raise Exception("未能找到天寿星的位置，也许是参数错了，时辰是用1-12表示的")
        return di_zhi_iter.now()


"""
用来表示截空位置
根据年干定下截空星在哪个位置，但是现在看不懂表格，
暂时先按这是两个星辰来看
"""


class Jie_Kong_Xing:
    def __init__(self, nian_gan):
        biao = {
            "甲": {
                "截路": "申",
                "空亡": "酉",
            },
            "乙": {
                "截路": "午",
                "空亡": "未",
            },
            "丙": {
                "截路": "辰",
                "空亡": "巳",
            },
            "丁": {
                "截路": "寅",
                "空亡": "卯",
            },
            "戊": {
                "截路": "子",
                "空亡": "丑",
            },
            "己": {
                "截路": "申",
                "空亡": "酉",
            },
            "庚": {
                "截路": "午",
                "空亡": "未",
            },
            "辛": {
                "截路": "辰",
                "空亡": "巳",
            },
            "壬": {
                "截路": "寅",
                "空亡": "卯",
            },
            "癸": {
                "截路": "子",
                "空亡": "丑",
            },
        }
        self.__name = "截空"
        self.__nian_gan = nian_gan

        self.截路 = biao.get(self.__nian_gan).get("截路")
        self.空亡 = biao.get(self.__nian_gan).get("空亡")


"""
安旬种和空亡星位置，但是表格只是给出了旬中星
"""


class Xun_Kong_Xing:
    def __init__(self, nian_gan, nian_zhi):
        self.__nian_gan = nian_gan
        self.__nian_zhi = nian_zhi
        biao = {
            "戌": {
                "甲": "子",
                "乙": "丑",
                "丙": "寅",
                "丁": "卯",
                "戊": "辰",
                "己": "巳",
                "庚": "午",
                "辛": "未",
                "壬": "申",
                "癸": "酉"
            },
            "申": {
                "甲": "戌",
                "乙": "亥",
                "丙": "子",
                "丁": "丑",
                "戊": "寅",
                "己": "卯",
                "庚": "辰",
                "辛": "巳",
                "壬": "午",
                "癸": "未"},
            "午": {
                "甲": "申",
                "乙": "酉",
                "丙": "戌",
                "丁": "亥",
                "戊": "子",
                "己": "丑",
                "庚": "寅",
                "辛": "卯",
                "壬": "辰",
                "癸": "巳"},
            "辰": {
                "甲": "午",
                "乙": "未",
                "丙": "申",
                "丁": "酉",
                "戊": "戌",
                "己": "亥",
                "庚": "子",
                "辛": "丑",
                "壬": "寅",
                "癸": "卯"},
            "寅": {
                "甲": "辰",
                "乙": "巳",
                "丙": "午",
                "丁": "未",
                "戊": "申",
                "己": "酉",
                "庚": "戌",
                "辛": "亥",
                "壬": "子",
                "癸": "丑"},
            "子": {
                "甲": "寅",
                "乙": "卯",
                "丙": "辰",
                "丁": "巳",
                "戊": "午",
                "己": "未",
                "庚": "申",
                "辛": "酉",
                "壬": "戌",
                "癸": "亥"},
            "亥": {
                "甲": "子",
                "乙": "丑",
                "丙": "寅",
                "丁": "卯",
                "戊": "辰",
                "己": "巳",
                "庚": "午",
                "辛": "未",
                "壬": "申",
                "癸": "酉"
            },
            "酉": {
                "甲": "戌",
                "乙": "亥",
                "丙": "子",
                "丁": "丑",
                "戊": "寅",
                "己": "卯",
                "庚": "辰",
                "辛": "巳",
                "壬": "午",
                "癸": "未"},
            "未": {
                "甲": "申",
                "乙": "酉",
                "丙": "戌",
                "丁": "亥",
                "戊": "子",
                "己": "丑",
                "庚": "寅",
                "辛": "卯",
                "壬": "辰",
                "癸": "巳"},
            "巳": {
                "甲": "午",
                "乙": "未",
                "丙": "申",
                "丁": "酉",
                "戊": "戌",
                "己": "亥",
                "庚": "子",
                "辛": "丑",
                "壬": "寅",
                "癸": "卯"},
            "卯": {
                "甲": "辰",
                "乙": "巳",
                "丙": "午",
                "丁": "未",
                "戊": "申",
                "己": "酉",
                "庚": "戌",
                "辛": "亥",
                "壬": "子",
                "癸": "丑"},
            "丑": {
                "甲": "寅",
                "乙": "卯",
                "丙": "辰",
                "丁": "巳",
                "戊": "午",
                "己": "未",
                "庚": "申",
                "辛": "酉",
                "壬": "戌",
                "癸": "亥"},
        }
        self.旬空 = biao.get(nian_zhi).get(nian_gan)


"""
天伤星
天使星
天伤永在仆役宫。
天使永在疾厄宫。
"""


class Tian_Shang_Tian_Shi_Xing:
    def __init__(self, ming_gong):
        self.ming_gong = ming_gong
        yu_gong_iter = Yu_Gong(ming_gong)  # 获取所有宫所在的位置
        for temp in di_zhi.values():
            yu_gong = yu_gong_iter.__getattribute__(temp)
            if yu_gong == "疾厄":
                self.天使 = temp
            if yu_gong == "友仆":
                self.天伤 = temp


if __name__ == '__main__':
    from tianji.config.shi_gan_biao_module import tian_gan

    d = nian_gan_xing_biao
    for star in nian_gan_xing_biao.get("甲").keys():
        print(star, [d.get(gan).get(star) for gan in tian_gan.values()])
    d = si_hua_xing_biao
    print("---" * 30, "\n四化星")
    for hua in ["化禄", "化权", "化科", "化忌"]:
        print(hua, [d.get(gan).get(hua) for gan in tian_gan.values()])
    print("---" * 30, "\n年支确定的星耀 \n")

    d = nian_zhi_xing_biao
    for star in ["天马", "解神", "天哭", "天虚", "龙池", "凤阁", "红鸾", "天喜", "孤辰", "寡宿", "蜚廉", "破碎", "天空",
                 "月德"]:
        print(star, [d.get(gan).get(star) for gan in di_zhi.values()])
    print("---" * 30, "\n确定天才、天寿星 \n")
    t = Tian_Cai_Tian_Show_xing(yue=5, shi_zhi="子", nian_zhi="子")
    print("天才星位置  {} ".format(t.get_tian_cai_loaction()))
    print("天寿星位置  {} ".format(t.get_tian_show_loaction()))
    print("---" * 30, "\n确定截路空亡星 \n")
    nian_gan = "丙"
    jie_kong = Jie_Kong_Xing(nian_gan)
    print(f"年干 {nian_gan}  \n截路位置 {jie_kong.截路}  空亡位置 {jie_kong.空亡}")
    print("---" * 30, "\n确定旬中空亡星 \n")
    nian_zhi = "寅"
    xun_zhong = Xun_Kong_Xing(nian_gan, nian_zhi)
    print(f"年干年支 {nian_gan}{nian_zhi}  \n旬中位置 {xun_zhong.旬空}  空亡位置 未知")

    print("---" * 30, "\n确定天伤天使星 \n")
    ming_gong = "亥"
    t = Tian_Shang_Tian_Shi_Xing(ming_gong)
    print(f"天伤 -> {t.天伤}  天使 {t.天使} ")
