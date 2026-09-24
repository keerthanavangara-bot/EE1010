import os
import subprocess
from PIL import Image

def process_existing_photo():
	    # Look for exact match or common casing variations
	    filename = "My_photo.jpg"
	        if not os.path.exists(filename):
			        # Try checking lowercase or uppercase variations just in case
			        if os.path.exists("my_photo.jpg"):
				            filename = "my_photo.jpg"
					            elif os.path.exists("My_Photo.jpg"):
						                filename = "My_Photo.jpg"
								        else:
									            print(f"Error: Could not find '{filename}' in the current folder: {os.getcwd()}")
										                print("Files available right here:", os.listdir('.'))
												            return

													        print(f"Successfully found and processing: {filename}")
														    
														    # Open the image and convert it to grayscale ('L' mode)
														    img = Image.open(filename)
	    grayscale_img = img.convert('L')
	        
	        width, height = grayscale_img.size
		    pixels = grayscale_img.load()
	    
	    # Thresholding loop (T = 128)
	    threshold = 128
	        for y in range(height):
			        for x in range(width):
					            if pixels[x, y] >= threshold:
						                    pixels[x, y] = 255
							               else:
								                  pixels[x, y] = 0
									                 
									     output_filename = "output_bw.jpg"
									         grayscale_img.save(output_filename)
	    print(f"Done! Opening {output_filename}...")

	        # Automatically trigger your phone's image viewer
	        subprocess.run(["termux-open", output_filename])

		if __name__ == '__main__':
		    process_existing_photo()

