# this script converts all images in a folder to jpg format
import os


from instagram_util.convert_jpg import convert_to_jpg

# get all images in the queue folder
path = "/Users/blaine/Downloads/Photos-001"
images = os.listdir(path)

# convert all images to jpg
for image in images:
    if image.endswith(".jpg") or image.endswith(".HEIC") or image.endswith(".DS_Store") or image.endswith(".MP4"):
        continue
    else:
        print("converting image to jpg..." + image + "\n")
        convert_to_jpg(os.path.join(path, image))

