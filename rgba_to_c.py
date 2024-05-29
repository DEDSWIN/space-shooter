import numpy as np
import sys

def rgb_to_rgb565(r, g, b):
    r = (r >> 3) & 0x1F
    g = (g >> 2) & 0x3F
    b = (b >> 3) & 0x1F
    return (r << 11) | (g << 5) | b

def read_image(file_path):
    pixels = []
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split()  # Split the RGB values by spaces
            row_pixels = []
            rgb_values = np.array(row, dtype=int).reshape(-1, 4)  # Convert to NumPy array and reshape into triplets
            for rgb_triplet in rgb_values:
                r, g, b, a = rgb_triplet
                rgb565 = rgb_to_rgb565(r, g, b)
                a = (a >> 7) & 0x01
                row_pixels.append((rgb565, a))
            pixels.append(row_pixels)
    return pixels

def generate_c_array(pixels):
    print("{\n", end="")
    for row in pixels:
        print("    {", end="")
        c_array = ""
        for pixel in row:
            c_array += "{" + f"0x{pixel[0]:04X}, 0x{pixel[1]:01X}" + "}, "
            # c_array += f"0x{pixel[0]:04X}, "
        c_array = c_array[:-2]  # Remove the last comma and space
        print(c_array, end="")
        print("},\n", end="")
    print("};", end="")
    # return c_array

def main():
    file_path = "asteroid_pack/big4_colors.txt"  # Update with your file path
    pixels = read_image(file_path)
    old_stdout = sys.stdout
    with open("asteroid_pack/explode.txt", 'w') as new_stdout:
        sys.stdout = new_stdout
        c_array = generate_c_array(pixels)
        sys.stdout = old_stdout
    # print(c_array)

if __name__ == "__main__":
    main()
