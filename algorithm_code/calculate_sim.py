# -*- coding: utf-8 -*-

import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import os
import numpy as np
import cv2
from datetime import datetime

#filenames = os.listdir('graph_surf2')
#filenames = [item for item in filenames if item.endswith('_cut2.npy')]
#print (len(filenames), filenames)
filenames = ['Ashes Remain - On My Own.png_all.npy', 'Avril Lavigne - 17.png_all.npy', 'Avril Lavigne - Complicated.png_all.npy', 'Avril Lavigne - Fly.png_all.npy', 'Avril Lavigne - Girlfriend.png_all.npy', 
'Avril Lavigne - Give You What You Like.png_all.npy', 'Avril Lavigne - Hello Kitty.png_all.npy', 
"Avril Lavigne - Here's To Never Growing Up.png_all.npy", 'Avril Lavigne - Hot.png_all.npy', 
'Avril Lavigne - How You Remind Me.png_all.npy', 'Avril Lavigne - I Will Be.png_all.npy', 
'Avril Lavigne - Innocence.png_all.npy', 'Avril Lavigne - Losing Grip.png_all.npy', 
'Avril Lavigne - My Happy Ending.png_all.npy', "Avril Lavigne - Nobody's Home.png_all.npy", 
'Avril Lavigne - Rock N Roll.png_all.npy', 'Avril Lavigne - Runaway.png_all.npy', 
'Avril Lavigne - The Best Damn Thing.png_all.npy', 'Avril Lavigne - Tomorrow.png_all.npy', 
"Avril Lavigne - When You're Gone.png_all.npy", 'Avril Lavigne - Wish You Were Here.png_all.npy', 
'BIGBANG - 하루하루.png_all.npy', 'Blue - One Love.png_all.npy', "Bon Jovi - It's My Life.png_all.npy", 
'Celine Dion - I Surrender.png_all.npy', "Celine Dion - I'm Alive.png_all.npy", 'Celine Dion - My Heart Will Go On.png_all.npy', "Celine Dion - That's the Way It Is.png_all.npy", 'Celine Dion - The Power of Love.png_all.npy', 'Chemistry - Period.png_all.npy', 'Coldplay - Viva La Vida.png_all.npy', 'Derek Duke - Dorado.png_all.npy', 'Derek Duke - Hanamura.png_all.npy', "Derek Duke - King's Row.png_all.npy", 'Derek Duke - Nepal.png_all.npy', 'Derek Duke - Numbani.png_all.npy', 'Derek Duke - Route 66.png_all.npy', 'Derek Duke - Temple of Anubis.png_all.npy', 'Derek Duke - Volskaya Industries.png_all.npy', 'Derek Duke - Watchpoint Gibraltar.png_all.npy', 'Derek Duke,Adam Burgess - Hollywood.png_all.npy', 'Derek Duke,Neal Acree,Neal Acree - Victory.png_all.npy', 'Fall Out Boy - Alone Together.png_all.npy', 'Fall Out Boy - Centuries.png_all.npy', 'Fall Out Boy - Immortals.png_all.npy', 'Fall Out Boy - My Songs Know What You Did In The Dark (Light Em Up).png_all.npy', 'Fall Out Boy - The Phoenix.png_all.npy', 'Fall Out Boy - Uma Thurman.png_all.npy', 'Fall Out Boy - Young Volcanoes.png_all.npy', 'Fall Out Boy,Elton John - Save Rock And Roll (Feat. Elton John).png_all.npy', 'G.E.M.邓紫棋 - 泡沫.png_all.npy', 'Hilary Hahn - Violin Concerto No.5 In A, K.219： II. Adagio.png_all.npy', 'Hilary Hahn - Violin Concerto No.5 In A, K.219： III. Rondeau (Tempo di minuetto).png_all.npy', 'Hillsong Young And Free - Wake.png_all.npy', 'Joy Gruttmann - Schnappi.png_all.npy', 'Kobe Bryant,Tyra Banks - K.O.B.E.png_all.npy', "Lil'B - つないだ手.png_all.npy", 'Linkin Park - Burn It Down (Single Version).png_all.npy', 'Linkin Park - Faint (Album Version).png_all.npy', 'Lube - А зори здесь тихие.png_all.npy', 'Lube - Березы.png_all.npy', 'Lube - Давай за….png_all.npy', 'Lube - Долго.png_all.npy', 'Lube - За бортом.png_all.npy', 'Lube - За тебя, Родина-мать.png_all.npy', 'Lube - Комбат.png_all.npy', 'Lube - Позови меня тихо по имени.png_all.npy', 'Lube - Покосы.png_all.npy', 'Lube - Солдат.png_all.npy', 'Lube - Якоря.png_all.npy', 'Maroon 5 - Moves Like Jagger.png_all.npy', 'Michael Jackson - We Are The World (Demo).png_all.npy', 'NICO Touches the Walls - ホログラム.png_all.npy', 'Nightwish - She Is My Sin.png_all.npy', 'OneRepublic - Counting Stars.png_all.npy', 'Queen - We Are the Champions.png_all.npy', 'Sam Cardon - Overture.png_all.npy', 'Sarah Brightman - Scarborough Fair.png_all.npy', 'Sarah Brightman - Time To Say Goodbye.png_all.npy', 'Sarah Brightman,Andrea Bocelli - Time to Say Goodbye (Con te partirò).png_all.npy', 'Sarah Brightman,刘欢 - 我和你 (You And Me).png_all.npy', 'SCANDAL - 瞬间センチメンタル.png_all.npy', 'Shakira - Try Everything.png_all.npy', 'Sistar19 - 있다 없으니까.png_all.npy', 'The Downtown Fiction - I Just Wanna Run.png_all.npy', 'Willie Nelson - He Was A Friend Of Mine.png_all.npy', 'WINNER - 공허해.png_all.npy', 'WINNER - 컬러링.png_all.npy', 'Wiz Khalifa,Charlie Puth - See You Again.png_all.npy', 'YUI - again.png_all.npy', 'Zard - 愛は暗闇の中で.png_all.npy', 'Zard - 运命のルーレット廻して.png_all.npy', '김지현 - 오나라Ⅱ.png_all.npy', 'シド - レイン.png_all.npy', 'シド - 嘘.png_all.npy', 'スキマスイッチ - ゴールデンタイムラバー.png_all.npy', '中川翔子 - RAY OF LIGHT.png_all.npy', '久石譲 - いつも何度でも.png_all.npy', '久石譲 - スラッグ溪谷の朝.png_all.npy', '久石譲,井上あずみ - 君をのせて.png_all.npy', '五月天 - 小太阳.png_all.npy', '五月天 - 拥抱.png_all.npy', '五月天 - 放肆.png_all.npy', '五月天 - 星空.png_all.npy', '五月天 - 盛夏光年.png_all.npy', '五月天 - 突然好想你.png_all.npy', '五月天,欧开合唱团,乱弹阿翔 - 由我们主宰 The World Is Ours.png_all.npy', '亚历山大红旗歌舞团 - 山楂树.png_all.npy', '信念合唱团 - БРАТЬЯ(兄弟).png_all.npy', '内田光子 - Piano Sonata No.9 in D, K.311 - 1. Allegro con spirito.png_all.npy', '内田光子 - Piano Sonata No.9 in D, K.311 - 2. Andantino con espressione.png_all.npy', '内田光子 - Piano Sonata No.9 in D, K.311 - 3. Rondeau (Allegro).png_all.npy', '周杰伦 - 一路向北.png_all.npy', '周杰伦 - 七里香.png_all.npy', '周杰伦 - 三年二班.png_all.npy', '周杰伦 - 不能说的秘密.png_all.npy', '周杰伦 - 世界末日.png_all.npy', '周杰伦 - 东风破.png_all.npy', '周杰伦 - 借口.png_all.npy', '周杰伦 - 发如雪.png_all.npy', '周杰伦 - 听妈妈的话.png_all.npy', '周杰伦 - 听见下雨的声音.png_all.npy', '周杰伦 - 告白气球.png_all.npy', '周杰伦 - 回到过去.png_all.npy', '周杰伦 - 夜曲.png_all.npy', '周杰伦 - 安静.png_all.npy', '周杰伦 - 彩虹.png_all.npy', '周杰伦 - 我不配.png_all.npy', '周杰伦 - 搁浅.png_all.npy', '周杰伦 - 晴天.png_all.npy', '周杰伦 - 暗号.png_all.npy', '周杰伦 - 最长的电影.png_all.npy', '周杰伦 - 本草纲目.png_all.npy', '周杰伦 - 烟花易冷.png_all.npy', '周杰伦 - 甜甜的.png_all.npy', '周杰伦 - 稻香.png_all.npy', '周杰伦 - 算什么男人.png_all.npy', '周杰伦 - 红尘客栈.png_all.npy', '周杰伦 - 给我一首歌的时间.png_all.npy', '周杰伦 - 菊花台.png_all.npy', '周杰伦 - 蒲公英的约定.png_all.npy', '周杰伦 - 说了再见.png_all.npy', '周杰伦 - 说好的幸福呢.png_all.npy', '周杰伦 - 退后.png_all.npy', '周杰伦 - 青花瓷.png_all.npy', '周杰伦 - 龙卷风.png_all.npy', '周杰伦,Kobe Bryant - 天地一斗.png_all.npy', '周杰伦,梁心颐 - 珊瑚海.png_all.npy', '周杰伦,费玉清 - 千里之外.png_all.npy', '小松未歩 - 哀しい恋.png_all.npy', '朴志胤 - 성인식.png_all.npy', '李昇基 - 정신이 나갔었나봐.png_all.npy', '林俊杰 - Always Online.png_all.npy', '林俊杰 - 一千年以后.png_all.npy', '林俊杰 - 一眼万年.png_all.npy', '林俊杰 - 可惜没如果.png_all.npy', '林俊杰 - 她说.png_all.npy', '林俊杰 - 当你.png_all.npy', '林俊杰 - 江南.png_all.npy', '林俊杰 - 爱笑的眼睛.png_all.npy', '林俊杰 - 第几个一百天.png_all.npy', '林俊杰 - 美人鱼.png_all.npy', '林俊杰 - 背对背拥抱.png_all.npy', '林俊杰 - 转动.png_all.npy', '林俊杰 - 醉赤壁.png_all.npy', '林俊杰,蔡卓妍 - 小酒窝.png_all.npy', '福原美穂 - LET IT OUT.png_all.npy', '竹井詩織里 - 世界 止めて.png_all.npy', '蔡依林,周杰伦 - 布拉格广场.png_all.npy', '袁咏琳,周杰伦 - 画沙.png_all.npy', '郑俊日 - 안아줘.png_all.npy', '金必,金昌万 - 청춘.png_all.npy', '防弹少年团 - 이사.png_all.npy']

