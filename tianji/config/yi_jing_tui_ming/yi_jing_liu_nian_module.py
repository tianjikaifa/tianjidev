#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2024/1/12 13:13
# @Author  : huangfujue
# @File    : yi_jing_liu_nian_module.py
# @Date    : 2024/1/12 
"""
用来表示每个卦的大运和流年，需要有元堂爻
"""

# ----------------------------------------------------------------------------------------------------------------------
from tianji.config.yi_jing_tui_ming.gua_module import BaseGua, Gua
from tianji.config.yi_jing_tui_ming.yi_jing_pai_ming import get_xian_tian_gua, get_hou_tian_gua
from tianji.config.zi_wei_dou_shu.shi_er_di_zhi_biao_module import Di_Zhi_Iter
from tianji.config.zi_wei_dou_shu.shi_gan_biao_module import Tian_Gan_Iter

from lunar_python import Lunar, Solar




class YaoIter:
    def __init__(self, cheng_gua):
        self.cheng_gua = cheng_gua
        self.yuan_tang_yao = cheng_gua.yuan_tang_yao
        self.gua_zu_cheng = cheng_gua.gua_zu_cheng
        self.start_year = 0

    def next(self):
        current = self.yuan_tang_yao
        if current > 5:
            self.yuan_tang_yao = 1
        else:
            self.yuan_tang_yao += 1

        # 阳爻9年，阴爻6年
        yin_yang_yao = self.gua_zu_cheng[current - 1]
        age = 9 if yin_yang_yao == "1" else 6
        start_year = self.start_year
        self.start_year += age
        return [start_year + 1, start_year + age]

    def yang_yao_bian(self, bian_yao, nian_gan, nian_zhi, is_fist=False):
        """
        用来表示九龙游变法，将一个爻进行变化
        元堂爻、应爻、应爻、然后往上走六个爻
        :param bian_yao:
        :param nian_gan:
        :param nian_zhi:
        :param is_fist:
        :return:
        """
        tian_gan_iter = Tian_Gan_Iter(nian_gan)
        di_zhi_iter = Di_Zhi_Iter(1)
        di_zhi_iter.update(nian_zhi)

        seq = self.make_yang_yao_bian_sqe(bian_yao)
        temp_gua = self.cheng_gua

        # if temp_gua.gua_zu_cheng[bian_yao - 1] == "1":
        liu_nian_gua = []
        if is_fist:
            if nian_gan in "甲丙戊庚壬":
                temp_gua.yuan_tang_yao = bian_yao
                temp_gua.nian_gan = nian_gan
                temp_gua.nian_zhi = nian_zhi
                liu_nian_gua.append(temp_gua)
            else:
                gua = list(temp_gua.gua_zu_cheng)
                yao_type = gua[bian_yao - 1]
                gua[bian_yao - 1] = self.bian_yao(yao_type, nian_gan)
                gua = "".join(gua)
                x = BaseGua.fond(gua[:3])
                s = BaseGua.fond(gua[3:])
                temp_gua = Gua(s, x, bian_yao)
                temp_gua.yuan_tang_yao = bian_yao
                temp_gua.nian_gan = nian_gan
                temp_gua.nian_zhi = nian_zhi
                liu_nian_gua.append(temp_gua)
        else:
            gua = list(temp_gua.gua_zu_cheng)
            yao_type = gua[bian_yao - 1]
            gua[bian_yao - 1] = self.bian_yao(yao_type, nian_gan)
            gua = "".join(gua)
            x = BaseGua.fond(gua[:3])
            s = BaseGua.fond(gua[3:])
            temp_gua = Gua(s, x, bian_yao)
            temp_gua.yuan_tang_yao = bian_yao
            temp_gua.nian_gan = nian_gan
            temp_gua.nian_zhi = nian_zhi
            liu_nian_gua.append(temp_gua)
        # print(age_count,temp_gua.name, temp_gua.nian_gan, temp_gua.nian_zhi)
        for yao_index in seq:
            gan = tian_gan_iter.next()
            zhi = di_zhi_iter.up()
            gua = list(temp_gua.gua_zu_cheng)
            yao_type = gua[yao_index - 1]
            gua[yao_index - 1] = "0" if yao_type == "1" else "1"
            gua = "".join(gua)
            x = BaseGua.fond(gua[:3])
            s = BaseGua.fond(gua[3:])
            temp_gua = Gua(s, x, yao_index)
            temp_gua.nian_gan = gan
            temp_gua.nian_zhi = zhi

            liu_nian_gua.append(temp_gua)
            # print(age_count,temp_gua.name, temp_gua.nian_gan, temp_gua.nian_zhi)
        return liu_nian_gua

    def yin_yao_bian(self, bian_yao, nian_gan, nian_zhi):
        """
        用来表示九龙游变法，将一个爻进行变化
        元堂爻、应爻、元堂爻、然后往上走六个爻
        :param bian_yao:
        :return:
        """
        tian_gan_iter = Tian_Gan_Iter(nian_gan)
        di_zhi_iter = Di_Zhi_Iter(1)
        di_zhi_iter.update(nian_zhi)

        seq = self.make_yin_yao_bian_sqe(bian_yao)
        temp_gua = self.cheng_gua

        gua = list(temp_gua.gua_zu_cheng)
        yao_type = gua[bian_yao - 1]
        gua[bian_yao - 1] = "0" if yao_type == "1" else "1"
        gua = "".join(gua)
        x = BaseGua.fond(gua[:3])
        s = BaseGua.fond(gua[3:])
        temp_gua = Gua(s, x, bian_yao)
        temp_gua.yuan_tang_yao = bian_yao
        temp_gua.nian_gan = nian_gan
        temp_gua.nian_zhi = nian_zhi
        liu_nian_gua = [temp_gua]

        # print(age_count,temp_gua.name, temp_gua.nian_gan, temp_gua.nian_zhi)
        for yao_index in seq:
            gan = tian_gan_iter.next()
            zhi = di_zhi_iter.up()
            gua = list(temp_gua.gua_zu_cheng)
            yao_type = gua[yao_index - 1]
            gua[yao_index - 1] = "0" if yao_type == "1" else "1"
            gua = "".join(gua)
            x = BaseGua.fond(gua[:3])
            s = BaseGua.fond(gua[3:])
            temp_gua = Gua(s, x, yao_index)
            temp_gua.nian_gan = gan
            temp_gua.nian_zhi = zhi
            # print(age_count,temp_gua.name, temp_gua.nian_gan, temp_gua.nian_zhi)
            liu_nian_gua.append(temp_gua)
        return liu_nian_gua

    def bian_yao(self, yao, nian_gan="None"):
        """
        一个卦的首年阳爻遇阳年不变，阴年则变
        :param yao:
        :param nian_gan:
        :return:
        """
        if nian_gan in "甲丙戊庚壬":
            return yao
        else:
            return "0"

    def make_yang_yao_bian_sqe(self, bian_yao):
        if self.gua_zu_cheng[bian_yao - 1] == "0":
            raise Exception(f"九龙游变法只使用于阳爻，请检查这个爻是否为阳爻 {bian_yao}")
        seq = []
        # 应爻对照表
        ying_yao = {
            1: 4,
            2: 5,
            3: 6,
            4: 1,
            5: 2,
            6: 3,
        }
        new_yuan_tang = ying_yao.get(bian_yao)
        seq.append(new_yuan_tang)
        new_yuan_tang = ying_yao.get(new_yuan_tang)
        seq.append(new_yuan_tang)

        for i in range(6):
            new_yuan_tang = self.get_next_yao_index(new_yuan_tang)
            seq.append(new_yuan_tang)

        return seq

    def make_yin_yao_bian_sqe(self, bian_yao):
        if self.gua_zu_cheng[bian_yao - 1] == "1":
            raise Exception(f"请检查这个爻是否为阴爻 {bian_yao}")
        seq = []

        for i in range(5):
            bian_yao = self.get_next_yao_index(bian_yao)
            seq.append(bian_yao)

        return seq

    def get_next_yao_index(self, yao_index):
        next_yao_index = yao_index + 1
        if next_yao_index > 6:
            next_yao_index = 1
        return next_yao_index


