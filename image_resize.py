from PIL import Image
import argparse
import sys
import os


def get_image(path_to_image):
    image = Image.open(path_to_image)
    return image


def resize_image(image, width, height, scale):
    old_width, old_height = image.size
    ratio = old_width / old_height
    if not height and width:
        new_height = int(width / ratio)
        new_width = width
    if not width and height:
        new_width = int(height * ratio)
        new_height = height
    if height and width:
        new_width = width
        new_height = height
        if ratio != new_width/new_height:
            print('Соотношение сторон изменено')
    if scale:
        new_width = int(old_width * scale)
        new_height = int(old_height * scale)
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_image


def save_resized_image(resized_image, source_name, source_format, image_dir):
    width, height = resized_image.size
    new_image_name = '{}__{}x{}.{}'.format(source_name,
                                           width, height, source_format)
    resized_image.save(os.path.join(image_dir, new_image_name))


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', dest='path', required=True,
                        help='Path to image file')
    parser.add_argument('--width', dest='width', type=int,
                        required=False, default=None)
    parser.add_argument('--height', dest='height', type=int,
                        required=False, default=None)
    parser.add_argument('--scale', dest='scale', type=float,
                        required=False, default=None)
    parser.add_argument('--dest', dest='dest',
                        required=False, default=None)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    if args.scale and (args.width or args.height):
        sys.exit('Некорректно указаны аргументы')
    if not os.path.exists(args.path):
        sys.exit('Файл по указанному пути не существует')
    image = get_image(args.path)
    source_name, ext = os.path.basename(args.path).split('.')
    if not args.dest:
        image_dir = os.path.dirname(args.path)
    else:
        image_dir = args.dest
    source_format = image.format.lower()
    resized_image = resize_image(image, args.width, args.height, args.scale)
    save_resized_image(resized_image, source_name, ext, image_dir)
