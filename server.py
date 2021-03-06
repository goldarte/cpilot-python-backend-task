import glob
import random
random.seed()

from agroproto.data.ImageFormat import ImageFormat
from modules.enet_wrapper import AgroProto, EnetServer, Data

images_paths = glob.glob("data/*.jpg")
images = []

for image_path in images_paths:
    with open(image_path, 'rb') as image_file:
        images.append(image_file.read())

enet_server = EnetServer("0.0.0.0", 5555)

while True:
    enet_server.receive_message()
    common_info = {"cte": random.gauss(0.0, 0.05), "speed": random.gauss(5.0, 0.1)}
    send_msg = AgroProto.pack_message(common_info, Data.CommonInfo)
    enet_server.send_message(send_msg)
    index = random.randint(0,4)
    view = {"width": 960, "height": 600, "format": ImageFormat.Jpeg, "data": images[index]}
    send_msg = AgroProto.pack_message(view, Data.View)
    enet_server.send_message(send_msg)
