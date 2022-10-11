import seam_carving as SC
import show_img as SI

numPixel=5
image_goc,image_resized=SC.proceed_doc('paint_smaller.jpg',numPixel)
SI.show(image_goc,'Source')
SI.show(image_resized,'Resized')