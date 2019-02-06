from manipulation import *

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
        self.operations = operations
        self.font_path = font_path
        self.font_size = font_size

    def generate(self):
        text_stack = self.texts.split(',')
        image_stack= list(map(Image.open,self.images.split(',')))
        operation_stack = self.operations.split(',')

        img_col = list()

        while image_stack.__len__() > 1:
            stackop = operation_stack.pop()

            if stackop == '1': # merge side by side
                img2 = self.put_text(image_stack.pop())
                img1 = self.put_text(image_stack.pop())

                img = image_join_along_breadth(img1, img2, (None, None), ((int((img2.size[0]/img2.size[1])*img1.size[1])),img1.size[1]))
                # img = put_text(img)
                image_stack.append(img)

            elif stackop == '2': # merge bottom to top
                img = self.put_text(image_stack.pop())
                img_col.append(img)

        img_col.append(self.put_text(image_stack.pop()))

        while img_col.__len__() > 1:
            img1 = img_col.pop()
            img2 = img_col.pop()
            img = image_join_along_length(img1, img2, (None, None), (img1.size[0], (int((img2.size[1]/img2.size[0])*img1.size[0]))))
            img_col.append(img)

        img_col[0].show()

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

    # def generate(self):
    #     conf, img = self.sequence()
    #     print(conf)
    #     img.show()
    #
    # def sequence(self):
    #     conf = list()
    #     x_offset = 0
    #     y_offset = 0
    #
    #     img_path = input("Path of initial image : ")
    #     img = Image.open(img_path)
    #     img = img.resize((320,360), Image.ANTIALIAS)
    #
    #     img = self.put_text(img)
    #
    #     while True:
    #         img_path = input('Enter another image path : ')
    #         ximg = Image.open(img_path)
    #         ximg = ximg.resize((320,360), Image.ANTIALIAS)
    #
    #         ximg = self.put_text(ximg)
    #
    #         res = input("Concat the images (v)ertically or (h)orizontally?")
    #
    #
    #         if res == "h":
    #
    #             img = image_join_along_breadth(img, ximg, (None, None), ((int((ximg.size[0]/ximg.size[1])*img.size[1])),img.size[1]))
    #             img = self.put_text(img)
    #
    #         if res == "v":
    #
    #             img = image_join_along_length(img, ximg, (None, None), (img.size[0], (int((ximg.size[1]/ximg.size[0])*img.size[0]))))
    #             img = self.put_text(img)
    #
    #         pos = (x_offset, y_offset)
    #
    #         dict = {'image': img_path,
    #                 'coordinate': pos}
    #         conf.append(dict)
    #
    #         ch = input("Want to add more pictures?(y/n)")
    #
    #         if ch == 'n':
    #             break
    #     return conf, img
