import PIL

CARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def sizechange(img, new_width=100):
    width, height = img.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_img = img.resize((new_width, new_height))
    return(resized_img)

def lowersat(img):
    grsc_img = img.convert("L")
    return(grsc_img)
    
def pixelselections(img):
    pixs = img.getdata()
    chars = "".join([CARS[pix//25] for pix in pixs])
    return(chars)    

def drawpls(new_width=100):
    where = input("Pick a god damn jpg file!:\n")
    from PIL import Image
    try:
        image = Image.open(where)
    except:
        print(where, "is invalid af, you die. Now.")
        return
   
    newimgdat = pixelselections(lowersat(sizechange(image)))
    
    countforpix = len(newimgdat)  
    textimg = "\n".join([newimgdat[index:(index+new_width)] for index in range(0, countforpix, new_width)])
    
    print(textimg)
    
    with open("data_output.txt", "w") as f:
        f.write(textimg)

drawpls()