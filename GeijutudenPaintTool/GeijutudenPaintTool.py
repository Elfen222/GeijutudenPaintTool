import cv2
import numpy as np
import struct
import random
from PIL import Image
import os

def get_palette(img):
    palette = []
    cols, rows, _ = img.shape
    for x in range(cols):
        for y in range(rows):
            if((img[x][y].tolist() in palette) == False):
                palette.append(img[x][y].tolist())

    return palette

DIR = []
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/images/_4T_SIDE/')#0
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/images/_10T_SIDE/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/images/_4T_10T_BACK/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/images/_DUMP_SIDE/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/images/_DUMP_BACK/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/images/_FLATED_SIDE/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/images/_FLATED_BACK/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/images/_PROTECTER/')#7

DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output images/_4T_SIDE/')#8
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output images/_10T_SIDE/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output images/_4T_10T_BACK/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output images/_DUMP_SIDE/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output images/_DUMP_BACK/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output images/_FLATED_SIDE/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output images/_FLATED_BACK/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output images/_PROTECTER/')#15

DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output txts/_4T_SIDE/')#16
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output txts/_10T_SIDE/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output txts/_4T_10T_BACK/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output txts/_DUMP_SIDE/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output txts/_DUMP_BACK/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output txts/_FLATED_SIDE/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output txts/_FLATED_BACK/')
DIR.append(os.path.abspath(os.path.dirname(__file__)) + '/output txts/_PROTECTER/')#23

for i in DIR:
    os.makedirs(i, exist_ok=True)

STR = ('４ｔ横','１０ｔ横','４ｔ、１０ｔ後ろ','ダンプ横','ダンプ後ろ','平ボディー横','平ボディー後ろ','ダンプ、平ボディープロテクター')
SIZE = ((176, 64),(224, 64),(64, 64),(108, 40),(64, 40),(186, 36),(72, 36),(64, 28))

for method in range(3):
    for loop in range(8):
        img = []
        directry = []
        files = os.listdir(DIR[loop])
        print('【', STR[loop], '】' + 'メソッド' + str(method))

        for file in files:
            directry.append(file)
        
            print(file)
            img.append(cv2.imread(DIR[loop] + file))

        for i in range(len(img)):
            directry[i] = directry[i][:-4] + '_method' + str(method) + '.png'
            img[i] = cv2.resize(img[i], SIZE[loop], interpolation=cv2.INTER_AREA)
        
            cv2.imwrite(DIR[loop + 8] + directry[i], img[i])

            im = Image.open(DIR[loop + 8] + directry[i])
            im = im.quantize(colors=96, method=method, kmeans = True, dither=1)
            im.save(DIR[loop + 8] + directry[i])
            img[i] = cv2.imread(DIR[loop + 8] + directry[i])

            clist = get_palette(img[i])
            data_list = []

            for x in range(SIZE[loop][1]):
                data_list.append([])
                for y in range(SIZE[loop][0]):
                    data_list[x].append(format(clist.index(img[i][x][y].tolist()), '04x'))

            text = open(DIR[loop + 16] + directry[i].split('.')[0] + '.txt', 'w')

            for x in range(SIZE[loop][1]):
                for y in range (SIZE[loop][0]):
                    text.write('30' +hex(1384460 + x * 224 + y)[2:] + ' ' + data_list[x][y] + '\n')
            for i in np.array(clist):
                i = i[::-1]

            for x in range(len(clist)):
                for y in range(4):
                    if(y != 3):
                        text.write('30' +hex(1470492 + x * 4 + y)[2:] + ' ' + format(int(clist[x][::-1][y]//8.2)*8, '04x') + '\n')
            text.close()
