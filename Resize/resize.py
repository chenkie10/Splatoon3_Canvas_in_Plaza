import argparse
from PIL import Image
parser=argparse.ArgumentParser(description="Resize an input image file.")
parser.add_argument('image_file',type=str)
parser.add_argument('--output',type=str,default='Resized.png')
args=parser.parse_args()
try:
    img=Image.open(args.image_file)
    resized_img=img.resize((320,120))

    resized_img.save(args.output)
    print(f'Image successfully resized to {320}x{120}')
except FileNotFoundError:
    print(f"Error: The file '{args.image_file}' does not exist.")
except Exception as e:
    print(f"Error: Unable to resize the image. {e}")

