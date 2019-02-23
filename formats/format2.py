from manipulation import *

class Format2:

    '''Two images concatenated sideways and text on the top and bottom of the image.'''

    def __init__(
        self,
        image1_path,
        image2_path,
        top_text,
        bottom_text,
        font_path='impact/impact.ttf',
        font_size=9,
        ):

        self.image1_path = image1_path
        self.image2_path = image2_path
        self.top_text = top_text
        self.bottom_text = bottom_text
        self.font_path = font_path
        self.font_size = font_size

    def generate(self):
        img01 = Image.open(self.image1_path)
        img02 = Image.open(self.image2_path)
        merge_image = image_join_along_length(img01, img02, (320, 360), (320, 360))
        top_text_image = text_on_top(self.top_text, merge_image)
        final_img = text_in_bottom(self.bottom_text, top_text_image)
        final_img.filename = 'meme-{}{}.jpg'.format(os.path.basename(self.image1_path).split('.')[0], os.path.basename(self.image2_path).split('.')[0])
        final_img.save(final_img.filename)
        return final_img

    # def generate(self):
    #     img01 = Image.open(self.image1_path)
    #     img02 = Image.open(self.image2_path)
    #     images = map(Image.open, [self.image1_path, self.image2_path])
    #     size = (320, 360)
    #     img1 = img01.resize((320, 360), Image.ANTIALIAS)
    #     img2 = img02.resize((320, 360), Image.ANTIALIAS)
    #     img1.save('short1.jpg')
    #     img2.save('short2.jpg')
    #     images = map(Image.open, ['short1.jpg', 'short2.jpg'])
    #
    #     # widths, heights = zip(*(i.size for i in images))
    #
    #     image_width = 640  # sum(widths)
    #     image_height = 360  # max(heights)
    #     img = Image.new('RGB', (image_width, image_height))
    #     x_offset = 0
    #
    #     for im in images:
    #         img.paste(im, (x_offset, 0))
    #         x_offset += im.size[0]
    #
    #     draw = ImageDraw.Draw(img)
    #     font = ImageFont.truetype(font=self.font_path,
    #                               size=int(image_height
    #                               * self.font_size) // 100)
    #     self.top_text = self.top_text.upper()
    #     self.bottom_text = self.bottom_text.upper()
    #     (char_width, char_height) = font.getsize('A')
    #     chars_per_line = image_width // char_width
    #     top_lines = textwrap.wrap(self.top_text, width=chars_per_line)
    #     bottom_lines = textwrap.wrap(self.bottom_text,
    #             width=chars_per_line)
    #     y = 10
    #
    #     for line in top_lines:
    #         (line_width, line_height) = font.getsize(line)
    #         x = (image_width - line_width) / 2
    #         draw.text((x, y), line, fill='white', font=font)
    #         y += line_height
    #
    #     y = image_height - char_height * len(bottom_lines) - 15
    #
    #     for line in bottom_lines:
    #         (line_width, line_height) = font.getsize(line)
    #         x = (image_width - line_width) / 2
    #         draw.text((x, y), line, fill='white', font=font)
    #         y += line_height
    #
    #     # img.save("meme3.jpg")
    #
    #     img.save('meme-{}{}.jpg'.format(os.path.basename(self.image1_path).split('.'
    #              )[0], os.path.basename(self.image2_path).split('.')[0]))
    #     img.show()
