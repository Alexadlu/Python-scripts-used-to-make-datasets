# -*- coding:utf8 -*-
 
import os
class BatchRename():
    '''
    �����������ļ����е�ͼƬ�ļ�
    '''
    def __init__(self):
        self.path = '/home/z/work/train'     #���ͼƬ���ļ���·��
    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
            if item.endswith('.jpg') or item.endswith('.JPG'):  #ͼƬ��ʽΪjpg��JPG
 
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(i).zfill(5) + '.jpg')      #�����µ�ͼƬ����
                try:
                    os.rename(src, dst)
                    print ("converting %s to %s ..." % (src, dst))
                    i = i + 1        
                except:
                    continue
 
        print ("total %d to rename & converted %d jpgs" % (total_num, i))
if __name__ == '__main__':
    demo = BatchRename()
 
    demo.rename()