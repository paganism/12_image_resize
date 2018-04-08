from PIL import Image
import argparse
import sys
import os


def get_image(path_to_image):
    image = Image.open(path_to_image)
    return image


def get_new_dimensions(old_dimensions, width, height, scale):
    old_width, old_height = old_dimensions
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
    if scale:
        new_width = int(old_width * scale)
        new_height = int(old_height * scale)
    new_ratio = new_width / new_height
    return new_width, new_height, ratio, new_ratio


def resize_image(image, new_width, new_height):
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_image


def save_resized_image(resized_image, source_path, image_dir):
    width, height = resized_image.size
    source_name, ext = os.path.splitext(os.path.basename(args.path))
    new_image_name = '{}__{}x{}{}'.format(source_name, width, height, ext)
    resized_image.save(os.path.join(image_dir, new_image_name))


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        dest='path',
        required=True,
        help='Path to image file'
    )
    parser.add_argument(
        '--width',
        dest='width',
        type=int,
        required=False,
        default=None
    )
    parser.add_argument(
        '--height',
        dest='height',
        type=int,
        required=False,
        default=None
    )
    parser.add_argument(
        '--scale',
        dest='scale',
        type=float,
        required=False,
        default=None
    )
    parser.add_argument(
        '--dest',
        dest='dest',
        required=False,
        default=None
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    if args.scale and (args.width or args.height):
        sys.exit('Некорректно указаны аргументы')
    if not os.path.exists(args.path):
        sys.exit('Файл по указанному пути не существует')
    image = get_image(args.path)
    old_dimensions = image.size
    if not args.dest:
        image_dir = os.path.dirname(args.path)
    else:
        image_dir = args.dest
    source_format = image.format
    new_width, new_height, ratio, new_ratio = get_new_dimensions(
        old_dimensions, args.width, args.height, args.scale)
    if ratio != new_ratio:
        print('Соотношение сторон изменено')
    resized_image = resize_image(image, new_width, new_height)
    save_resized_image(resized_image, args.path, image_dir)
