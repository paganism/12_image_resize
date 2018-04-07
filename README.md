# Image Resizer

Module takes path to image and resizes it according to your arguments and saves it to the same directory or to the directory which could be set
# Usage Example
```
$ python3.5 image_size.py --path /home/user/images/img.jpg --scale 2

Required parameter:
--path
  required parameter that specifies path to source image
  (ex. --path /tmp/source_image.jpg)

Optional parameters:
--width
  parameter specifies the width of the new image (ex. --width 1280)
--height
  parameter specifies the height of the new image (ex. --height 720)
--scale
  parameter specifies the scale of the new image (ex. --scale 2)
--dest
  parameter specifies the dest directory of the new image (ex. --dest /tmp/)

Parameters  --width and --height can't be uset with parameter --scale and vise versa
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
