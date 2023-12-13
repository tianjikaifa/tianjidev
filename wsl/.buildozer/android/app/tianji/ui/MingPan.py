#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/15 14:55
# @Author  : huangfujue
# @File    : MingPanScreenUI.py
# @Date    : 2023/11/15 
"""
表示紫薇斗数的十二个宫的容器
"""

# ----------------------------------------------------------------------------------------------------------------------
from datetime import datetime
from tianji.config.gong import Gong
from tianji.config.zhu_xing_biao_module import bei_dou_zhu_xing_biao, nan_dou_zhu_xing_biao
from tianji.config.wu_xing_jv_biao_module import Wu_Xing
from tianji.config.yu_gong_biao_module import Yu_Gong
from tianji.config.shi_er_gong_tian_gan_biao_module import Shi_Er_Gong_Tian_Gan
from tianji.config.shi_er_di_zhi_biao_module import di_zhi
from tianji.config.shi_gan_biao_module import shi_gan_biao
from tianji.config.bo_shi_shi_er_xing_module import Bo_Shi_Shi_Er_Xing
from tianji.config.ming_gong_shen_gong_module import Ming_Shen_Gong, Ming_Zhu, Shen_Zhu
from tianji.config.da_xian_module import Da_Liu_Nian
from tianji.config.zi_nian_dou_jun_biao_module import Dou_jun
from tianji.config.nian_xi_zhu_xing_biao_module import nian_gan_xing_biao, si_hua_xing_biao, nian_zhi_xing_biao, \
    Tian_Cai_Tian_Show_xing
from tianji.config.nian_xi_zhu_xing_biao_module import Jie_Kong_Xing, Xun_Kong_Xing, Tian_Shang_Tian_Shi_Xing
from tianji.config.ri_xi_zhu_xing_biao_module import CalculateLocation
from tianji.config.shi_xi_zhu_xing_biao_module import shi_chen_xing_biao, huo_ling_xing_biao
from tianji.config.xing_chen_biao_module import dou_shu_stars
from tianji.config.yue_xi_zhu_xing_biao_module import yue_xing_biao
from tianji.config.liu_nian_zhu_xing_biao_module import Liu_Nian_Xing
from tianji.config.qi_zi_wei_biao_module import zi_wei_biao
from tianji.config.chang_sheng_shi_er_xing_module import chang_sheng_shi_er_xing_biao


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
        self.liu_nian_ba_zi=pan_time.liu_nian_ba_zi()

        self.age = datetime.now().year - self.pan_time.nian + 1
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
        self.star_loaction = {}
        self.liu_nian_dou_jun = "子"
        self.pai_pan()

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
        zi_wei_location = zi_wei_biao.get(str(self.pan_time.ri)).get(self.wu_xing_jv_name)
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
        yue_xi_dic = yue_xing_biao.get(str(self.pan_time.yue))
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
        # TODO 目前搞不清楚这些星是不是每年都会变，但是先按流年年算
        ndz = self.liu_nian_ba_zi[1]  # 流年地支
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
