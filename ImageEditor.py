import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap 
from PyQt5 import QtGui
import tkinter as tk
import tkinter.messagebox as mb

from PIL import Image
from PIL import ImageFilter

app = QApplication([])
win = QWidget()
win.resize(2000, 1000)
win.setStyleSheet("background-color : chartreuse")
win.setWindowIcon(QtGui.QIcon('applogo(.ico)')) #app icon
win.setWindowTitle('PhotoGraf')
lb_image = QLabel("Image")
lb_image.setStyleSheet("background-color : ivory")
btn_dir = QPushButton("Browse:")
btn_dir.setStyleSheet("background-color : orange")
lw_files = QListWidget()
lw_files.setStyleSheet("background-color : white")
btn_dir2 =  QPushButton('Exit')
btn_dir2.setStyleSheet("background-color : red")



btn_left = QPushButton("rotate")
btn_left.setStyleSheet("background-color : green")
btn_right = QPushButton("up/down")
btn_right.setStyleSheet("background-color : green")
btn_flip = QPushButton("mirror")
btn_flip.setStyleSheet("background-color : green")
btn_sharp = QPushButton("blur")
btn_sharp.setStyleSheet("background-color : green")
btn_bw = QPushButton("bw")
btn_bw.setStyleSheet("background-color : green")
btn_save = QPushButton("save") #1
btn_save.setStyleSheet("background-color : yellow") #1
btn_blue = QPushButton("contour") #2
btn_blue.setStyleSheet("background-color : green") #2
btn_rid = QPushButton("embossing") #3
btn_rid.setStyleSheet("background-color : green") #3
btn_fgd = QPushButton("details") #4
btn_fgd.setStyleSheet("background-color : green") #4
btn_hjk = QPushButton("smoothing") #5
btn_hjk.setStyleSheet("background-color : green") #5
btn_poi = QPushButton("clarity of boundaries") #6
btn_poi.setStyleSheet("background-color : green") #6
btn_lkj = QPushButton("boundaries")
btn_lkj.setStyleSheet("background-color : green")
btn_tuy = QPushButton("sharp")
btn_tuy.setStyleSheet("background-color : green")
btn_sdf = QPushButton("boundaries(+)")
btn_sdf.setStyleSheet("background-color : green")
btn_rty = QPushButton("[ + ] crop center (1)") #btn_rty - btn_zo (image crop functions)
btn_rty.setStyleSheet("background-color : Khaki")
btn_rty2 = QPushButton("[+] crop center (2)")
btn_rty2.setStyleSheet("background-color : Khaki")
btn_ty = QPushButton("[  '] right up (1)")
btn_ty.setStyleSheet("background-color : Khaki")
btn_ty2 = QPushButton("['] right up (2)")
btn_ty2.setStyleSheet("background-color : Khaki")
btn_po = QPushButton("[ .] right lower (1)")
btn_po.setStyleSheet("background-color : Khaki")
btn_po2 = QPushButton("[.] right lower (2)")
btn_po2.setStyleSheet("background-color : Khaki")
btn_op = QPushButton("[: :] edges (1)")
btn_op.setStyleSheet("background-color : Khaki")
btn_op2 = QPushButton("[::] edges (2)")
btn_op2.setStyleSheet("background-color : Khaki")
btn_gh = QPushButton("[' ] left up (1)")
btn_gh.setStyleSheet("background-color : Khaki")
btn_gh2 = QPushButton("['] left up (2)")
btn_gh2.setStyleSheet("background-color : Khaki")
btn_jo = QPushButton("[. ] left lower (1)")
btn_jo.setStyleSheet("background-color : Khaki")
btn_jo2 = QPushButton("[.] left lower (2)")
btn_jo2.setStyleSheet("background-color : Khaki")
btn_zo = QPushButton("[ { } ] zoom")
btn_zo.setStyleSheet("background-color : Khaki")

row = QHBoxLayout()          
col1 = QVBoxLayout()         
col2 = QVBoxLayout()
col3 = QVBoxLayout()
col5 = QVBoxLayout()
col3.addWidget(btn_dir2)
#==============================================|
col1.addWidget(btn_rty)
col1.addWidget(btn_ty) #1
col1.addWidget(btn_po) #2
col1.addWidget(btn_op) #3
col1.addWidget(btn_gh) #4
col1.addWidget(btn_jo) #5
#=======================================|
col1.addWidget(btn_rty2)
col1.addWidget(btn_ty2)
col1.addWidget(btn_po2)
col1.addWidget(btn_op2)
col1.addWidget(btn_gh2)
col1.addWidget(btn_jo2)
col1.addWidget(btn_zo)
#==========================================|
col2.addWidget(btn_dir)     
col2.addWidget(lw_files)
col2.addWidget(btn_save)     
col2.addWidget(lb_image, 95) 
row_tools = QHBoxLayout()    
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_blue)
row_tools.addWidget(btn_rid)
row_tools.addWidget(btn_fgd)
row_tools.addWidget(btn_hjk)
row_tools.addWidget(btn_poi)
row_tools.addWidget(btn_lkj)
row_tools.addWidget(btn_tuy)
row_tools.addWidget(btn_sdf)

col2.addLayout(row_tools)


row.addLayout(col1, 20)
row.addLayout(col2, 80)
row.addLayout(col3, 20)
row.addLayout(col1, 20)
win.setLayout(row)


win.show()


workdir = ''


def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result


def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()


def showFilenamesList():
   extensions = ['.jpg','.jpeg', '.png', '.svg', '.bmp']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)


   lw_files.clear()
   for filename in filenames:
       lw_files.addItem(filename)


btn_dir.clicked.connect(showFilenamesList)

