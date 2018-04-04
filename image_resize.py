from PIL import Image
import argparse
import sys
import os


def get_image(path_to_image):
    image = Image.open(path_to_image)
    return image


def resize_image(image, width, height, scale):
    old_width = image.size[0]
    old_height = image.size[1]
    ratio = old_width / old_height
    if not height and width:
        resized_image = image.resize((int(width),
                                      int(int(width) / ratio)),
                                     Image.ANTIALIAS)
    if height and width:
        resized_image = image.resize((int(width),
                                      int(height)),
                                     Image.ANTIALIAS)
    if scale and not all([scale, width]):
        resized_image = image.resize((int(old_width * scale),
                                      int(old_height * scale)),
                                     Image.ANTIALIAS)
    return resized_image


def save_resized_image(resized_image):
    width = resized_image.size[0]
    height = resized_image.size[1]
    resized_image.save('pic__{}x{}.jpg'.format(width, height))


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', dest='path', type=str,
                        required=True, help='Path to image file')
    parser.add_argument('--width', dest='width', type=int,
                        required=False, default=None)
    parser.add_argument('--height', dest='height', type=int,
                        required=False, default=None)
    parser.add_argument('--scale', dest='scale', type=float,
                        required=False, default=None)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    if args.scale and (args.width or args.height) \
            or (args.height and not args.width):
        sys.exit('Некорректно указаны аргументы')
    if not os.path.exists(args.path):
        sys.exit('Файл по указанному пути не существует')
    image = get_image(args.path)
    resized_image = resize_image(image, args.width, args.height, args.scale)
    save_resized_image(resized_image)
