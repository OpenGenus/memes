from definitions import *

class CustomFormat:

    def __init__(
        self,
        images,
        texts,
        font_path='impact/impact.ttf',
        font_size=9
    ):
        self.images = images
        self.texts = texts
        self.font_path = font_path
        self.font_size = font_size

    def generate(self):
        conf, img = self.sequence()
        print(conf)
        img.show()

    def sequence(self):
        conf = list()
        x_offset = 0
        y_offset = 0

        img_path = input("Path of initial image : ")
        img = Image.open(img_path)
        img = img.resize((320,360), Image.ANTIALIAS)

        img = self.put_text(img)

        while True:
            img_path = input('Enter another image path : ')
            ximg = Image.open(img_path)
            ximg = ximg.resize((320,360), Image.ANTIALIAS)

            ximg = self.put_text(ximg)

            res = input("Concat the images (v)ertically or (h)orizontally?")


            if res == "h":

                img = image_join_along_breadth(img, ximg, (None, None), ((int((ximg.size[0]/ximg.size[1])*img.size[1])),img.size[1]))
                img = self.put_text(img)

            if res == "v":

                img = image_join_along_length(img, ximg, (None, None), (img.size[0], (int((ximg.size[1]/ximg.size[0])*img.size[0]))))
                img = self.put_text(img)

            pos = (x_offset, y_offset)

            dict = {'image': img_path,
                    'coordinate': pos}
            conf.append(dict)

            ch = input("Want to add more pictures?(y/n)")

            if ch == 'n':
                break
        return conf, img

    def put_text(self, image):

        res = input('Do you want to enter text to it?(top/bottom/no)')

        if res == 'top':
            text = input('Enter the top text : ')
            image = text_on_top(text, image)

        elif res == 'bottom':
            text = input('Enter the bottom text : ')
            image = text_in_bottom(text, image)

        elif res == 'no' or res == '':
            pass

        return image

CustomObj = CustomFormat("asdasd","asdasdasd")
CustomObj.generate()
