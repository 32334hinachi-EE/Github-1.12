import oled
import time
import sys
import wiringpi
from random import randint
from PIL import ImageFont

print('まだ修正中')    # 自分の担当分の修正が完了したら、この行は削除しておいてください。

def main():    #　main担当： 1. □マークを追加する。  2. ギリギリ○マークが勝てるようにする
    disp, image, draw = oled.oled_setup()
    fsize = 15
    n = 1    #　この部分が〇の固定値
    ifont = ImageFont.truetype('/usr/share/fonts/oled/Shinonome/Shinonome16.ttf',fsize,encoding='unic')
    
    members = [entry(0, fsize, '〇'), entry(0, fsize*2, '△')]    #　この部分に各印（xの位置、yの位置、マーク）が格納されている
    
    while True:
        make(image, draw, ifont, members)
        for m in members:
            if m.pos == fsize:
                m.play(n)    #　〇マークの場合は固定値、それ以外は1-5のランダムな値となっている
            else:
                m.rand(5)
            if m.num >= 100:    #　xの位置が100以上になるとゴール
                m.goal(draw, ifont)
                disp.image(image)
                disp.show()
                return
        disp.image(image)
        disp.show()
        time.sleep(0.1)
        oled.oled_clear(draw)

class entry:
    def __init__(self, num, ps, mk):
        self.num = num
        self.pos = ps
        self.mark = mk
    def rand(self, n):
        self.num = self.num + randint(1,n)
    def play(self, n):
        self.num = switch(self.num, n)
    def goal(self, draw, ifont):    # goal担当：どれかがゴールしたときに"(ゴールしたマーク） WIN !!"を表示する画面に遷移させる
        pass    #　このpassを削除してプログラムを作成する
  
    
def make(image, draw, ifont, members):    # make担当：x座標0に"Start"、100に"Goal"を表示する（yは0でよい）
    for m in members:
        draw.text((m.num,m.pos),m.mark,font=ifont,fill=255)

def switch(cir,n):    # switch担当：固定値となっている○の移動をSW1を押されたとき（長押し可）に移動するようにする　*前回の実験資料参照（SW1は5である）
    cir = cir + n
    return cir        

if __name__ == '__main__':
    main()
