from PIL import Image
import os

def initialise_images():
    images = []
    for i in os.listdir("Images"):
        images.append(Image.open(f"Images\\{i}").convert('RGB'))

    return images

def SaveAsPdf(images):
    books = int(os.listdir("Book")[-1].strip("book").strip(".pdf"))+1
    images[0].save(f'Book\\book{str(books).zfill(3)}.pdf', save_all=True, append_images=images)

def delete_files():
    for i in os.listdir("Images"):
        os.remove(f"Images\\{i}")

if "__main__" == __name__:
    images = initialise_images()
    SaveAsPdf(images)
    delete_files()