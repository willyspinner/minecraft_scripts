# Given image, fill blocks
import cv2
import numpy as np
from automation_utils import fill_block
import json

blocks_map = None
with open('./block_map.json') as f:
    blocks_map = json.loads(f.read())
    for i in range(len(blocks_map)):
        blocks_map[i]['color'] = np.array(blocks_map[i]['color'])


def find_block_by_color(rgb):
    global blocks_map
    # find nearest color
    print("Finding block for rgb", rgb)
    min_dist = float('inf')
    min_block_id = None
    for block_item in blocks_map:
        dist = np.linalg.norm(rgb - block_item['color'], ord=2)
        if dist < min_dist:
            min_dist = dist
            min_block_id = block_item['id']
    return min_block_id


    # starting_coords is a tuple of (x,y,z), which is the bottom-left of the image.
def write_image_blocks(image_path, starting_coords):
    img = cv2.imread(image_path)
    rows, cols = img.shape[:2]
    x_0, y_0, z_0 = starting_coords
    for i in range(rows):
      for j in range(cols):
          pixel = img[i,j]
          nearest_block = find_block_by_color(pixel)
          fill_block(nearest_block, x_0 + i, y_0 + j, z_0)
if __name__ == "__main__":
    write_image_blocks('/Users/willyspinner/Desktop/royce.png', [10, 10, 10])

