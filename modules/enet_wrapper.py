import enet
import time
import logging
import flatbuffers
from dataclasses import dataclass

# Agrobox modules
from agroproto.data import DataMessage, CommonInfo, View, Image
from agroproto.data.Data import Data, DataCreator

logger = logging.getLogger(__name__)

seq_num = 0

def get_property_name(cls, _property):
    rev_properties = {y:x for x,y in cls.__dict__.items()}
    return rev_properties[_property]

class ChannelType:
    COMMAND = 0
    DATA = 1
    DISCONNECT_EVENT = 2
    CONNECT_EVENT = 3

class ConnectionType:
    CLIENT = 0
    SERVER = 1

@dataclass
class Message:
    type: ChannelType
    data: bytes

@dataclass
class ParsedData:
    type: Data
    data: object

class Enet():
    def __init__(self):
        # pure enet objects
        self.host = None
        self._peer = None

        # connection settings
        self._connection_host = None
        self._connection_port = None
        self.connection_timeout = 1
        self.connection_timeout_ms = 1000

    def get_event(self):
        return self.host.service(self.connection_timeout_ms)

    def send_message(self, message:Message):
        if self._peer is None:
            return
        flags = 0
        if message.type == ChannelType.COMMAND:
            flags = enet.PACKET_FLAG_RELIABLE
        packet = enet.Packet(message.data, flags)
        self._peer.send(message.type, packet)

    def receive_message(self):
        event = self.get_event()
        if event.type == enet.EVENT_TYPE_CONNECT:
            logger.debug(f"CONNECT to {event.peer.address}")
            self._peer = event.peer
            return Message(ChannelType.CONNECT_EVENT, 0)
        elif event.type == enet.EVENT_TYPE_DISCONNECT:
            logger.debug(f"DISCONNECT from {event.peer.address}.")
            self._peer.reset()
            self._peer = None
            return Message(ChannelType.DISCONNECT_EVENT, 0)
        elif event.type == enet.EVENT_TYPE_RECEIVE:
            return Message(event.channelID, bytes(event.packet.data))

class EnetClient(Enet):
    def __init__(self):
        super().__init__()
        self.host = enet.Host(None, 1, 2, 0, 0)

    def connect(self, host:str, port:int, timeout:float=1.0):
        self._connection_host = host
        self._connection_port = port
        self._connection_address = enet.Address(bytes(host, "ascii"), port)
        self.connection_timeout = timeout
        self.connection_timeout_ms = timeout*1000

        if self.connected():
            try:
                self.disconnect()
            except OSError as e:
                logger.debug(f"Can't disconnect from {self._connection_host}:{self._connection_port}! {e}")

        try:
            self._peer = self.host.connect(self._connection_address, 2)
            if self._peer is not None:
                event = self.get_event()
                if event.type == enet.EVENT_TYPE_CONNECT:
                    logger.info(f"Connected to {event.peer.address}")
                    self.last_action_timestamp = time.time()
                    return self.connected()
            logger.debug(f"No connection to peer on {self._connection_host}:{self._connection_port}")
        except OSError as e:
            logger.debug(f"Can't connect to {self._connection_host}:{self._connection_port}! {e}")

        return False

    def disconnect(self):
        if self._peer is not None:
            self._peer.disconnect()
            event = self.host.service(self.connection_timeout_ms, fast_drop=True)
            while event is not None:
                if event.type == enet.EVENT_TYPE_DISCONNECT:
                    logger.info(f"Successfully disconnected from {event.peer.address}!")
                    return
                event = self.host.service(self.connection_timeout_ms, fast_drop=True)
            self._peer.reset()
            logger.info(f"Force disconnected from {event.peer.address}!")

    def connected(self) -> bool:
        if self._peer is None:
            return False
        return self._peer.state == enet.PEER_STATE_CONNECTED

    def reconnect(self):
        self.connect(self._connection_host, self._connection_port, self.connection_timeout)

class EnetServer(Enet):
    def __init__(self, host:str, port:int, serve_timeout:float=0.1):
        super().__init__()
        self.host = enet.Host(enet.Address(bytes(host, "ascii"), port), 1, 2, 0)
        self.connection_timeout = serve_timeout
        self.connection_timeout_ms = self.connection_timeout*1000

class AgroProto():

    @classmethod
    def parse_message(cls, message:Message):
        if message.type == ChannelType.DATA:
            data_parsed = DataMessage.DataMessage.GetRootAs(message.data)
            msg_type = data_parsed.MessageType()
            return ParsedData(msg_type, DataCreator(msg_type, data_parsed.Message()))

    @classmethod
    def pack_message(cls, data:dict, data_type:Data):
        builder = flatbuffers.Builder(0)
        if data_type == Data.View:
            image_data = builder.CreateByteVector(data["data"])
            Image.Start(builder)
            Image.AddData(builder, image_data)
            Image.AddWidth(builder, data["width"])
            Image.AddHeight(builder, data["height"])
            Image.AddFormat(builder, data["format"])
            image = Image.End(builder)
            View.Start(builder)
            View.AddImage(builder, image)
            message = View.End(builder)
        elif data_type == Data.CommonInfo:
            builder = flatbuffers.Builder(0)
            CommonInfo.Start(builder)
            CommonInfo.AddCte(builder, data.get("cte", 0))
            CommonInfo.AddCteFlt(builder, data.get("cte_flt", 0))
            CommonInfo.AddCteOrigin(builder, data.get("cte_origin", 0))
            CommonInfo.AddSpeed(builder, data.get("speed", 0))
            message = CommonInfo.End(builder)
        DataMessage.Start(builder)
        DataMessage.AddMessageType(builder, data_type)
        DataMessage.AddMessage(builder, message)
        data_message = DataMessage.End(builder)
        builder.Finish(data_message)
        buffer = builder.Output()
        return Message(ChannelType.DATA, bytes(buffer))
