from manipulation import *

class Format3:
    """
    This format helps create memes of comparision as decsribed in the
    format_details.md file.
    """

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

        size = (320, 360)
        if self.top_text.__len__() == 1 and self.bottom_text.__len__() == 1:

            merge_image = image_join_along_breadth(img01, img02, (320, 360), (320, 360))
            top_text_image = text_on_top(self.top_text[0], merge_image)

            final_img = text_in_bottom(self.bottom_text[0], top_text_image)

        elif self.top_text.__len__() == 2 and self.bottom_text.__len__() == 1:

            img1 = text_on_top(self.top_text[0], img01, size)
            img2 = text_on_top(self.top_text[1], img02, size)

            final_img = image_join_along_breadth(img1, img2)
            final_img = text_in_bottom(self.bottom_text[0], final_img)

        elif self.bottom_text.__len__() == 2 and self.top_text.__len__() == 1:

            img1 = text_in_bottom(self.bottom_text[0], img01, size)
            img2 = text_in_bottom(self.bottom_text[1], img02, size)

            final_img = image_join_along_breadth(img1, img2)
            final_img = text_on_top(self.top_text[0], final_img)

        elif self.top_text.__len__() == 2 and self.bottom_text.__len__() == 2:

            img1 = text_in_bottom(self.bottom_text[0], img01, size)
            img1 = text_on_top(self.top_text[0], img1, size)

            img2 = text_in_bottom(self.bottom_text[1], img02, size)
            img2 = text_on_top(self.top_text[1], img2, size)

            final_img = image_join_along_breadth(img1, img2)

        final_img.filename ='meme-{}{}.jpg'.format(os.path.basename(self.image1_path).split(
			'.')[0], os.path.basename(self.image2_path).split('.')[0])
        final_img.save(final_img.filename)
        return final_img

format3type1 = """
Type 1:     _______________________
            |    Long top text    |
            |          |          |
            |          |          |
            |   Long bottom text  |
            |__________|__________|
"""
format3type2 = """
Type 2:     _______________________
            |    Long top text    |
            |          |          |
            |          |          |
            |   Text   |   Text   |
            |__________|__________|
"""

format3type3 = """
Type 3:     _______________________
            |    Text  |  Text    |
            |          |          |
            |          |          |
            |  Long bottom text   |
            |_____________________|
"""

format3type4 = """
Type 4:     _______________________
            |   Text   |   Text   |
            |          |          |
            |          |          |
            |   Text   |   Text   |
            |__________|__________|
"""

    # def generate(self):
    #     img01 = Image.open(self.image1_path)
    #     img02 = Image.open(self.image2_path)
    #     images = map(Image.open, [self.image1_path, self.image2_path])
    #
    #     size = (320, 360)
    #     img1 = img01.resize((320, 360), Image.ANTIALIAS)
    #     img2 = img02.resize((320, 360), Image.ANTIALIAS)
    #     img1.save('short1.jpg')
    #     img2.save('short2.jpg')
    #     images = map(Image.open, ['short1.jpg', 'short2.jpg'])
    #
    #     individual_image_width = 320
    #     image_width = 640
    #     image_height = 360
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
    #
    #     self.text_individual1 = self.text_individual1.upper()
    #     self.text_individual2 = self.text_individual2.upper()
    #
    #     (char_width, char_height) = font.getsize('A')
    #     individual_char_per_line = individual_image_width // char_width
    #     char_per_line = image_width // char_width
    #
    #     individual1_lines = textwrap.wrap(self.text_individual1, width=individual_char_per_line)
    #     individual2_lines = textwrap.wrap(self.text_individual2, width=individual_char_per_line)
    #
    #
    #     if self.bottom_text != None:
    #         self.bottom_text = self.bottom_text.upper()
    #         bottom_lines = textwrap.wrap(self.bottom_text, width=char_per_line)
    #
    #         y = image_height - char_height * len(bottom_lines) - 15
    #
    #         for line in bottom_lines:
    #             (line_width, line_height) = font.getsize(line)
    #             x = (image_width - line_width) / 2
    #             draw.text((x, y), line, fill='white', font=font)
    #             y += line_height
    #
    #         if self.text_individual1 != None and self.text_individual2 != None:
    #             y = 10
    #
    #             for line in individual1_lines:
    #                 (line_width, line_height) = font.getsize(line)
    #                 x = (individual_image_width - line_width) / 2
    #                 draw.text((x, y), line, fill='white', font=font)
    #                 y += line_height
    #
    #             y = 10
    #
    #             for line in individual2_lines:
    #                 (line_width, line_height) = font.getsize(line)
    #                 x = 320 + (individual_image_width - line_width) / 2
    #                 draw.text((x, y), line, fill='white', font=font)
    #                 y += line_height
    #
    #     elif self.top_text != None:
    #         self.top_text = self.top_text.upper()
    #         top_lines = textwrap.wrap(self.top_text, width=char_per_line)
    #
    #         y = 10
    #
    #         for line in top_lines:
    #             (line_width, line_height) = font.getsize(line)
    #             x = (image_width - line_width) / 2
    #             draw.text((x, y), line, fill='white', font=font)
    #             y += line_height
    #
    #         if self.text_individual1 != None and self.text_individual2 != None:
    #             y = image_height - char_height * len(individual1_lines) - 15
    #
    #             for line in individual1_lines:
    #                 (line_width, line_height) = font.getsize(line)
    #                 x = (individual_image_width - line_width) / 2
    #                 draw.text((x, y), line, fill='white', font=font)
    #                 y += line_height
    #
    #             y = image_height - char_height * len(individual2_lines) - 15
    #
    #             for line in individual2_lines:
    #                 (line_width, line_height) = font.getsize(line)
    #                 x = 320 + (individual_image_width - line_width) / 2
    #                 draw.text((x, y), line, fill='white', font=font)
    #                 y += line_height

        # img.show()

# ob = Format5(image1_path="data/got_memes/images/got01.jpg",
#             image2_path="data/got_memes/images/got02.jpg",
#             text_individual1="This is a text for image one", text_individual2="This is a text for thie image two",
#             top_text="Hello this it's the top line",
#             bottom_text="this a bottom line text wolla")
# ob.generate()
