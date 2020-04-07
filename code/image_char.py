from PIL import Image
import sys

chars = ['f', 'u', 'c', 'k', 'p', 'y', 't', 'h', 'o', 'n', '.']

# 对图片进行等比例缩放


def resize_image(image):
    w, h = image.size
    target_w = 100
    aspect_ratio = h/float(w)
    target_h = int(target_w * aspect_ratio * 0.66)
    new_image = image.resize((target_w, target_h))
    return new_image


def convert_image(image):
    gray_image = image.convert('L')
    return gray_image


def get_img_pixel(image):
    pixels = image.getdata()
    return pixels


def change_pixles_to_chars(pixels):
    new_pixels = []

    for pixel_value in pixels:
        index = pixel_value//25
        new_pixels.append(chars[index])

    return ''.join(new_pixels)


def main(image_path):
    image = Image.open(image_path)
    new_image = resize_image(image)
    gray_image = convert_image(new_image)
    pixels = get_img_pixel(gray_image)
    new_pixels = change_pixles_to_chars(pixels)
    len_pixels = len(new_pixels)

    char_image = [new_pixels[index:index+100]
                  for index in range(0, len_pixels, 100)]

    print('\n'.join(char_image))


if __name__ == '__main__':
    image_path = sys.argv[1]
    main(image_path)
