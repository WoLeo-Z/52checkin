# -- coding: utf-8 --
# 吾爱破解签到
import requests
import re


pj_cookie = "htVD_2132_auth=2897TA7ECnKpCg0aBHn4oRx%2FgehZwUJ8%2FVL%2FqtCF5BtAoDtdm6BSFgGLDOt3pf%2BILgs5z0uAMHteRw001A6INaPih7g3;htVD_2132_saltkey=e0q65k0b"
if pj_cookie:
	url = "https://www.52pojie.cn/home.php?mod=task&do=apply&id=2"
	headers = {"cookie": pj_cookie, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4265.0 Safari/537.36 Edg/87.0.644.4"}
	req = requests.get(url, headers=headers).text
	patt = '''<div id="messagetext" class="alert_info"><p>([\s\S]*?)</p>'''
	pattern = re.compile(patt)
	list = re.findall(r'<div id="messagetext" class="alert_info">\n<p>([\s\S]*?)</p>', req, re.M)
	tip = list[0]
	if "您需要先登录才能继续本操作" in tip:
		status = "未登陆 / 登陆失败"
		msg = "cookie失效，请重新获取cookie"
	elif "本期您已申请过此任务" in tip:
		status = "今日已签到"
		msg = "重复签到"
	elif "恭喜" in tip:
		status = "签到成功"
		msg = "任务已完成"
	msg = status + ' - ' + msg + '\n' + tip
	print(msg)
