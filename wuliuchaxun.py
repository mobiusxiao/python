import urllib.request


#单号输入错误提示
def error():
    print ('单号输入错误！无法查找')

    
#查找所属物流
def getType(num):
    typeurl = 'http://www.kuaidi100.com/autonumber/autoComNum?text='+num
    typeweb = urllib.request.urlopen(typeurl)
    dict1 = eval(typeweb.read().decode())
    list1 = dict1['auto']
    if len(list1):
        dict2 = list1[0]
        mailtype = dict2['comCode']
        print ('所属物流：'+ mailtype)
        return mailtype
    else:
        error()
        return 0


#查找物流信息
def getInfo(num,mailtype):
    surl = 'http://www.kuaidi100.com/query?type='+mailtype+'&postid='+num
    sweb = urllib.request.urlopen(surl).read().decode()
    dicts = eval(sweb)
    if dicts['message']=='ok':
        lists = dicts['data']
        for a in lists:
            print ('%s ----- %s' % (a['time'],a['context']))
    else:
        error()
        

num = str(input('输入快递单号(输入exit退出)：'))

while num != 'exit':
    mailtype = getType(num)
        
    if mailtype:
        getInfo(num,mailtype)
    else:
        pass

    num = str(input('继续查询请输入快递单号(输入exit退出)：'))

ex = input('查询结束，按回车关闭程序！')
