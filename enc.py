# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:29:49 2022

@author: Pc
"""
import random


string = ' Attention dation Course and learn the basics.'


char_list_one = ['@@@@','@@','@@@','....','..','...','----','--','---','____','__','___','||||','||','|||','****',
                 '**','***','~~~~','~~','~~~','````','``','```',':::::','::',':::','+++++','++','+++','!!!!','!!!'
                 ,'!!','====','==','===',';;;;',';;',';;;','))))','))',')))','>>>>','>>','>>>','<<<<','<<','<<<',
                 '####','##','###','$$$$','$$','$$$','%%%%','%%','%%%','^^^^','^^^','&&&&','&&','&&&','((((','((','(((',
                 '////','//','///',',,,,',',,',',,,','????','???','??','    ','  ','   ','aaaa','aa','aaa','bbbb','bb','bbb',
                 'cccc','cc','ccc','dddd','ddd','dd','eeee','ee','eee','ffff','ff','fff','gggg','gg','ggg','hhhh','hh',
                 'hhh','iiii','ii','iii','jjjj','jj','jjj','kkkk','kk','kkk','llll','ll',
                 'lll','mmmm','mm','mmm','nnnn','nn','nnn','oooo','oo','ooo','pppp','pp','ppp','qqqq','qq','qqq','rrrr','rrr'
                 ,'rr','ssss','ss','sss','tttt','tt','ttt','uuuu','uu','uuu','vvvv','vv','vvv','wwww','ww','www','xxxx',
                 'xx','xxx','yyyy','yy','yyy','zzzz','zz','zzz','1111','11','111','22','2222','222','3333','333',
                 '4444','44','444','555','5555','55','6666','66','666','777','77','7777','8888','88','999','888','99','9999',
                 '0000','00','000']
char_list_two = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
                 'u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','.',',',':','-',';',' ']
char_assigned = []
control = []
form = []
to_encode = []
char_lenght = []
#encoded = string
print(string[1])

for element in string:
    form.append(string.find(element))
   # print(element)
    to_encode.append(element.lower())
print(to_encode)
to_encode = set(to_encode)
for charss in char_list_two:
    char_to_assign = random.choice(char_list_one)
    if charss in to_encode:
        to_encode = list(map(lambda x: x.replace(charss, str(char_to_assign) + ">"+ charss), to_encode))
        #encoded = string.lower().replace(chars, char_to_assign)
        new_l = char_lenght.append(len(char_to_assign))
       
        
    char_assigned.append(charss + " > " + char_to_assign)
    
    control.append(char_to_assign)

#print(string)
print(to_encode)
print(form)
print(char_assigned)
#print(encoded)
#print(control)
#print(char_lenght)





