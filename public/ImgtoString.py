import os,sys
sys.path.append("..")
from PIL import Image
import pytesseract
		
class Images:
    def __init__(self, img):
        if os.path.exists(img):
            self.img = img
        else:
            raise FileNotFoundError('图片不存在！')
        self._string = None

    @property
    def string(self):
        self.im = Image.open(self.img)
        self.imgry = self.im.convert('L')
        self._string = pytesseract.image_to_string(self.imgry)
        return self._string

    @property
    def string_ch(self):
        self.im = Image.open(self.img)
        self.imgry = self.im.convert('L')
        self._string = pytesseract.image_to_string(self.imgry,lang='chi_sim')
        return self._string

if __name__ == '__main__':
    a = '../img/a.jpg'
    b = '../img/b.jpg'
    c = '../img/c.jpg'
    d = '../img/d.jpg'
    e = '../img/e.jpg'
    print(Images(a).string)
    print(Images(b).string)
    print(Images(c).string)
    print(Images(d).string)
    print(Images(e).string_ch)
		