filenames = ['Ashes Remain - On My Own.png_cut2.npy', 'Avril Lavigne - 17.png_cut2.npy', 'Avril Lavigne - Complicated.png_cut2.npy', 'Avril Lavigne - Fly.png_cut2.npy', 'Avril Lavigne - Girlfriend.png_cut2.npy', 'Avril Lavigne - Give You What You Like.png_cut2.npy', 'Avril Lavigne - Hello Kitty.png_cut2.npy', "Avril Lavigne - Here's To Never Growing Up.png_cut2.npy", 'Avril Lavigne - Hot.png_cut2.npy', 'Avril Lavigne - How You Remind Me.png_cut2.npy', 'Avril Lavigne - I Will Be.png_cut2.npy', 'Avril Lavigne - Innocence.png_cut2.npy', 'Avril Lavigne - Losing Grip.png_cut2.npy', 'Avril Lavigne - My Happy Ending.png_cut2.npy', "Avril Lavigne - Nobody's Home.png_cut2.npy", 'Avril Lavigne - Rock N Roll.png_cut2.npy', 'Avril Lavigne - Runaway.png_cut2.npy', 'Avril Lavigne - The Best Damn Thing.png_cut2.npy', 'Avril Lavigne - Tomorrow.png_cut2.npy', "Avril Lavigne - When You're Gone.png_cut2.npy", 'Avril Lavigne - Wish You Were Here.png_cut2.npy', 'BIGBANG - 하루하루.png_cut2.npy', 'Blue - One Love.png_cut2.npy', "Bon Jovi - It's My Life.png_cut2.npy", 'Celine Dion - I Surrender.png_cut2.npy', "Celine Dion - I'm Alive.png_cut2.npy", 'Celine Dion - My Heart Will Go On.png_cut2.npy', "Celine Dion - That's the Way It Is.png_cut2.npy", 'Celine Dion - The Power of Love.png_cut2.npy', 'Chemistry - Period.png_cut2.npy', 'Coldplay - Viva La Vida.png_cut2.npy', 'Derek Duke - Dorado.png_cut2.npy', 'Derek Duke - Hanamura.png_cut2.npy', "Derek Duke - King's Row.png_cut2.npy", 'Derek Duke - Nepal.png_cut2.npy', 'Derek Duke - Numbani.png_cut2.npy', 'Derek Duke - Route 66.png_cut2.npy', 'Derek Duke - Temple of Anubis.png_cut2.npy', 'Derek Duke - Volskaya Industries.png_cut2.npy', 'Derek Duke - Watchpoint Gibraltar.png_cut2.npy', 'Derek Duke,Adam Burgess - Hollywood.png_cut2.npy', 'Derek Duke,Neal Acree,Neal Acree - Victory.png_cut2.npy', 'Fall Out Boy - Alone Together.png_cut2.npy', 'Fall Out Boy - Centuries.png_cut2.npy', 'Fall Out Boy - Immortals.png_cut2.npy', 'Fall Out Boy - My Songs Know What You Did In The Dark (Light Em Up).png_cut2.npy', 'Fall Out Boy - The Phoenix.png_cut2.npy', 'Fall Out Boy - Uma Thurman.png_cut2.npy', 'Fall Out Boy - Young Volcanoes.png_cut2.npy', 'Fall Out Boy,Elton John - Save Rock And Roll (Feat. Elton John).png_cut2.npy', 'G.E.M.邓紫棋 - 泡沫.png_cut2.npy', 'Hilary Hahn - Violin Concerto No.5 In A, K.219： II. Adagio.png_cut2.npy', 'Hilary Hahn - Violin Concerto No.5 In A, K.219： III. Rondeau (Tempo di minuetto).png_cut2.npy', 'Hillsong Young And Free - Wake.png_cut2.npy', 'Joy Gruttmann - Schnappi.png_cut2.npy', 'Kobe Bryant,Tyra Banks - K.O.B.E.png_cut2.npy', "Lil'B - つないだ手.png_cut2.npy", 'Linkin Park - Burn It Down (Single Version).png_cut2.npy', 'Linkin Park - Faint (Album Version).png_cut2.npy', 'Lube - А зори здесь тихие.png_cut2.npy', 'Lube - Березы.png_cut2.npy', 'Lube - Давай за….png_cut2.npy', 'Lube - Долго.png_cut2.npy', 'Lube - За бортом.png_cut2.npy', 'Lube - За тебя, Родина-мать.png_cut2.npy', 'Lube - Комбат.png_cut2.npy', 'Lube - Позови меня тихо по имени.png_cut2.npy', 'Lube - Покосы.png_cut2.npy', 'Lube - Солдат.png_cut2.npy', 'Lube - Якоря.png_cut2.npy', 'Maroon 5 - Moves Like Jagger.png_cut2.npy', 'Michael Jackson - We Are The World (Demo).png_cut2.npy', 'NICO Touches the Walls - ホログラム.png_cut2.npy', 'Nightwish - She Is My Sin.png_cut2.npy', 'OneRepublic - Counting Stars.png_cut2.npy', 'Queen - We Are the Champions.png_cut2.npy', 'Sam Cardon - Overture.png_cut2.npy', 'Sarah Brightman - Scarborough Fair.png_cut2.npy', 'Sarah Brightman - Time To Say Goodbye.png_cut2.npy', 'Sarah Brightman,Andrea Bocelli - Time to Say Goodbye (Con te partirò).png_cut2.npy', 'Sarah Brightman,刘欢 - 我和你 (You And Me).png_cut2.npy', 'SCANDAL - 瞬间センチメンタル.png_cut2.npy', 'Shakira - Try Everything.png_cut2.npy', 'Sistar19 - 있다 없으니까.png_cut2.npy', 'The Downtown Fiction - I Just Wanna Run.png_cut2.npy', 'Willie Nelson - He Was A Friend Of Mine.png_cut2.npy', 'WINNER - 공허해.png_cut2.npy', 'WINNER - 컬러링.png_cut2.npy', 'Wiz Khalifa,Charlie Puth - See You Again.png_cut2.npy', 'YUI - again.png_cut2.npy', 'Zard - 愛は暗闇の中で.png_cut2.npy', 'Zard - 运命のルーレット廻して.png_cut2.npy', '김지현 - 오나라Ⅱ.png_cut2.npy', 'シド - レイン.png_cut2.npy', 'シド - 嘘.png_cut2.npy', 'スキマスイッチ - ゴールデンタイムラバー.png_cut2.npy', '中川翔子 - RAY OF LIGHT.png_cut2.npy', '久石譲 - いつも何度でも.png_cut2.npy', '久石譲 - スラッグ溪谷の朝.png_cut2.npy', '久石譲,井上あずみ - 君をのせて.png_cut2.npy', '五月天 - 小太阳.png_cut2.npy', '五月天 - 拥抱.png_cut2.npy', '五月天 - 放肆.png_cut2.npy', '五月天 - 星空.png_cut2.npy', '五月天 - 盛夏光年.png_cut2.npy', '五月天 - 突然好想你.png_cut2.npy', '五月天,欧开合唱团,乱弹阿翔 - 由我们主宰 The World Is Ours.png_cut2.npy', '亚历山大红旗歌舞团 - 山楂树.png_cut2.npy', '信念合唱团 - БРАТЬЯ(兄弟).png_cut2.npy', '内田光子 - Piano Sonata No.9 in D, K.311 - 1. Allegro con spirito.png_cut2.npy', '内田光子 - Piano Sonata No.9 in D, K.311 - 2. Andantino con espressione.png_cut2.npy', '内田光子 - Piano Sonata No.9 in D, K.311 - 3. Rondeau (Allegro).png_cut2.npy', '周杰伦 - 一路向北.png_cut2.npy', '周杰伦 - 七里香.png_cut2.npy', '周杰伦 - 三年二班.png_cut2.npy', '周杰伦 - 不能说的秘密.png_cut2.npy', '周杰伦 - 世界末日.png_cut2.npy', '周杰伦 - 东风破.png_cut2.npy', '周杰伦 - 借口.png_cut2.npy', '周杰伦 - 发如雪.png_cut2.npy', '周杰伦 - 听妈妈的话.png_cut2.npy', '周杰伦 - 听见下雨的声音.png_cut2.npy', '周杰伦 - 告白气球.png_cut2.npy', '周杰伦 - 回到过去.png_cut2.npy', '周杰伦 - 夜曲.png_cut2.npy', '周杰伦 - 安静.png_cut2.npy', '周杰伦 - 彩虹.png_cut2.npy', '周杰伦 - 我不配.png_cut2.npy', '周杰伦 - 搁浅.png_cut2.npy', '周杰伦 - 晴天.png_cut2.npy', '周杰伦 - 暗号.png_cut2.npy', '周杰伦 - 最长的电影.png_cut2.npy', '周杰伦 - 本草纲目.png_cut2.npy', '周杰伦 - 烟花易冷.png_cut2.npy', '周杰伦 - 甜甜的.png_cut2.npy', '周杰伦 - 稻香.png_cut2.npy', '周杰伦 - 算什么男人.png_cut2.npy', '周杰伦 - 红尘客栈.png_cut2.npy', '周杰伦 - 给我一首歌的时间.png_cut2.npy', '周杰伦 - 菊花台.png_cut2.npy', '周杰伦 - 蒲公英的约定.png_cut2.npy', '周杰伦 - 说了再见.png_cut2.npy', '周杰伦 - 说好的幸福呢.png_cut2.npy', '周杰伦 - 退后.png_cut2.npy', '周杰伦 - 青花瓷.png_cut2.npy', '周杰伦 - 龙卷风.png_cut2.npy', '周杰伦,Kobe Bryant - 天地一斗.png_cut2.npy', '周杰伦,梁心颐 - 珊瑚海.png_cut2.npy', '周杰伦,费玉清 - 千里之外.png_cut2.npy', '小松未歩 - 哀しい恋.png_cut2.npy', '朴志胤 - 성인식.png_cut2.npy', '李昇基 - 정신이 나갔었나봐.png_cut2.npy', '林俊杰 - Always Online.png_cut2.npy', '林俊杰 - 一千年以后.png_cut2.npy', '林俊杰 - 一眼万年.png_cut2.npy', '林俊杰 - 可惜没如果.png_cut2.npy', '林俊杰 - 她说.png_cut2.npy', '林俊杰 - 当你.png_cut2.npy', '林俊杰 - 江南.png_cut2.npy', '林俊杰 - 爱笑的眼睛.png_cut2.npy', '林俊杰 - 第几个一百天.png_cut2.npy', '林俊杰 - 美人鱼.png_cut2.npy', '林俊杰 - 背对背拥抱.png_cut2.npy', '林俊杰 - 转动.png_cut2.npy', '林俊杰 - 醉赤壁.png_cut2.npy', '林俊杰,蔡卓妍 - 小酒窝.png_cut2.npy', '福原美穂 - LET IT OUT.png_cut2.npy', '竹井詩織里 - 世界 止めて.png_cut2.npy', '蔡依林,周杰伦 - 布拉格广场.png_cut2.npy', '袁咏琳,周杰伦 - 画沙.png_cut2.npy', '郑俊日 - 안아줘.png_cut2.npy', '金必,金昌万 - 청춘.png_cut2.npy', '防弹少年团 - 이사.png_cut2.npy']

