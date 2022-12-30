from PIL import  Image,ImageEnhance,ImageFilter,ImageColor
import os
"""
path='D:\Mega_Data_Science\Practice\DSC_0078.JPG'
pathout ='D:\Mega_Data_Science\Practice'
for filename in os.listdir(path):
  img=Image.open(f"{path}/{filename}")
  edit = img.fillter(ImageFilter.SHARPEN).convert('L')
  clean_name= os.path.splitext(filename)[0]
  edit.save(f'.{pathout}/{clean_name}_edited.jpg')
"""
#create a new image by import
image = Image.open('image.JPG')
#alternate way to import an image
#with Image.open(picture.jpg) as image:
 # image.show()
#create a new image from scratch
image_blank=Image.new('RGBA',(1000,600))

#show the image
#image_blank.show()

#saving the picture
#image.save('test_save.png')
 
#IMAGE INFORMATION
#print(image.size)
#print(image.filename)
#print(image.format)
#print(image.size)

#ROTATE 

image_rotate=image.rotate(60,expand=True,fillcolor=ImageColor.getcolor('blue','RGB'))
image_crop=image.crop(left_x,top_y,right_x,bottom_y)
image_rotate.show()



