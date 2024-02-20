#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2024/1/3 13:21
# @Author  : huangfujue
# @File    : liu_nian_gua_module.py
# @Date    : 2024/1/3 
"""
根据先天卦和时支计算后天卦
"""

# ----------------------------------------------------------------------------------------------------------------------

from tianji.config.json_module import gua_zu_he_biao


class BaseGua:
    biao = {
        "乾": "111",
        "兑": "110",
        "离": "101",
        "震": "100",
        "巽": "011",
        "坎": "010",
        "艮": "001",
        "坤": "000"
    }
    biao2 = {
        "天": "乾",
        "泽": "兑",
        "火": "离",
        "雷": "震",
        "风": "巽",
        "水": "坎",
        "山": "艮",
        "地": "坤"
    }

    def __init__(self, name):
        name = BaseGua.biao2.get(name, name)
        self.name = name
        self.gua_info = BaseGua.biao.get(name, None)
        if self.gua_info is None:
            raise Exception(f"错误的卦名 {name}")

    @staticmethod
    def fond(info="111"):
        if len(info) == 3:
            for k, v in BaseGua.biao.items():
                if v == info:
                    return BaseGua(k)

        # 找不到的或者格式不对的直接抛异常
        raise Exception(f"卦的表示应该是3个0和1的组合的字符串，例如‘111’找到的是乾,但给的是 {info}")


