# -*- coding: UTF-8 -*-
import datetime
def init():

  global chatGroups
  global vT
  global usersDict
  global admins 
  global ADMIN
  global previousDay
  global v18 
  chatGroups =[
  u'纽约租房总群3',
  u'纽约拼车',
  u'纽约二手总群2',
  u'纽约美食',
  u'leetcode天天',
  u'NYU纽约内推找工作群2',
  u'北美CPA',
  u'北美妈妈',
  u'8圣约翰租房',
  u'北美信用',
  u'线上KTV',
  u'北美表情分享',
  u'北美绿卡申请讨论总群',
  u'Pokemon Go北美交流总群',
  u'北美区块链技术交流总群',
  u'高盛内推面试刷题群',
  u'北美股市Trading技术交流总群1'
  ]

  v000= u"您好,NYU纽约加群建群小助手为您服务:)\n"
  v00=u"每天只能加1个群哦;\n"
  v0= u"回复 0 加纽约租房群;\n"
  v1= u"回复 1 加纽约拼车群;\n"
  v2= u"回复 2 加纽约二手货群;\n"
  v3= u"回复 3 加纽约美食约饭群;\n"
  v4= u"回复 4 加北美CS刷题竞赛面试总群;\n"
  v5= u"回复 5 加NYU纽约内推找工作群;\n"
  v6= u"回复 6 加北美CPA,REG天天刷题群;\n"
  v7= u"回复 7 加北美妈妈母婴总群;\n"
  v8= u"回复 8 加圣约翰租房叫车玩乐全攻略群;\n"
  v9= u"回复 9 北美信用卡爱好者总群;\n"
  v10= u"回复 10 加线上KTV开嗓🎙️北美总群;\n"
  v11= u"回复 11 加北美表情分享总群;\n"
  v12= u"回复 12 加北美绿卡申请讨论总群;\n"
  v13= u"回复 13 加Pokemon Go北美交流总群;\n"
  v14= u"回复 14 加北美区块链技术交流总群;\n"
  v15= u"回复 15 加高盛内推面试刷题群;\n"
  v16= u"回复 99 查看【北美加群小助手Jogchat.com】\n 公众号二维码加硅谷、西雅图、三番、UIUC、Purdue等地群(无次数限制)\n"
  v17= u"回复 100 加北美股市Trading技术交流总群1(无次数限制)\n"
  v18= u"微信自动加群群功能已关，请使用我们的网站【北美加群小助手jogchat.com】加入北美各地区Facebook群组。谢谢😊"
  vT =v000+v00+v0+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v16+v17
  
  usersDict = {}
  admins = []
  ADMIN = u'NY纽约加群小助手😃jogchat.com'
  previousDay = datetime.datetime.now().day