def get_liu_nian_gua(ba_zi, year, gender, dong_zhi_hou_xia_zhi_qian):
    res = get_xian_tian_gua(ba_zi, gender, year)
    xian_tian_gua = Gua.find_gua(res[0])
    xian_tian_gua.yuan_tang_yao = xian_tian_gua.get_yuan_tang(ba_zi[-1])
    hou_tian_gua = get_hou_tian_gua(res[1], res[2], ba_zi[-1], dong_zhi_hou_xia_zhi_qian)
    # print(hou_tian_gua.name,hou_tian_gua.yuan_tang_yao)
    # print(xian_tian_gua.name,xian_tian_gua.yuan_tang_yao)
    # 先天卦
    nina_gan = ba_zi[0]
    nian_zhi = ba_zi[1]
    it = YaoIter(xian_tian_gua)
    liu_nian_gua = []
    t_iter = Tian_Gan_Iter("甲")
    d_iter = Di_Zhi_Iter(1)
    qi_yun_yao = xian_tian_gua.yuan_tang_yao
    yao = it.gua_zu_cheng[qi_yun_yao - 1]

    if yao == "1":
        res = it.yang_yao_bian(qi_yun_yao, nina_gan, nian_zhi, True)
    else:
        res = it.yin_yao_bian(qi_yun_yao, nina_gan, nian_zhi)
    liu_nian_gua.extend(res)
    last_gua = res[-1]
    t_iter.update(last_gua.nian_gan)
    d_iter.update(last_gua.nian_zhi)
    gan_ = t_iter.next()
    zhi_ = d_iter.next()

    for _ in range(5):
        qi_yun_yao = it.get_next_yao_index(qi_yun_yao)
        yao = it.gua_zu_cheng[qi_yun_yao - 1]
        if yao == "1":
            res = it.yang_yao_bian(qi_yun_yao, gan_, zhi_)
        else:
            res = it.yin_yao_bian(qi_yun_yao, gan_, zhi_)
        liu_nian_gua.extend(res)
        last_gua = res[-1]
        t_iter.update(last_gua.nian_gan)
        d_iter.update(last_gua.nian_zhi)
        gan_ = t_iter.next()
        zhi_ = d_iter.next()
    # 后天卦
    it = YaoIter(hou_tian_gua)
    qi_yun_yao = hou_tian_gua.yuan_tang_yao
    yao = it.gua_zu_cheng[qi_yun_yao - 1]

    if yao == "1":
        # 只有卦的第1岁的阳爻需要考虑阴阳年
        res = it.yang_yao_bian(qi_yun_yao, nina_gan, nian_zhi, True)
    else:
        res = it.yin_yao_bian(qi_yun_yao, nina_gan, nian_zhi)
    liu_nian_gua.extend(res)
    last_gua = res[-1]
    t_iter.update(last_gua.nian_gan)
    d_iter.update(last_gua.nian_zhi)
    gan_ = t_iter.next()
    zhi_ = d_iter.next()

    for _ in range(5):
        qi_yun_yao = it.get_next_yao_index(qi_yun_yao)
        yao = it.gua_zu_cheng[qi_yun_yao - 1]
        if yao == "1":
            res = it.yang_yao_bian(qi_yun_yao, gan_, zhi_)
        else:
            res = it.yin_yao_bian(qi_yun_yao, gan_, zhi_)
        liu_nian_gua.extend(res)
        last_gua = res[-1]
        t_iter.update(last_gua.nian_gan)
        d_iter.update(last_gua.nian_zhi)
        gan_ = t_iter.next()
        zhi_ = d_iter.next()

    return liu_nian_gua


