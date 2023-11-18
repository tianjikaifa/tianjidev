#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/15 14:55
# @Author  : huangfujue
# @File    : 十二宫.py
# @Date    : 2023/11/15 
"""
表示紫薇斗数的十二个宫的容器
"""
import sxtwl

from tianji.config.主星表 import bei_dou_zhu_xing_biao, nan_dou_zhu_xing_biao
from tianji.config.五行局表 import Wu_Xing
from tianji.config.余宫表 import Yu_Gong
from tianji.config.十二宫天干表 import Shi_Er_Gong_Tian_Gan
from tianji.config.十二支所属表 import di_zhi, Di_Zhi_Iter
from tianji.config.十干表 import tian_gan, shi_gan_biao
from tianji.config.博士十二星 import Bo_Shi_Shi_Er_Xing
from tianji.config.命宫身宫表 import Ming_Shen_Gong, Ming_Zhu, Shen_Zhu
from tianji.config.大限表 import Da_Liu_Nian
from tianji.config.子年斗君表 import Dou_jun
from tianji.config.年系诸星表 import nian_gan_xing_biao, si_hua_xing_biao, nian_zhi_xing_biao, Tian_Cai_Tian_Show_xing, \
    Jie_Kong_Xing, Xun_Kong_Xing, Tian_Shang_Tian_Shi_Xing
from tianji.config.庙旺利陷表 import liang_du_biao
from tianji.config.日系诸星表 import CalculateLocation
from tianji.config.时系诸星表 import shi_chen_xing_biao, huo_ling_xing_biao
from tianji.config.星辰表 import dou_shu_stars
from tianji.config.月系诸星表 import yue_xing_biao
from tianji.config.流年诸星表 import Liu_Nian_Xing
from tianji.config.起紫薇表 import zi_wei_biao
from tianji.config.长生十二星 import chang_sheng_shi_er_xing_biao


# ----------------------------------------------------------------------------------------------------------------------


class PanTime:
    """
    表示紫薇斗数的一个排盘时间,使用农历时间作为输入
    """

    def __init__(self, nian, yue, ri, shi):
        """
        默认农历
        :param nian: 农历年
        :param yue: 农历月
        :param ri: 农历日
        :param shi: 几点,会转化成时辰
        """

        self.nian = nian
        self.yue = yue
        self.ri = ri
        self.shi = shi
        self.day_info = sxtwl.fromLunar(self.nian, self.yue, self.ri)
        self.get_ba_zi()

    def get_ba_zi(self):
        Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        # ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]

        # yTG = self.day_info.getYearGZ(False) # 按春节这天作为两年分割线
        yTG = self.day_info.getYearGZ(True)  # 按春分这天作为两年的分割线
        mTG = self.day_info.getMonthGZ()
        dTG = self.day_info.getDayGZ()
        self.ntg = Gan[yTG.tg]
        self.ndz = Zhi[yTG.dz]

        self.ytg = Gan[mTG.tg]
        self.ydz = Zhi[mTG.dz]

        self.rtg = Gan[dTG.tg]
        self.rdz = Zhi[dTG.dz]

        # 时干支
        hTG = sxtwl.getShiGz(dTG.tg, self.shi)
        self.stg = Gan[hTG.tg]
        self.sdz = Zhi[hTG.dz]
        return [self.ntg, self.ndz, self.ytg, self.ydz, self.rtg, self.rdz, self.stg, self.sdz]

    def lunar_to_solar(self):
        """
        农历转新历,时间是不变的
        :param nian:
        :param yue:
        :param ri:
        :return:
        """

        y = self.day_info.getSolarYear()
        m = self.day_info.day.getSolarMonth()
        d = self.day_info.getSolarDay()
        return y, m, d

    def get_jie_qi(self):
        """
        获取这一天是不是节气，因为涉及到跨年
        :return:
        """
        jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏",
                "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
                "立冬", "小雪", "大雪"]
        if self.day_info.hasJieQi():
            # print('节气：%s' % jqmc[self.day_info.getJieQi()])
            # 获取节气的儒略日数
            jd = self.day_info.getJieQiJD()
            # 将儒略日数转换成年月日时秒
            t = sxtwl.JD2DD(jd)

            # 注意，t.s是小数，需要四舍五入
            # print("节气时间:%d-%d-%d %d:%d:%d" % (t.Y, t.M, t.D, t.h, t.m, round(t.s)))
            return True, jqmc[self.day_info.getJieQi()], (t.Y, t.M, t.D, t.h, t.m, round(t.s))
        else:
            return False, None, None

    @staticmethod
    def solar_to_lunar(nian, yue, ri):
        """
        新历转农历
        :param nian:
        :param yue:
        :param ri:
        :return:
        """
        day = sxtwl.fromSolar(nian, yue, ri)
        y = day.getLunarYear()
        m = day.getLunarMonth()
        d = day.getLunarDay()
        return y, m, d