#FLANN_INDEX_KDTREE = 0
#index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 2)
#search_params = dict(checks=10)   # or pass empty dictionary
#flann = cv2.FlannBasedMatcher(index_params,search_params)
def get_sim(start=0, end=49, restart=False):
    bf = cv2.BFMatcher()
    total_cnt = len(filenames)
    if restart:
        with open('sim_result.txt', 'w') as f:
            pass
    for i in range(total_cnt):
        if i < start:
            continue
        nppath1 = 'graph_surf2' + os.sep + filenames[i]
        for j in range(total_cnt):
            start_time = datetime.now()
            if i >= j:
                continue
            print (i, j, 'start...')
            nppath2 = 'graph_surf2' + os.sep + filenames[j]
            desi = np.load(nppath1)
            desj = np.load(nppath2)
            #matches1 = flann.knnMatch(desi, desj, k=1)s
            matches1 = bf.knnMatch(desi, desj, k=1)
            matches1 = [item[0] for item in matches1]
            #matches1 = bf.match(desi, desj)
            sim1 = np.sum([item.distance for item in matches1])
            #matches2 = flann.knnMatch(desj, desi, k=1)
            matches2 = bf.knnMatch(desj, desi, k=1)
            matches2 = [item[0] for item in matches2]
            #matches2 = bf.match(desj, desi)
            sim2 = np.sum([item.distance for item in matches2])
            out1 = filenames[i] + '\t' + filenames[j] + '\t' + str(sim1 / desi.shape[0])
            out2 = filenames[j] + '\t' + filenames[i] + '\t' + str(sim2 / desj.shape[0])
            with open('sim_result.txt', 'a', encoding='utf-8') as f:
                f.write(out1 + '\n')
                f.write(out2 + '\n')
            print (datetime.now() - start_time)
            
        if i == end:
            break
    #f.close()


if __name__ == '__main__':
    get_sim(1, 49)
    