def next_index(index):
    return index + 1 if index < 6 else 1


def make_bian_gua(gua, dong_yao):
    yao = gua[dong_yao - 1]
    gua[dong_yao - 1] = "0" if yao == "1" else "1"
    gua = "".join(gua)
    x = BaseGua.fond(gua[:3])
    s = BaseGua.fond(gua[3:])
    temp_gua = Gua(s, x, dong_yao)
    return temp_gua, gua


def get_liu_yue_gua(liu_nian_gua):
    liu_yue_gua = []

    ying_yao_index_biao = {
        1: 4,
        2: 5,
        3: 6,
        4: 1,
        5: 2,
        6: 3
    }
    dong_yao = liu_nian_gua.yuan_tang_yao
    gua_zu_cheng = liu_nian_gua.gua_zu_cheng
    gua = list(gua_zu_cheng)
    for i in range(6):
        # 阳月
        yang_gua=[y for y in gua]
        dong_yao = next_index(dong_yao)
        liu_yue, gua = make_bian_gua(yang_gua, dong_yao)
        liu_yue.yue_fen=i+1
        liu_yue_gua.append(liu_yue)
        # 阴月
        yin_gua=[d for d in gua]
        ying_yao = ying_yao_index_biao.get(dong_yao)
        liu_yue, _ = make_bian_gua(yin_gua, ying_yao)
        liu_yue.yue_fen = i + 2
        liu_yue_gua.append(liu_yue)

    return liu_yue_gua

# 流日卦暂时不能使用，没搞清楚
def get_liu_ri_gua(liu_yue_gua):
    """
    因为易经推命术的每个月是节与节之间的，但是每年的节都在动态的变化，
    所以需要获取这一年对应月份的开始和结束时间,一个卦代表六天
    :param liu_yue_gua:
    :return:
    """
    liu_ri_gua=[]
    dong_yao = liu_yue_gua.yuan_tang_yao
    gua_zu_cheng = liu_yue_gua.gua_zu_cheng
    dong_yao = next_index(dong_yao)
    gua = list(gua_zu_cheng)
    liu_yue, gua = make_bian_gua(gua, dong_yao)
    liu_ri_gua.append(liu_yue)
    for i in range(6):
        gua=list(gua)
        liu_yue, gua = make_bian_gua(gua, dong_yao)
        liu_ri_gua.append(liu_yue)
        dong_yao = next_index(dong_yao)


    return liu_ri_gua


if __name__ == '__main__':
    # bazi = "庚辰戊寅癸巳癸丑"
    # year = 2000
    # gender = "男"
    # dong_zhi_hou_xia_zhi_qian = True
    # res = liu_nians = get_liu_nian_gua(bazi, year, gender, dong_zhi_hou_xia_zhi_qian)

    # cheng_gua = Gua.find_gua("风雷益")
    # cheng_gua.yuan_tang_yao = 5
    # res = get_liu_yue(cheng_gua)
    # for gua in res:
    #     print(gua.yue_fen,"月",gua.name,gua.yuan_tang_yao)

    cheng_gua = Gua.find_gua("水火即济")
    cheng_gua.yuan_tang_yao = 2
    res = get_liu_ri(cheng_gua)
    for gua in res:
        print(gua.name,gua.yuan_tang_yao)