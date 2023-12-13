#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : "乙"0"乙""丙"/"甲""甲"/"甲""丁" "甲""甲":4"丙"
# @Author  : huangfujue
# @File    : xing_chen_biao_module.py
# @Date    : "乙"0"乙""丙"/"甲""甲"/"甲""丁" 
"""
表示所有用到得星辰
"""
# ----------------------------------------------------------------------------------------------------------------------
# TODO
"""
描述诸星分属南北斗五行并化吉凶信息的类
四化星等级设置为-"甲"-丁，表示所有的星都排干净了才排它们

缺少天厨,先补上
缺少天空,先补上
缺少月德星,先补上
缺少空亡星，先按丙级星补上，
缺少推背星，先按"丁"级星补上，
缺少吊客星，先按串客星补上，

地空地劫改为甲级星耀
左辅右弼改为甲级星耀
天马改为甲级星耀

"""


class Star_Info:
    def __init__(self, level="甲", name="", dou_fen="", zhu_hua="", wuxing_list=[]):
        """
        :param level: 星辰等级("甲"-4)
        :param name: 名称
        :param dou_fen: 属于南北斗的信息，不属于是空字符串
        :param zhu_hua: 这个星辰主的是什么，化的是什么
        :param wuxing_list: 五行所属列表，允许空列表，但不要不传参
        """
        self.level = level
        self.name = name
        self.wuxing_list = wuxing_list
        self.dou_fen = dou_fen
        self.zhu_hua = zhu_hua
        self.info=f"等级:{level}\n 星耀:\n{name}\n 所属:\n{dou_fen}\n 主化:\n{zhu_hua}\n 五行:\n{''.join(wuxing_list)}\n"


class Si_Hua_Xing(Star_Info):
    def __init__(self, level="甲", name="", dou_fen="", zhu_hua="", wuxing_list=[]):
        super().__init__(level, name, dou_fen, zhu_hua, wuxing_list)

    def __call__(self, *args, **kwargs):
        srar_name = args[0]
        self.belong_star = srar_name
        return self


