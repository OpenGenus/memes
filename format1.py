from PIL import Image, ImageFont, ImageDraw
import textwrap
import os


class Format1:

    '''Text on the top of the image.'''

    def __init__(
        self,
        image_path,
        top_text,
        font_path='impact/impact.ttf',
        font_size=9,
        ):
        self.image_path = image_path
        self.top_text = top_text
        self.font_path = font_path
        self.font_size = font_size

    def generate(self):
        img = Image.open(self.image_path)

        image = text_on_top(self.top_text, img)

        image.save('meme-' + img.filename.split(os.sep)[-1])
        image.show()

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
