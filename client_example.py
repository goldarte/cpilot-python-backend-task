from agroproto.data.ImageFormat import ImageFormat
from modules.enet_wrapper import EnetClient, AgroProto, Data, get_property_name

enet_client = EnetClient()

if enet_client.connect("localhost", 5555):
    while True:
        message = enet_client.receive_message()
        if message is not None:
            parsed_data = AgroProto.parse_message(message)
            if parsed_data is not None:
                if parsed_data.type == Data.CommonInfo:
                    print(f"Got parsed cte: {parsed_data.data.cte}, speed: {parsed_data.data.speed}")
                elif parsed_data.type == Data.View:
                    image = parsed_data.data.image
                    image_format = get_property_name(ImageFormat, image.format)
                    print(f"Got {image.width}x{image.height} image in {image_format} format!")