dou_shu_stars = {
    "紫薇": Star_Info("甲", "紫薇", "南北", "尊", ["土"]),
    "天机": Star_Info("甲", "天机", "南三", "善", ["木"]),
    "太阳": Star_Info("甲", "太阳", "南北", "贵", ["火"]),
    "武曲": Star_Info("甲", "武曲", "北六", "财", ["金"]),
    "天同": Star_Info("甲", "天同", "南四", "福", ["水"]),
    "廉贞": Star_Info("甲", "廉贞", "北五", "囚", ["木", "火"]),
    "天府": Star_Info("甲", "天府", "南一", "贤能", ["土"]),
    "太阴": Star_Info("甲", "太阴", "南北", "富", ["水"]),
    "贪狼": Star_Info("甲", "贪狼", "北一", "桃花", ["水", "木"]),
    "巨门": Star_Info("甲", "巨门", "北二", "暗", ["水"]),
    "天相": Star_Info("甲", "天相", "南五", "印", ["水"]),
    "天梁": Star_Info("甲", "天梁", "南二", "阴", ["土"]),
    "七杀": Star_Info("甲", "七杀", "南六", "将星", ["火", "金"]),
    "破军": Star_Info("甲", "破军", "北七", "耗", ["水"]),
    "文昌": Star_Info("甲", "文昌", "南北", "科甲", ["金"]),
    "文曲": Star_Info("甲", "文曲", "北四", "科甲", ["水"]),
    "左辅": Star_Info("甲", "左辅", "南北", "助力", ["土"]),
    "右弼": Star_Info("甲", "右弼", "南北", "助力", ["水"]),

    "天魁": Star_Info("甲", "天魁", "    ", "阳贵", ["火"]),
    "天钺": Star_Info("甲", "天钺", "    ", "阴贵", ["火"]),
    "禄存": Star_Info("甲", "禄存", "北三", "爵禄", ["土"]),
    "擎羊": Star_Info("甲", "擎羊", "北助", "刑", ["火", "金"]),
    "陀罗": Star_Info("甲", "陀罗", "北助", "忌", ["金"]),
    "火星": Star_Info("甲", "火星", "南助", "杀", ["火"]),
    "铃星": Star_Info("甲", "铃星", "南助", "杀", ["火"]),
    "地劫": Star_Info("甲", "地劫", "    ", "多灾", ["火"]),
    "地空": Star_Info("甲", "地空", "    ", "失", ["火"]),
    "天马": Star_Info("甲", "天马", "    ", "主动", ["火"]),

    "化禄": Si_Hua_Xing("四化", "化禄", "    ", "财禄", ["土"]),
    "化权": Si_Hua_Xing("四化", "化权", "    ", "权势", ["木"]),
    "化科": Si_Hua_Xing("四化", "化科", "    ", "声名", ["水"]),
    "化忌": Si_Hua_Xing("四化", "化忌", "    ", "多咎", ["水"]),

    "台辅": Star_Info("乙", "台辅", "    ", "主贵", ["土"]),
    "封诰": Star_Info("乙", "封诰", "    ", "主贵", ["土"]),
    "天刑": Star_Info("乙", "天刑", "    ", "孤克", ["火"]),
    "天姚": Star_Info("乙", "天姚", "    ", "风流", ["水"]),

    "天巫": Star_Info("乙", "天巫", "    ", "升迁", []),
    "天月": Star_Info("乙", "天月", "    ", "主病", []),
    "阴煞": Star_Info("乙", "阴煞", "    ", "主有小人", []),
    "三台": Star_Info("乙", "三台", "    ", "主贵", ["土"]),
    "八座": Star_Info("乙", "八座", "    ", "主贵", ["土"]),
    "恩光": Star_Info("乙", "恩光", "    ", "主受殊恩", ["火"]),
    "天贵": Star_Info("乙", "天贵", "    ", "主贵", ["土"]),
    "天官": Star_Info("乙", "天官", "    ", "贵显", ["土"]),
    "天福": Star_Info("乙", "天福", "    ", "爵禄", ["土"]),
    "解神": Star_Info("乙", "解神", "    ", "解灾", []),
    "博士": Star_Info("丙", "博士", "    ", "聪明", ["水"]),
    "力士": Star_Info("丙", "力士", "    ", "权势", ["火"]),
    "青龙": Star_Info("丙", "青龙", "    ", "喜气", ["水"]),
    "小耗": Star_Info("丙", "小耗", "    ", "耗财、小败", ["火"]),
    "将军": Star_Info("丙", "将军", "    ", "威猛", ["木"]),
    "奏书": Star_Info("丙", "奏书", "    ", "福禄", ["金"]),
    "飞廉": Star_Info("丙", "飞廉", "    ", "孤克", ["火"]),
    "喜神": Star_Info("丙", "喜神", "    ", "吉庆", ["火"]),

    "病符": Star_Info("丙", "病符", "    ", "主灾病", ["水"]),
    "大耗": Star_Info("丙", "大耗", "    ", "退祖、破财、大败", ["火"]),
    "伏兵": Star_Info("丙", "伏兵", "    ", "口舌、是非", ["火"]),
    "官府": Star_Info("丙", "官府", "    ", "口舌、刑仗", ["火"]),
    "天哭": Star_Info("乙", "天哭", "    ", "主忧伤", ["金"]),
    "天虚": Star_Info("乙", "天虚", "    ", "主忧伤", ["土"]),
    "龙池": Star_Info("乙", "龙池", "    ", "主科甲", ["水"]),
    "凤阁": Star_Info("乙", "凤阁", "    ", "主科甲", ["土"]),
    "红鸾": Star_Info("乙", "红鸾", "    ", "主婚姻", ["水"]),
    "天喜": Star_Info("乙", "天喜", "    ", "主喜庆", ["水"]),
    "孤辰": Star_Info("乙", "孤辰", "    ", "主孤", ["火"]),
    "寡宿": Star_Info("乙", "寡宿", "    ", "主寡", ["火"]),
    "蜚廉": Star_Info("乙", "蜚廉", "    ", "主孤克", ["火"]),
    "破碎": Star_Info("乙", "破碎", "    ", "主损耗", ["火"]),
    "天才": Star_Info("乙", "天才", "    ", "主才能", ["木"]),

    "天寿": Star_Info("乙", "天寿", "    ", "主有寿", ["土"]),
    "截路": Star_Info("丙", "截路", "    ", "诸空", []),
    "旬空": Star_Info("丙", "旬空", "    ", "诸空", []),

    "天伤": Star_Info("丙", "天伤", "    ", "虚耗", ["水"]),
    "天使": Star_Info("丙", "天使", "    ", "灾祸", ["水"]),
    "长生": Star_Info("丙", "长生", "    ", "主生发", []),
    "沐浴": Star_Info("丙", "沐浴", "    ", "主桃花", []),
    "冠带": Star_Info("丙", "冠带", "    ", "主喜庆", []),
    "临官": Star_Info("丙", "临官", "    ", "主喜庆", []),
    "帝旺": Star_Info("丙", "帝旺", "    ", "旺壮", []),
    "衰": Star_Info("丙", "衰", "    ", "颓败", []),
    "病": Star_Info("丙", "病", "    ", "疾病", []),
    "死": Star_Info("丙", "死", "    ", "丧亡", []),
    "墓": Star_Info("丙", "墓", "    ", "钦藏", []),
    "绝": Star_Info("丙", "绝", "    ", "绝灭", []),
    "胎": Star_Info("丙", "胎", "    ", "主喜", []),
    "养": Star_Info("丙", "养", "    ", "主福", []),
    # 之后德这些看不到等级德星统统按第四等级处理
    "将星": Star_Info("丁", "将星", "    ", "化凶为吉", []),
    "攀鞍": Star_Info("丁", "攀鞍", "    ", "利功名", []),
    "岁驿": Star_Info("丁", "岁驿", "    ", "利迁动", []),
    "息神": Star_Info("丁", "息神", "    ", "消沉", []),

    "华盖": Star_Info("丁", "华盖", "    ", "孤高", ["木"]),
    "劫煞": Star_Info("丁", "劫煞", "    ", "窍盗", ["火"]),
    "灾煞": Star_Info("丁", "灾煞", "    ", "灾患", []),
    "天煞": Star_Info("丁", "天煞", "    ", "克父、克夫", []),
    "指背": Star_Info("丁", "指背", "    ", "诽谤", []),
    "咸池": Star_Info("丁", "咸池", "    ", "桃花", []),
    "月煞": Star_Info("丁", "月煞", "    ", "克母、克妻", []),
    "亡神": Star_Info("丁", "亡神", "    ", "耗败", []),
    "岁建": Star_Info("丁", "岁建", "    ", "一年休咎", ["火"]),
    "晦气": Star_Info("丁", "晦气", "    ", "主咎", []),
    "丧门": Star_Info("丁", "丧门", "    ", "丧亡", ["木"]),
    "贯索": Star_Info("丁", "贯索", "    ", "狱灾", []),
    "官符": Star_Info("丁", "官符", "    ", "主讼", ["火"]),
    # "小耗": Star_Inf"丁","("小耗", "    ", "小失", ["火"]),    # 重复了，内容在上补充
    # "大耗": Star_Inf"丁","("大耗", "    ", "大败", ["火"]),    # 重复了，内容在上补充
    "龙德": Star_Info("丁", "龙德", "    ", "化凶为吉", []),
    "白虎": Star_Info("丁", "白虎", "    ", "诸凶", ["金"]),
    "天德": Star_Info("丁", "天德", "    ", "化凶为吉", []),
    "串客": Star_Info("丁", "串客", "    ", "孝服", ["火"]),
    # "病符": Star_Info("病符", "    ", "疾厄", []), # 重复了
    # 以下为表里缺少的星
    "天厨": Star_Info("乙", "天厨", "    ", "缺少天厨星", []),
    "月德": Star_Info("乙", "月德", "    ", "缺少月德星", ["木"]),
    "天空": Star_Info("乙", "天空", "    ", "缺少天空星", []),
    "空亡": Star_Info("丙", "空亡", "    ", "缺少空亡星", []),
    "推背": Star_Info("丁", "推背", "    ", "缺少推背星", []),
    "吊客": Star_Info("丁", "吊客", "    ", "缺少吊客星，按串客处理，主孝服", ["火"]),
}

if __name__ == '__main__':
    print(len(dou_shu_stars))