class ImageProcessor():
   def __init__(self):
       self.image = None
       self.dir = None
       self.filename = None
       self.save_dir = "Modified Images/"

   
   def loadImage(self, dir, filename):
       self.dir = dir
       self.filename = filename
       image_path = os.path.join(dir, filename)
       self.image = Image.open(image_path)


   def do_bw(self):
       self.image = self.image.convert("L")
       self.saveImage()
       image_path = os.path.join(self.dir, self.save_dir, self.filename)
       self.showImage(image_path)

   def do_flip(self):
       self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )    
       self.showImage(image_path)

   def do_blur(self):
       self.image = self.image.filter(ImageFilter.BLUR)
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def do_right(self): 
       self.image = self.image.transpose(Image.ROTATE_180)
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def do_left(self):
       self.image = self.image.transpose(Image.ROTATE_270)
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

  def close_window():
    app.quit()

   def do_Cont(self):
       self.image = self.image.filter(ImageFilter.CONTOUR)
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def do_F(self):
       self.image = self.image.filter(ImageFilter.EMBOSS)
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path) 

   def do_D(self):
       self.image = self.image.filter(ImageFilter.DETAIL)
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )  
       self.showImage(image_path)

   def do_G(self):
       self.image = self.image.filter(ImageFilter.SMOOTH_MORE)
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def do_x(self):
       self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def do_I(self):
       self.image = self.image.filter(ImageFilter.FIND_EDGES)
       self.saveImage() 
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       ) 
       self.showImage(image_path)  

   def do_H(self):
       self.image = self.image.filter(ImageFilter.SHARPEN) 
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       ) 
       self.showImage(image_path)

   def do_U(self):
       self.image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)


   def crop_center(self):
       self.image = self.image.crop((400, 0, 900, 500)) 
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename       
       )
       self.showImage(image_path)

   def crop_right(self):
       self.image = self.image.crop((800, -300, 1250, 500))
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def crop_right2(self):
       self.image = self.image.crop((800, 300, 1300, 750)) 
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path) 

   def crop_dance(self):
       self.image = self.image.crop((500, 0, 900, 600))
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def crop_left(self):
       self.image = self.image.crop((0, 0, 600, 400))
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def crop_left2lp(self):
       self.image = self.image.crop((0, 250, 900, 800))
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)
#|============================================================================================
   def crop_center2(self):
       self.image = self.image.crop((0, 250, 900, 800))
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def crop_righttwo(self):
       self.image = self.image.crop((250, 0, 600, 400))
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def crop_righttwo2(self):
       self.image = self.image.crop((150, 200, 500, 300))
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def crop_dance2(self):
       self.image = self.image.crop((0, 250, 900, 800))
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def crop_lefttwo(self):
       self.image = self.image.crop((0, 250, 900, 800))
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def crop_lefttwo2(self):
       self.image = self.image.crop((0, 250, 900, 800))
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def crop_zoom(self):
       self.image = self.image.crop((0, 200, 600, 400))
       self.saveImage()
       image_path = os.path.join(
           workdir, self.save_dir, self.filename
       )
       self.showImage(image_path)

   def saveImage(self):
       path = os.path.join(self.dir, self.save_dir)
       if not(os.path.exists(path) or os.path.isdir(path)):
           os.mkdir(path)
       image_path = os.path.join(path, self.filename)
       self.image.save(image_path)


   def showImage(self, path):
       lb_image.hide()
       pixmapimage = QPixmap(path)
       w, h = lb_image.width(), lb_image.height()
       pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
       lb_image.setPixmap(pixmapimage)
       lb_image.show()

    

def showChosenImage():
   if lw_files.currentRow() >= 0:
       filename = lw_files.currentItem().text()
       workimage.loadImage(workdir, filename)
       image_path = os.path.join(workimage.dir, workimage.filename)
       workimage.showImage(image_path)

    


workimage = ImageProcessor() 
lw_files.currentRowChanged.connect(showChosenImage)


btn_bw.clicked.connect(workimage.do_bw)
btn_flip.clicked.connect(workimage.do_flip)
btn_sharp.clicked.connect(workimage.do_blur)
btn_right.clicked.connect(workimage.do_right)
btn_left.clicked.connect(workimage.do_left)
btn_save.clicked.connect(workimage.saveImage)
btn_blue.clicked.connect(workimage.do_Cont)
btn_rid.clicked.connect(workimage.do_F)
btn_fgd.clicked.connect(workimage.do_D)
btn_hjk.clicked.connect(workimage.do_G)
btn_poi.clicked.connect(workimage.do_x)
btn_lkj.clicked.connect(workimage.do_I)
btn_tuy.clicked.connect(workimage.do_H)
btn_sdf.clicked.connect(workimage.do_U)
btn_rty.clicked.connect(workimage.crop_center)
btn_ty.clicked.connect(workimage.crop_right)
btn_po.clicked.connect(workimage.crop_right2)
btn_op.clicked.connect(workimage.crop_dance)
btn_gh.clicked.connect(workimage.crop_left)
btn_jo.clicked.connect(workimage.crop_left2lp)
btn_zo.clicked.connect(workimage.crop_zoom)
btn_rty2.clicked.connect(workimage.crop_center2)
btn_ty2.clicked.connect(workimage.crop_righttwo)
btn_po2.clicked.connect(workimage.crop_righttwo2)
btn_op2.clicked.connect(workimage.crop_dance2)
btn_gh2.clicked.connect(workimage.crop_lefttwo)
btn_jo2.clicked.connect(workimage.crop_lefttwo2)
btn_dir2.clicked.connect(workimage.close_window)

app.exec()
