# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:29:49 2022

@author: kagwep
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
key_get1 = []
char_encoder_len = []
to = [0]

def encode():
    for element in string:
        form.append(string.find(element))
       # print(element)
        to_encode.append(element.lower())
        key_get1.append(element.lower())
   # print(to_encode) 
    for charss in to_encode:
        char_to_assign = random.choice(char_list_one)
        char_assigned.append(char_to_assign)
    for check in char_assigned:
        char_len = len(check)
        char_encoder_len.append(char_len)
    print(char_assigned)
    
    global char_assignedToStr
    char_assignedToStr = ''.join([str(elem) for elem in char_assigned])
    print(char_assignedToStr)
key1 = tuple(char_encoder_len)
key2 = key_get1
encode()
decoded = []
def decode():
    
    for i in tuple(char_encoder_len):
        val = to[-1]
        to.append(i + to[-1])
        decoded.append(char_assignedToStr[val:to[-1]])
    #print(decoded)
        
decode()




