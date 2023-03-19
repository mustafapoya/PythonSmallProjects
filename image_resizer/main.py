from PIL import Image
import os

arr = os.listdir('E:/images')


print(arr)

# size_300 = (1680, 1050)

# for f in os.listdir('./images'):
#     if f.endswith(".JPG"):
#         i = Image.open('./images/' + f)
#         fn, fext = os.path.splitext(f)
#         i.thumbnail(size_300)
#         i.save('./images/300/{}_300{}'.format(fn, fext))