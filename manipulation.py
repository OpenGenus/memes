from PIL import Image, ImageFont, ImageDraw
import textwrap
import os

font_path = "impact/impact.ttf"
font_size = 9

def text_on_top (text, image, resize=(None,None)):
    '''
    Input PIL Image object
    Puts text on the top of the image w/r/t the image height and width
    Returns the PIL Image object, its height and width
    '''
    if resize != (None, None):
        image = image.resize(resize, Image.ANTIALIAS)

    draw = ImageDraw.Draw(image)
    (image_width, image_height) = image.size
    font = ImageFont.truetype(font=font_path,
                              size=int(image_height
                              * font_size) // 100)
    text = text.upper()
    (char_width, char_height) = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(text, width=chars_per_line)
    y = 10

    for line in top_lines:
        (line_width, line_height) = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height

    return image

def text_in_bottom (text, image, resize=(None, None)):
    '''
    Input PIL image object
    Puts Text in the bottom of the image w/r/t the image height and width
    Returns the PIL Image object, its height and width
    '''
    if resize != (None, None):
        image = image.resize(resize, Image.ANTIALIAS)

    draw = ImageDraw.Draw(image)
    (image_width, image_height) = image.size
    font = ImageFont.truetype(font=font_path,
                              size=int(image_height
                              * font_size) // 100)
    text = text.upper()
    (char_width, char_height) = font.getsize('A')
    chars_per_line = image_width // char_width
    bottom_lines = textwrap.wrap(text,
                            width=chars_per_line)
    y = image_height - char_height * len(bottom_lines) - 15

    for line in bottom_lines:
        (line_width, line_height) = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height

    return image

def image_join_along_breadth (image1, image2, resize=(None,None)):
    '''
    Concatenates two images side by side
    Input PIL Image obejct
    Returns the PIL Image object, its height and width
    '''

    if size1 != (None, None):
        image1 = image1.resize(size1, Image.ANTIALIAS)
    if size2 != (None, None):
        image2 = image2.resize(size2, Image.ANTIALIAS)

    image1.save('short1.jpg')
    image2.save('short2.jpg')
    images = map(Image.open, ['short1.jpg', 'short2.jpg'])

    image_width = image1.size[0] + image2.size[0]
    image_height = image1.size[1]
    image = Image.new('RGB', (image_width, image_height))
    x_offset = 0

    for im in images:
        image.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    return image

def image_join_along_length (image1, image2, resize=(None, None)):
    '''
    Input PIL Image obejct
    Concatenates images in a top to bottom fashion
    Returns PIL Image object, its height and width
    '''
    if size1 != (None, None):
        image1 = image1.resize(size1, Image.ANTIALIAS)
    if size2 != (None, None):
        image2 = image2.resize(size2, Image.ANTIALIAS)

    image1.save('short1.jpg')
    image2.save('short2.jpg')
    images = map(Image.open, ['short1.jpg', 'short2.jpg'])

    image_width = image1.size[0]
    image_height = image1.size[1] + image2.size[1]
    image = Image.new('RGB', (image_width, image_height))
    y_offset = 0

    for im in images:
        image.paste(im, (0, y_offset))
        y_offset += im.size[1]

    return image

# img = Image.open('data/got_memes/images/got01.jpg')
# img1 = Image.open('data/got_memes/images/got02.jpg')
# img2 = Image.open('data/got_memes/images/got03.jpg')

# op = text_on_top('random text to test the feature', img, resize=(320,360))
# op2 = text_on_top(text='random text to test the feature', image=img1, resize=(320,360))
# op3 = text_in_bottom(text='Plain text data bottom', image=op2)
# op4 = image_join_along_length(op, op3, )
# op5 = text_in_bottom('random bottom text', op3)
# op = text_on_top('Test texttttttt on the toopppppppppppp',op3)
# op.show()
# op2.show()
# op4.show()
