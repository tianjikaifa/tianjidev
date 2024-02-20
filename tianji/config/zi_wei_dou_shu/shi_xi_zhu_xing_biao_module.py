#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/13 19:17
# @Author  : huangfujue
# @File    : shi_xi_zhu_xing_biao_module.py
# @Date    : 2023/11/13 
"""
根据出生的时辰和出生年支确定以下这些星在哪个宫
火星、铃星

根据出生时辰直接确定乙级的星在哪个宫
文昌、文曲
地空、地劫
台辅，封诰

根据年支和出生时辰确定的甲级星 火星、铃星
先本生年支，再取对应的星辰，再安出生时辰取值得到该星对应的宫

"""
# ----------------------------------------------------------------------------------------------------------------------



from tianji.config.json_module import huo_ling_xing_biao, shi_chen_xing_biao







if __name__ == '__main__':
    # 先取年支，再取星耀，再取出生时辰
    for nian_zhi in ["寅",
                     "申",
                     "巳",
                     "亥",
                     ]:
        print(nian_zhi)
        for start in ["火星", "铃星"]:
            d = huo_ling_xing_biao.get(nian_zhi).get(start)
            print(start, f"{d.get('子')} {d.get('丑')} {d.get('寅')} {d.get('卯')} {d.get('辰')} "
                         f"{d.get('巳')} {d.get('午')} {d.get('未')} {d.get('申')} {d.get('酉')} {d.get('戌')} {d.get('亥')} ")

    # 直接根据出生时辰确定的星耀
    print("=="*20)

    for start in shi_chen_xing_biao.keys():
        d=shi_chen_xing_biao.get(start)
        print(start, f"{d.get('子')} {d.get('丑')} {d.get('寅')} {d.get('卯')} {d.get('辰')} "
                     f"{d.get('巳')} {d.get('午')} {d.get('未')} {d.get('申')} {d.get('酉')} {d.get('戌')} {d.get('亥')} ")


