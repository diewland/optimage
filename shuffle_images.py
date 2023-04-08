import glob, json, random, shutil
from pprint import pprint as pp

src_path = "/Users/m1/Desktop/New folder/*.png"
desc_path = "./assets/{}.png"

images = [ path for path in glob.glob(src_path) ]

# shuffle 99 times
for rnd in range(0, 99):
    random.shuffle(images)

#pp(images)
#print(len(images))

# save to desc
for id, src in enumerate(images):
    dest = desc_path.format(id)
    print(src, '->', dest)
    shutil.copyfile(src, dest)
