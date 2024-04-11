import numpy as np
from PIL import Image
from collections import Counter

def get_most_common_color(image, box):
    cropped_image = image.crop(box)  # Crop the image to the specified box
    colors = cropped_image.getcolors(cropped_image.width * cropped_image.height)
    most_common_color = max(colors, key=lambda x: x[0])[1]
    return most_common_color

def closest_color_index(color_tuple):
    color_array = np.array(color_tuple)
    distances = np.linalg.norm(indexed_colors - color_array, axis=1)
    closest_index = np.argmin(distances)
    return closest_index

if __name__ == "__main__":

    topological_map = Image.open(r"topographicalmap.png").convert('RGB')

    x_splits = 121
    y_splits = 121

    box_width = topological_map.width/x_splits
    box_height = topological_map.height/y_splits

    indexed_colors = np.array(
            [[255, 255, 255],
            [217, 250, 255],
            [194, 232, 165],
            [167, 212, 125],
            [132, 184, 112],
            [105, 161, 103],
            [78, 138, 93],
            [69, 115, 73],
            [75, 102, 54],
            [83, 92, 41],
            [97, 95, 47],
            [110, 100, 55],
            [120, 102, 59],
            [133, 104, 65]]
            )

    index_map = np.zeros((x_splits, y_splits))

    for y_sec in range(x_splits):
        for x_sec in range(y_splits):
            box = (x_sec*box_width, y_sec*box_height, (x_sec+1)*box_width, (y_sec+1)*box_height)
            index_map[y_sec][x_sec] = closest_color_index(get_most_common_color(topological_map, box))


    # print(index_map)

    output_map = index_map*2.5 - 10

    # print(output_map)

    # Define the file path for the CSV file
    csv_file_path = "topological_map.csv"

    # Export the array to a CSV file
    np.savetxt(csv_file_path, output_map, delimiter=",")