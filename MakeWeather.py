# -* - coding: UTF-8 -* -
a = ["北京","天津","哈尔滨","乌鲁木齐","西宁","兰州","银川","呼和浩特","石家庄","太原","沈阳","长春","济南","拉萨","成都","昆明","西安","郑州","重庆","武汉","长沙","贵阳","南京","合肥","上海","杭州","南昌","福州","广州","南宁","海口","台北","香港","澳门","厦门","青岛","大连","无锡","桂林"]
a1 = ["元旦","春节","元宵节","妇女节","植树节","清明节","劳动节","青年节","端午节","儿童节","建军节","中秋节","教师节","重阳节","国庆节","除夕","情人节","七夕情人节","愚人节","圣诞节","感恩节","复活节"]
#a11 = ["1月1日","1号","腊月一号","10月1日"]
a2 = ["今天","明天","后天","昨天","前天"]
a3 = ["上午","早上","早晨","中午","下午","晚上"]
#a4 = ["10点","两点","2点","一会","过会","2:30"]
a5 = ["周末","周一","星期一","星期二","星期三","星期四","星期五","星期六","星期日","星期天"]
c = ["天气"]
b = ["怎样","怎么样","咋样","好吗","不好吗","如何","好不好","行不行","不好，是不是","好,是不是","不好，是吗 ","好,是吗"]

cb = ["有雨","下雨","有雾","有雾霾","有冰雹","有风","下雪","降雪","降水","降温","降雪","晴天","阴天"]
cb_p = "吗"
#cb1 = ["晴","多云","阴","阵雨","雷阵雨","雷阵雨伴有冰雹","雨夹雪","小雨","中雨","大雨","暴雨","大暴雨","特大暴雨","阵雪","小雪","中雪","大雪","暴雪","雾","冻雨","沙尘暴","小到中雨","中到大雨","大到暴雨","暴雨到大暴雨","大暴雨到特大暴雨","小到中雪"," 中到大雪","大到暴雪","浮尘","扬沙","强沙尘暴","霾"]
#cb1_p = "是" #"吗"
#cb2 = ["多少度","能见度","湿度多少","雨多大","雪多大","风多大"]


#a a1 c b
scanf_file_path = r"./scanf_file.txt"
with open(scanf_file_path,'w') as scanf_file:
    linecount = 0
    # for  ai in a:
    #     for a1i in a1:
    #         for ci in c:
    #             for bi in b:
    #                 linecount += 1
    #                 print(linecount,':')
    #                 print(ai+a1i+ci+bi)

    #a a2 c b
    for  ai in a:
        for a2i in a2:
            for ci in c:
                for bi in b:
                    linecount += 1
                    print(linecount,':')
                    print(ai+a2i+ci+bi)
                    #scanf_file.write(ai+a2i+ci+bi+'\n')

    #a c b
    for  ai in a:
            for ci in c:
                for bi in b:
                    linecount += 1
                    print(linecount,':')
                    print(ai+ci+bi)
                    scanf_file.write(ai+ci+bi+'\n')

    #a1 c b
    for  a1i in a1:
            for ci in c:
                for bi in b:
                    linecount += 1
                    print(linecount,':')
                    print(a1i+ci+bi)
                    #scanf_file.write(a1i+ci+bi+'\n')

    #a cb
    for  ai in a:
            for cbi in cb:
                for cb_pi in cb_p:
                    linecount += 1
                    print(linecount,':')
                    print(ai+cbi+cb_pi)
                    #scanf_file.write(ai+cbi+cb_pi+'\n')

    #a2 c b
    for a2i in a2:
        for ci in c:
            for bi in b:
                linecount += 1
                print(linecount, ':')
                print(a2i + ci + bi)
                #scanf_file.write(a2i + ci + bi+'\n')

    #a3 c b
    for a3i in a3:
        for ci in c:
            for bi in b:
                linecount += 1
                print(linecount, ':')
                print(a3i + ci + bi)
                #scanf_file.write(a3i + ci + bi+'\n')

    #a5 c b
    for a5i in a5:
        for ci in c:
            for bi in b:
                linecount += 1
                print(linecount, ':')
                print(a5i + ci + bi)
                #scanf_file.write(a5i + ci + bi+'\n')