class Gong:
    """
    表示紫薇斗数的十二个宫的容器
    """

    def __init__(self, location):
        self.location = location
        # 表示每个等级的星耀，不同等级的星耀会排在不同位置
        self.stars = {
            "甲": [],
            "乙": [],
            "丙": [],
            "丁": []
        }

    def get_san_fang(self, pan):
        """
        获取此宫的三方结果
        :param pan: 排盘对象
        :return:
        """
        di_zhi_iter = Di_Zhi_Iter(-1)
        di_zhi_iter.update(self.location)
        for i in range(4):
            di_zhi_iter.next()
        shi_ye_gong_location = di_zhi_iter.now()
        for i in range(2):
            di_zhi_iter.next()
        qian_yi_gong_location = di_zhi_iter.now()
        for i in range(2):
            di_zhi_iter.next()
        cai_bo_location = di_zhi_iter.now()
        return [pan.gongs.get(shi_ye_gong_location),
                pan.gongs.get(qian_yi_gong_location),
                pan.gongs.get(cai_bo_location)]

    def append_start(self, star_info):
        star_name = star_info.name
        level = star_info.level
        if level != "四化":  # 不是四化星
            self.stars.get(level).append(f"{star_name}{liang_du_biao.get(self.location).get(star_name, '')}")
        else:
            # 是四化星
            hua_xing = star_info.belong_star
            old_star_name = f"{hua_xing}{liang_du_biao.get(self.location).get(hua_xing, '')}"
            remove_level = self.__remove_star__(old_star_name)
            new_star_name = f"{hua_xing}{liang_du_biao.get(self.location).get(hua_xing, '')} {star_info.name}"
            self.stars.get(remove_level).append(new_star_name)

    def set_name(self, name):
        """
        设置宫名称
        :param name:
        :return:
        """
        self.name = "{}宫".format(name)

    def set_da_xian(self, da_xain):
        self.da_xian = da_xain

    def set_tian_gan(self, gong_tian_gan):
        """
        设置宫名称
        :param gong_tian_gan:
        :return:
        """
        self.gong_tian_gan = gong_tian_gan

    def __remove_star__(self, remove_star):
        for level, stars in self.stars.items():
            for star in stars:
                if star == remove_star:
                    stars.remove(star)
                    return level

    def pai_pan(self):
        """
        排盘,暂时模拟
        :return:
        """
        print(f"{self.da_xian}")
        print(f"{self.gong_tian_gan}{self.location}\n")
        for k, v in self.stars.items():
            print(k, self.stars.get(k))