class Gua:

    def __init__(self, shang, xia, yuan_tang_yao=-1):
        """
        用基本卦表示一个卦，基本卦是这个 BaseGua
        :param shang: 上基本卦
        :param xia: 下基本卦
        :param yuan_tang: 表示这个卦的元堂爻
        """
        self.name = gua_zu_he_biao.get(xia.name).get(shang.name)
        self.shang = shang
        self.xia = xia
        self.yuan_tang_yao = yuan_tang_yao
        self.gua_zu_cheng = f"{self.xia.gua_info}{self.shang.gua_info}"

        self.yang_yao_index = []
        self.yin_yao_index = []
        self.yao_index = [0, 1, 2, 3, 4, 5]
        self.yang_count = 0
        self.yin_count = 0
        for i in range(6):
            t = self.gua_zu_cheng[i]
            if t == "1":
                self.yang_yao_index.append(i)
                self.yang_count += 1
            else:
                self.yin_yao_index.append(i)
                self.yin_count += 1

    def get_yuan_tang(self, shi_zhi, gender="男", dong_zhi_hou_xia_zhi_qian=True):
        """
        取一个卦的元堂爻在一个卦的第几爻
        :param shi_zhi:
        :param gender:
        :param dong_zhi_hou_xia_zhi_qian:
        :return:
        """
        funcs = {
            1: self.yi,
            2: self.er,
            3: self.san,
            4: self.si,
            5: self.wu,
        }
        # 阳时以阳爻为主，阴时以阴爻为主
        if shi_zhi in ["子", "丑", "寅", "卯", "辰", "巳"]:
            yin_yang = "1"
            func = funcs.get(self.yang_count, None)
            if func is None:
                res = self.liu(yin_yang, gender, dong_zhi_hou_xia_zhi_qian).get(shi_zhi)
            else:
                res = func(yin_yang).get(shi_zhi)
        else:
            yin_yang = "0"
            func = funcs.get(self.yin_count, None)
            if func is None:
                res = self.liu(yin_yang, gender, dong_zhi_hou_xia_zhi_qian).get(shi_zhi)
            else:
                res = func(yin_yang).get(shi_zhi)
        # self.yuan_tang_yao = res + 1
        return res + 1  # 将爻的位置表示为常规位置

    def bian_hou_tian_gua(self, yuan_tang_yao, dong_zhi_hou_xia_zhi_qian):
        """
        根据某个元堂爻将先天卦变为后天卦,至尊卦稍微特殊点（坎为水，水雷屯，水山蹇），他们的阴主（上六）阳君（九五）不可轻变
        :param yuan_tang_yao:
        :param dong_zhi_hou_xia_zhi_qian: 冬至后夏至前的属于阳令，给Ture，夏至后冬至前属于阴月，给False
        :return:
        """
        # 单独处理至尊卦
        if self.name in ["坎为水", "水雷屯", "水山蹇"]:
            res = self.zhi_zun(yuan_tang_yao, dong_zhi_hou_xia_zhi_qian)
            if not res is None:
                return res

        gua_zu_cheng = self.gua_zu_cheng
        yao = gua_zu_cheng[yuan_tang_yao - 1]
        yao = "1" if yao == "0" else "0"

        gua_zu_cheng = list(self.gua_zu_cheng)
        # 普通卦的处理
        gua_zu_cheng[yuan_tang_yao - 1] = yao
        gua_zu_cheng = "".join(gua_zu_cheng)
        xia_gua = BaseGua.fond(gua_zu_cheng[:3])
        shang_gua = BaseGua.fond(gua_zu_cheng[3:])
        # print(shang_gua.name)
        # print(xia_gua.name)
        new_yuan_tang = yuan_tang_yao - 3 if yuan_tang_yao > 3 else yuan_tang_yao + 3
        gua = Gua(xia_gua, shang_gua, yuan_tang_yao=new_yuan_tang)  # 变后天卦要上下颠倒
        return gua

    def zhi_zun(self, yuan_tang_yao, dong_zhi_hou_xia_zhi_qian):
        """
        对至尊卦的九五和上六进行处理，其他的按常规处理
        :param yuan_tang_yao:
        :param dong_zhi_hou_xia_zhi_qian:
        :return:
        """
        gua_zu_cheng = self.gua_zu_cheng
        yao = gua_zu_cheng[yuan_tang_yao - 1]
        yao = "1" if yao == "0" else "0"

        # 三至尊卦的九五和上六的处理
        if self.name in ["坎为水", "水雷屯", "水山蹇"]:
            # 九五的处理
            if yuan_tang_yao == 5 and gua_zu_cheng[4] == "1":
                biao = {
                    "坎为水": {
                        True: Gua(BaseGua("雷"), BaseGua("地"), yuan_tang_yao=2),
                        False: Gua(BaseGua("地"), BaseGua("水"), yuan_tang_yao=5)
                    },
                    "水雷屯": {
                        True: Gua(BaseGua("山"), BaseGua("地"), yuan_tang_yao=2),
                        False: Gua(BaseGua("地"), BaseGua("雷"), yuan_tang_yao=5)
                    },
                    "水山蹇": {
                        True: Gua(BaseGua("水"), BaseGua("地"), yuan_tang_yao=2),
                        False: Gua(BaseGua("地"), BaseGua("山"), yuan_tang_yao=5)
                    }
                }
                return biao.get(self.name).get(dong_zhi_hou_xia_zhi_qian)

            # 上六的处理
            if yuan_tang_yao == 6 and gua_zu_cheng[5] == "0":
                biao = {
                    "坎为水": {
                        True: Gua(BaseGua("风"), BaseGua("雷"), yuan_tang_yao=6),
                        False: Gua(BaseGua("水"), BaseGua("风"), yuan_tang_yao=3)
                    },
                    "水雷屯": {
                        True: Gua(BaseGua("风"), BaseGua("山"), yuan_tang_yao=6),
                        False: Gua(BaseGua("雷"), BaseGua("风"), yuan_tang_yao=3)
                    },
                    "水山蹇": {
                        True: Gua(BaseGua("风"), BaseGua("水"), yuan_tang_yao=6),
                        False: Gua(BaseGua("山"), BaseGua("风"), yuan_tang_yao=3)
                    }
                }
                return biao.get(self.name).get(dong_zhi_hou_xia_zhi_qian)
        else:
            raise Exception(f"三至尊卦只有坎、屯、蹇，但是当前是 {self.name}")
        # 是至尊卦，但是不是九五上六的还是按常规方法
        return None

    def yi(self, yin_yang="1"):
        yang_shi = ["子", "丑", "寅", "卯", "辰", "巳"]
        yin_shi = ["午", "未", "申", "酉", "戌", "亥"]
        shis = yang_shi if yin_yang == "1" else yin_shi
        dd = {}
        target_yao_index = self.gua_zu_cheng.find(yin_yang)

        dd[shis.pop(0)] = target_yao_index
        dd[shis.pop(0)] = target_yao_index
        self.yao_index.remove(target_yao_index)
        for i, shi in enumerate(shis):
            dd[shi] = self.yao_index[i]

        return dd

    def er(self, yin_yang="1"):
        yang_shi = ["子", "丑", "寅", "卯", "辰", "巳"]
        yin_shi = ["午", "未", "申", "酉", "戌", "亥"]
        shis = yang_shi if yin_yang == "1" else yin_shi
        dd = {}
        target_1 = self.gua_zu_cheng.find(yin_yang)
        target_2 = self.gua_zu_cheng.find(yin_yang, target_1 + 1)

        dd[shis.pop(0)] = target_1
        dd[shis.pop(0)] = target_2
        dd[shis.pop(0)] = target_1
        dd[shis.pop(0)] = target_2
        self.yao_index.remove(target_1)
        self.yao_index.remove(target_2)
        for i, shi in enumerate(shis):
            dd[shi] = self.yao_index[i]

        return dd

    def san(self, yin_yang="1"):
        yang_shi = ["子", "丑", "寅", "卯", "辰", "巳"]
        yin_shi = ["午", "未", "申", "酉", "戌", "亥"]
        shis = yang_shi if yin_yang == "1" else yin_shi
        dd = {}
        target_1 = self.gua_zu_cheng.find(yin_yang)
        target_2 = self.gua_zu_cheng.find(yin_yang, target_1 + 1)
        target_3 = self.gua_zu_cheng.find(yin_yang, target_2 + 1)

        dd[shis.pop(0)] = target_1
        dd[shis.pop(0)] = target_2
        dd[shis.pop(0)] = target_3

        dd[shis.pop(0)] = target_1
        dd[shis.pop(0)] = target_2
        dd[shis.pop(0)] = target_3

        return dd

    def si(self, yin_yang="1"):
        yang_shi = ["子", "丑", "寅", "卯", "辰", "巳"]
        yin_shi = ["午", "未", "申", "酉", "戌", "亥"]
        shis = yang_shi if yin_yang == "1" else yin_shi
        dd = {}
        target_1 = self.gua_zu_cheng.find(yin_yang)
        target_2 = self.gua_zu_cheng.find(yin_yang, target_1 + 1)
        target_3 = self.gua_zu_cheng.find(yin_yang, target_2 + 1)
        target_4 = self.gua_zu_cheng.find(yin_yang, target_3 + 1)

        dd[shis.pop(0)] = target_1
        dd[shis.pop(0)] = target_2
        dd[shis.pop(0)] = target_3
        dd[shis.pop(0)] = target_4
        self.yao_index.remove(target_1)
        self.yao_index.remove(target_2)
        self.yao_index.remove(target_3)
        self.yao_index.remove(target_4)
        for i, shi in enumerate(shis):
            dd[shi] = self.yao_index[i]
        return dd

    def wu(self, yin_yang="1"):
        yang_shi = ["子", "丑", "寅", "卯", "辰", "巳"]
        yin_shi = ["午", "未", "申", "酉", "戌", "亥"]
        shis = yang_shi if yin_yang == "1" else yin_shi
        dd = {}
        target_1 = self.gua_zu_cheng.find(yin_yang)
        target_2 = self.gua_zu_cheng.find(yin_yang, target_1 + 1)
        target_3 = self.gua_zu_cheng.find(yin_yang, target_2 + 1)
        target_4 = self.gua_zu_cheng.find(yin_yang, target_3 + 1)
        target_5 = self.gua_zu_cheng.find(yin_yang, target_4 + 1)

        dd[shis.pop(0)] = target_1
        dd[shis.pop(0)] = target_2
        dd[shis.pop(0)] = target_3
        dd[shis.pop(0)] = target_4
        dd[shis.pop(0)] = target_5
        self.yao_index.remove(target_1)
        self.yao_index.remove(target_2)
        self.yao_index.remove(target_3)
        self.yao_index.remove(target_4)
        self.yao_index.remove(target_5)
        dd[shis.pop(0)] = self.yao_index[0]
        return dd

    def liu(self, yin_yang="1", gender="男", dong_zhi_hou_xia_zhi_qian=True):
        """
        纯爻要根据男女和阴阳属性来判断怎么排
        :param yin_yang: 取的是阳时还是阴时，因为纯爻卦的排法不是固定的一个，所以得和其他得区分开
        :param gender:
        :param dong_zhi_hou_xia_zhi_qian: 是否在冬至以后，夏至以前
        :return:
        """
        yang_shi = ["子", "丑", "寅", "卯", "辰", "巳"]
        yin_shi = ["午", "未", "申", "酉", "戌", "亥"]
        shis = yang_shi if yin_yang == "1" else yin_shi
        dd = {}

        index_xia = [0, 1, 2, 0, 1, 2]
        index_shang = [3, 4, 5, 3, 4, 5]
        if self.gua_zu_cheng == "111111":  # 乾卦的处理
            if gender == "男":
                # 男性,阳时，阴时
                index = index_xia if yin_yang == "1" else index_shang
            else:
                # 女性要判断时间，在冬至以后，夏至以前的和男的相反，夏至以后冬至以前一样
                if dong_zhi_hou_xia_zhi_qian:
                    index = index_shang if yin_yang == "1" else index_xia
                else:
                    index = index_xia if yin_yang == "1" else index_shang
        else:
            # 坤卦的处理
            if gender == "女":
                # 女性
                index = index_xia if yin_yang == "1" else index_shang

            else:
                # 男性要判断时间，在冬至以后，夏至以前的和女性的相反，夏至以后冬至以前一样
                if dong_zhi_hou_xia_zhi_qian:
                    index = index_xia if yin_yang == "1" else index_shang
                else:
                    index = index_shang if yin_yang == "1" else index_xia

        # 乾卦，男子不区分冬至前后
        dd[shis.pop(0)] = index.pop(0)
        dd[shis.pop(0)] = index.pop(0)
        dd[shis.pop(0)] = index.pop(0)
        dd[shis.pop(0)] = index.pop(0)
        dd[shis.pop(0)] = index.pop(0)
        dd[shis.pop(0)] = index.pop(0)

        return dd

    @staticmethod
    def find_gua( name):
        for xia in gua_zu_he_biao:
            temp = gua_zu_he_biao.get(xia)
            for shang in temp:
                if name == temp.get(shang):
                    return Gua(BaseGua(shang), BaseGua(xia))

        raise Exception(f"64个卦中无法找到名字为{name}的卦，请检查是否给定正确的卦名称")


if __name__ == '__main__':
    s = BaseGua("火")
    x = BaseGua("山")
    shi_zhi = "寅"
    dong_zhi_hou_xia_zhi_qian = True
    g = Gua(s, x)
    print(g.gua_zu_cheng)
    print(g.name)
    yuantang = g.get_yuan_tang(shi_zhi)
    print("元堂爻", yuantang)
    print(g.bian_hou_tian_gua(yuantang, dong_zhi_hou_xia_zhi_qian).name)
    print(g.bian_hou_tian_gua(yuantang, dong_zhi_hou_xia_zhi_qian).name)
