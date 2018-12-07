from PIL import Image, ImageFont, ImageDraw
import textwrap
import os


# format-1

def meme_generator_1(
    image_path,
    top_text,
    font_path='impact/impact.ttf',
    font_size=9,
    ):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    (image_width, image_height) = img.size
    font = ImageFont.truetype(font=font_path, size=int(image_height
                              * font_size) // 100)
    top_text = top_text.upper()
    (char_width, char_height) = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    y = 10

    for line in top_lines:
        (line_width, line_height) = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height

    img.save('meme-' + img.filename.split(os.sep)[-1])
    img.show()


# format-2

def meme_generator_2(
    image_path,
    bottom_text,
    font_path='impact/impact.ttf',
    font_size=9,
    ):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    (image_width, image_height) = img.size
    font = ImageFont.truetype(font=font_path, size=int(image_height
                              * font_size) // 100)
    bottom_text = bottom_text.upper()
    (char_width, char_height) = font.getsize('A')
    chars_per_line = image_width // char_width
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)
    y = image_height - char_height * len(bottom_lines) - 15

    for line in bottom_lines:
        (line_width, line_height) = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height

    img.save('meme-' + img.filename.split(os.sep)[-1])
    img.show()


# format-3

def meme_generator_3(
    image_path,
    top_text,
    bottom_text,
    font_path='impact/impact.ttf',
    font_size=9,
    ):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    (image_width, image_height) = img.size
    font = ImageFont.truetype(font=font_path, size=int(image_height
                              * font_size) // 100)
    top_text = top_text.upper()
    bottom_text = bottom_text.upper()
    (char_width, char_height) = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)
    y = 10

    for line in top_lines:
        (line_width, line_height) = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height

    y = image_height - char_height * len(bottom_lines) - 15

    for line in bottom_lines:
        (line_width, line_height) = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height

    img.save('meme-' + img.filename.split(os.sep)[-1])
    img.show()


# format-4

def meme_generator_4(
    image1_path,
    image2_path,
    top_text,
    bottom_text,
    font_path='impact/impact.ttf',
    font_size=9,
    ):
    img01 = Image.open(image1_path)
    img02 = Image.open(image2_path)
    images = map(Image.open, [image1_path, image2_path])
    size = (320, 360)
    img1 = img01.resize((320, 360), Image.ANTIALIAS)
    img2 = img02.resize((320, 360), Image.ANTIALIAS)
    img1.save('short1.jpg')
    img2.save('short2.jpg')
    images = map(Image.open, ['short1.jpg', 'short2.jpg'])

    # widths, heights = zip(*(i.size for i in images))

    image_width = 640  # sum(widths)
    image_height = 360  # max(heights)
    img = Image.new('RGB', (image_width, image_height))
    x_offset = 0

    for im in images:
        img.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font=font_path, size=int(image_height
                              * font_size) // 100)
    top_text = top_text.upper()
    bottom_text = bottom_text.upper()
    (char_width, char_height) = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)
    y = 10

    for line in top_lines:
        (line_width, line_height) = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height

    y = image_height - char_height * len(bottom_lines) - 15

    for line in bottom_lines:
        (line_width, line_height) = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height

    # img.save("meme3.jpg")

    img.save('meme-' + (img01.filename.split('.')[0]
             + img02.filename.split(os.sep)[-1]).split(os.sep)[-1])
    img.show()
