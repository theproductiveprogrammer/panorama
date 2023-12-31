from PIL import Image
import os
import sys

if len(sys.argv) != 2:
    exit("usage: panorama <folder with screenshots>");

folder_path = sys.argv[1]

png_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]
print(f"Got {len(png_files)} from {folder_path})")

png_files.sort()

imgs = []
for file in png_files:
    print(f"Opening {file}")
    img = Image.open(os.path.join(folder_path, file))
    img = img.convert("RGBA")
    imgs.append(img)

image_heights = []
max_width = 0
for img in imgs:
    image_heights.append(img.height)
    if img.width > max_width:
        max_width = img.width
total_height = sum(image_heights)

result = Image.new('RGBA', (max_width, total_height))
print(f"Creating output: {max_width}x{total_height}")

current_height = 0
for img, height in zip(imgs, image_heights):
    print(f"Adding image")
    width_diff = max_width - img.width
    position = (width_diff // 2, current_height)
    result.paste(img, position)
    current_height += height

print(f"Saving output.png")
result.save('output.png')

