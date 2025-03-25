import imageio
import os

print(os.listdir("source"))

for i in os.listdir("source"):
    name = f'videos/{i[:-4]}'
    os.makedirs(name, exist_ok=True)

    reader = imageio.get_reader(f'source/{i}')

    for frame_number, im in enumerate(reader):
        # im is numpy array
        if frame_number % 1 == 0:
            imageio.imwrite(f'{name}/frame_{frame_number}.jpg', im)