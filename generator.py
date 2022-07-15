from PIL import Image, ImageDraw, ImageFont
import numpy as np  


path = 'E:\\тима.jpg'
symbols = " .:!/r(l1Z4H9W8$@" # 17

def Image_To_Text(path : str, size=175, symbols=symbols) -> str:
    """You put path or link to your image that is SQUARE, 
    size(length) of line that you want to photo be, 
    list of symbols sorted by brightness 
    and get your photo by symbols"""

    with Image.open(path) as img:
        img.thumbnail((size,size))
        arr = np.asarray(img)
    text = ''

    try:
        for x in range(0, size, 2):
            
            for y in range(size):
                RGB = 0             # 765 max
                for canal in arr[x][y]:
                    RGB += canal
                text += symbols[RGB // (765 // len(symbols)) - 1]
            text += '\n'
    except IndexError:
        True
    return text






def Text_To_Image_by_text(path, text=Image_To_Text(path)):
    img = Image.new('RGB', (1050,1040), color=('#000000'))
    font = ImageFont.truetype('C:\Windows\Fonts\CONSOLA.TTF', size=10)
    ImageDraw.Draw(img).text((0, 0), text, font=font, fill=('#F5F5F5'))
    img.save(path,'PNG')
    



# arr=text.split('\n')
# # arr=[[] for x in range(100)]
# # for x in range(100):
# #     for y in range(100):

# #         arr1[x].append()
# colors = [[] for x in range(100)]
# try:
#     for x in range(100):
#         color = symbols.count(arr[x][y]) * 45
#         colors[x].append([color, color,color])
# except:
#     True

# img2 = Image.fromarray(np.uint8(colors)).convert('RGB')
# img2.show()