class Pan:
    """
    表示紫薇斗数的一个排盘结果

    """

    def __init__(self, pan_time, gender):
        """
        需要按农历来
        :param pan_time:
        :param gender:
        """
        self.pan_time = pan_time
        self.ba_zi = self.pan_time.get_ba_zi()
        self.gender = gender
        self.gongs = {
            "子": Gong("子"),
            "丑": Gong("丑"),
            "寅": Gong("寅"),
            "卯": Gong("卯"),
            "辰": Gong("辰"),
            "巳": Gong("巳"),
            "午": Gong("午"),
            "未": Gong("未"),
            "申": Gong("申"),
            "酉": Gong("酉"),
            "戌": Gong("戌"),
            "亥": Gong("亥"),
        }
        self.da_liu_nian = {}

        self.star_loaction = {}
        self.liu_nian_dou_jun = "子"

    def append_start(self, location, star):
        self.star_loaction[star] = location

    def pai_pan(self):
        self.step1()
        self.step2()
        self.step3()
        self.step4()  # 安流年星，现在是按出生年安

    def step1(self):
        """
        安命宫和身宫
        定五行局
        :return:
        """
        # 安命宫和身宫
        m = Ming_Shen_Gong(self.pan_time.yue, self.pan_time.sdz)
        self.ming_gong_location = m.ming
        self.shen_gong_location = m.shen
        # 安余宫和他们的天干
        yu = Yu_Gong(self.ming_gong_location)
        gong_tian_gan = Shi_Er_Gong_Tian_Gan(self.pan_time.ntg)
        for g, in self.gongs.keys():
            self.gongs.get(g).set_name(yu.__getattribute__(g))  # 设置十二宫名
            self.gongs.get(g).set_tian_gan(gong_tian_gan.__getattribute__(g))  # 设置十二宫年干

        # 确定五行局和起运年龄
        wx = Wu_Xing(self.pan_time.ntg, self.ming_gong_location)
        res = wx.get_wu_xing()
        self.wu_xing_jv_name = res[1]
        self.start_age = res[0]
        self.yin_yang = shi_gan_biao.get(self.pan_time.ntg).yin_yang

        # 确定命主和身主
        self.ming_zhu_xing = Ming_Zhu(self.ming_gong_location).命主
        self.shen_zhu_xing = Shen_Zhu(self.pan_time.ndz).身主

    def step2(self):
        # 安紫微星
        zi_wei_location = zi_wei_biao.get(self.pan_time.ri).get(self.wu_xing_jv_name)
        self.gongs.get(zi_wei_location).append_start(dou_shu_stars.get("紫薇"))
        self.append_start(zi_wei_location, "紫薇")
        # 安北斗主星
        zhu_xing_dic = bei_dou_zhu_xing_biao.get(zi_wei_location)
        tian_fu_location = "not found"
        for star, location in zhu_xing_dic.items():
            self.gongs.get(location).append_start(dou_shu_stars.get(star))
            self.append_start(location, star)
            if star == "天府":
                tian_fu_location = location
        # 安南斗主星
        tian_fu_dic = nan_dou_zhu_xing_biao.get(tian_fu_location)
        for star, location in tian_fu_dic.items():
            self.gongs.get(location).append_start(dou_shu_stars.get(star))
            self.append_start(location, star)

        # 安时系诸星
        wen_chang_location = ""
        wen_qu_location = ""
        for star, sub_dic in shi_chen_xing_biao.items():
            location = sub_dic.get(self.pan_time.sdz)
            self.gongs.get(location).append_start(dou_shu_stars.get(star))
            self.append_start(location, star)
            if star == "文昌":
                wen_chang_location = sub_dic.get(self.pan_time.sdz)
            if star == "文曲":
                wen_qu_location = sub_dic.get(self.pan_time.sdz)

        star = "恩光"
        location = CalculateLocation(wen_chang_location, self.pan_time.ri, star_name=star).calculate()
        self.gongs.get(location).append_start(dou_shu_stars.get(star))
        self.append_start(location, star)
        star = "天贵"
        location = CalculateLocation(wen_qu_location, self.pan_time.ri, star_name=star).calculate()
        self.gongs.get(location).append_start(dou_shu_stars.get(star))
        self.append_start(location, star)

        # 安火星铃星
        huo_ling_dic = huo_ling_xing_biao.get(self.pan_time.ndz)
        for star, sub_dic in huo_ling_dic.items():
            location = sub_dic.get(self.pan_time.sdz)
            self.gongs.get(location).append_start(dou_shu_stars.get(star))
            self.append_start(location, star)

        # 安月系诸星
        zuo_fu_loaction = ""
        you_bi_loaction = ""
        yue_xi_dic = yue_xing_biao.get(self.pan_time.yue)
        for star, location in yue_xi_dic.items():
            self.gongs.get(location).append_start(dou_shu_stars.get(star))
            self.append_start(location, star)
            if star == "左辅":
                zuo_fu_loaction = location
            if star == "右弼":
                you_bi_loaction = location

        star = "三台"
        location = CalculateLocation(zuo_fu_loaction, self.pan_time.ri, star_name=star).calculate()
        self.gongs.get(location).append_start(dou_shu_stars.get(star))
        self.append_start(location, star)
        star = "八座"
        location = CalculateLocation(you_bi_loaction, self.pan_time.ri, star_name=star).calculate()
        self.gongs.get(location).append_start(dou_shu_stars.get(star))
        self.append_start(location, star)

        # 安年干系诸星
        sub_dic = nian_gan_xing_biao.get(self.pan_time.ntg)
        for star, location in sub_dic.items():
            self.gongs.get(location).append_start(dou_shu_stars.get(star))
            self.append_start(location, star)

        # 安年支系诸星
        sub_dic = nian_zhi_xing_biao.get(self.pan_time.ndz)
        for star, location in sub_dic.items():
            self.gongs.get(location).append_start(dou_shu_stars.get(star))
            self.append_start(location, star)

        # 安天才，天寿
        t = Tian_Cai_Tian_Show_xing(yue=self.pan_time.yue, shi_zhi=self.pan_time.sdz, nian_zhi=self.pan_time.ndz)
        star = "天才"
        location = t.get_tian_cai_loaction()
        self.gongs.get(location).append_start(dou_shu_stars.get(star))
        self.append_start(location, star)
        star = "天寿"
        location = t.get_tian_show_loaction()
        self.gongs.get(location).append_start(dou_shu_stars.get(star))
        self.append_start(location, star)

        # 安博士二十星
        lu_cun_loaction = self.star_loaction.get("禄存")
        bo_shi_shi_er_xing = Bo_Shi_Shi_Er_Xing(lu_cun_loaction, f"{self.yin_yang}{self.gender}")
        for star in ["博士", "力士", "青龙", "小耗", "将军", "奏书", "飞廉", "喜神", "病符", "大耗", "伏兵", "官府"]:
            location = bo_shi_shi_er_xing.__getattribute__(star)
            self.gongs.get(location).append_start(dou_shu_stars.get(star))
            self.append_start(location, star)

        # 安长生十二星
        sub_dic = chang_sheng_shi_er_xing_biao.get(self.wu_xing_jv_name).get(f"{self.yin_yang}{self.gender}")
        for star, location in sub_dic.items():
            self.gongs.get(location).append_start(dou_shu_stars.get(star))
            self.append_start(location, star)

        # 安截路，空亡
        jielu = Jie_Kong_Xing(self.pan_time.ntg)
        self.gongs.get(jielu.截路).append_start(dou_shu_stars.get("截路"))
        self.append_start(jielu.截路, "截路")
        self.gongs.get(jielu.空亡).append_start(dou_shu_stars.get("空亡"))
        self.append_start(jielu.空亡, "空亡")

        # 安旬中
        location = Xun_Kong_Xing(self.pan_time.ntg, self.pan_time.ndz).旬空
        self.gongs.get(location).append_start(dou_shu_stars.get("旬空"))
        self.append_start(location, "旬空")

        # 安天伤天使
        t = Tian_Shang_Tian_Shi_Xing(self.ming_gong_location)
        star = "天伤"
        location = t.__getattribute__(star)
        self.gongs.get(location).append_start(dou_shu_stars.get(star))
        self.append_start(location, star)
        star = "天使"
        location = t.__getattribute__(star)
        self.gongs.get(location).append_start(dou_shu_stars.get(star))
        self.append_start(location, star)

        # 四化星,
        # TODO 先保存在盘上，排完之后再去找在哪个宫
        sub_dic = si_hua_xing_biao.get(self.pan_time.ntg)
        for hua_star, star in sub_dic.items():
            location = self.star_loaction.get(star)
            self.gongs.get(location).append_start(dou_shu_stars.get(hua_star)(star))

    def step3(self):
        da = Da_Liu_Nian(self.ming_gong_location, self.start_age, f"{self.yin_yang}{self.gender}")
        for zhi in di_zhi.values():
            self.gongs.get(zhi).set_da_xian(da.__getattribute__(zhi))

    def step4(self):
        # TODO 目前搞不清楚这些星是不是每年都会变，但是先按年支固定下来
        ndz = self.pan_time.ndz  # 流年地支
        yue = self.pan_time.yue
        shi_zhi = self.pan_time.sdz
        # 安流年将前诸星表
        sub_dic = Liu_Nian_Xing(ndz).get_jiang_xing()
        for star, location in sub_dic.items():
            self.gongs.get(location).append_start(dou_shu_stars.get(star))
            self.append_start(location, star)

        # 安流年岁前诸星表
        sub_dic = Liu_Nian_Xing(ndz).get_sui_jian_biao()
        for star, location in sub_dic.items():
            self.gongs.get(location).append_start(dou_shu_stars.get(star))
            self.append_start(location, star)

        # TODO 安流年斗君 ,因为暂时不清楚怎么搞这个斗君流年，所以先不添加到宫里，先放盘上保存
        doujun = Dou_jun(yue, shi_zhi)
        location = doujun.get_liu_nian_location(ndz)
        self.liu_nian_dou_jun = location


if __name__ == '__main__':
    # count = -1
    # from tianji.config.十二支所属表 import di_zhi, Di_Zhi_Iter
    # from tianji.config.十干表 import tian_gan, Tian_Gan_Iter
    #
    # tian_gan_iter = Tian_Gan_Iter("葵")
    # di_zhi_iter = Di_Zhi_Iter(-2)
    # for i in range(60):
    #     count += 1
    #     gan = tian_gan_iter.next()
    #     zhi = di_zhi_iter.next()
    #     print(f'{count}:"{gan}{zhi}",')
    y = 1998
    m = 1
    d = 31
    shi = 6
    y, m, d = PanTime.solar_to_lunar(y, m, d)
    print(y, m, d)
    pt = PanTime(y, m, d, shi)
    pt.get_jie_qi()
    p = Pan(pt, "男")
    p.pai_pan()
    print(p.ba_zi)
    print("------" * 5)
    for dz in di_zhi.values():
        p.gongs.get(dz).pai_pan()
        print("==" * 10, dz, "==" * 10)

    # g = Gong("子")
    # print(g.get_san_fang())
