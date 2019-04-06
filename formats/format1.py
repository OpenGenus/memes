import sys
sys.path.append("..")
from services.manipulation import *

class Format1:

    """
    Type 1 -> Text on the top of the image.
    Type 2 -> Text in the bottom of the image.
    Type 3 -> Text on top and bottom of the image.
    """

    def __init__(
        self,
        image_path,
        top_text=None,
        bottom_text=None,
        font_path='impact/impact.ttf',
        font_size=9,
        ):
        self.image_path = image_path
        self.top_text = top_text
        self.bottom_text = bottom_text
        self.font_path = font_path
        self.font_size = font_size

    def generate(self):
        img = Image.open(self.image_path)

        if self.top_text and self.bottom_text:

            img = text_on_top(self.top_text, img)
            image = text_in_bottom(self.bottom_text, img)

        elif self.top_text:

            image = text_on_top(self.top_text, img)

        elif self.bottom_text:

            image = text_in_bottom(self.bottom_text, img)

        #image.save('meme-' + img.filename.split(os.sep)[-1])
        path, imagename =  os.path.split(img.filename)
        img.filename = os.path.join(path,'meme-' + imagename)
        return img

format1type1 = """
Type 1: __________________
        |  Text on top   |
        |                |
        |                |
        |                |
        |________________|

"""
format1type2 = """
Type 2: __________________
        |                |
        |                |
        |                |
        | Text in bottom |
        |________________|

"""
format1type3 = """
Type 3: __________________
        |  Text on top   |
        |                |
        |                |
        | Text in bottom |
        |________________|
"""
    # def generate(self):
    #     img = Image.open(self.image_path)
    #     draw = ImageDraw.Draw(img)
    #     (image_width, image_height) = img.size
    #     font = ImageFont.truetype(font=self.font_path,
    #                               size=int(image_height
    #                               * self.font_size) // 100)
    #     self.top_text = self.top_text.upper()
    #     (char_width, char_height) = font.getsize('A')
    #     chars_per_line = image_width // char_width
    #     top_lines = textwrap.wrap(self.top_text, width=chars_per_line)
    #     y = 10
    #
    #     for line in top_lines:
    #         (line_width, line_height) = font.getsize(line)
    #         x = (image_width - line_width) / 2
    #         draw.text((x, y), line, fill='white', font=font)
    #         y += line_height
    #
    #     img.save('meme-' + img.filename.split(os.sep)[-1])
    #     img.show()
