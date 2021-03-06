# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class DataMessage(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DataMessage()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsDataMessage(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # DataMessage
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DataMessage
    def Magic(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 12345

    # DataMessage
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # DataMessage
    def MessageType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # DataMessage
    def Message(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def Start(builder): builder.StartObject(4)
def DataMessageStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddMagic(builder, magic): builder.PrependInt32Slot(0, magic, 12345)
def DataMessageAddMagic(builder, magic):
    """This method is deprecated. Please switch to AddMagic."""
    return AddMagic(builder, magic)
def AddTimestamp(builder, timestamp): builder.PrependInt64Slot(1, timestamp, 0)
def DataMessageAddTimestamp(builder, timestamp):
    """This method is deprecated. Please switch to AddTimestamp."""
    return AddTimestamp(builder, timestamp)
def AddMessageType(builder, messageType): builder.PrependUint8Slot(2, messageType, 0)
def DataMessageAddMessageType(builder, messageType):
    """This method is deprecated. Please switch to AddMessageType."""
    return AddMessageType(builder, messageType)
def AddMessage(builder, message): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(message), 0)
def DataMessageAddMessage(builder, message):
    """This method is deprecated. Please switch to AddMessage."""
    return AddMessage(builder, message)
def End(builder): return builder.EndObject()
def DataMessageEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)
import agroproto.data.AutoStatus
import agroproto.data.CommonInfo
import agroproto.data.Data
import agroproto.data.FWRegulator
import agroproto.data.Gps
import agroproto.data.Mustache
import agroproto.data.TabView
import agroproto.data.View
import agroproto.data.Warning
try:
    from typing import Union
except:
    pass

class DataMessageT(object):

    # DataMessageT
    def __init__(self):
        self.magic = 12345  # type: int
        self.timestamp = 0  # type: int
        self.messageType = 0  # type: int
        self.message = None  # type: Union[None, agroproto.data.Gps.GpsT, agroproto.data.View.ViewT, agroproto.data.TabView.TabViewT, agroproto.data.Mustache.MustacheT, agroproto.data.AutoStatus.AutoStatusT, agroproto.data.CommonInfo.CommonInfoT, agroproto.data.FWRegulator.FWRegulatorT, agroproto.data.Warning.WarningT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        dataMessage = DataMessage()
        dataMessage.Init(buf, pos)
        return cls.InitFromObj(dataMessage)

    @classmethod
    def InitFromObj(cls, dataMessage):
        x = DataMessageT()
        x._UnPack(dataMessage)
        return x

    # DataMessageT
    def _UnPack(self, dataMessage):
        if dataMessage is None:
            return
        self.magic = dataMessage.Magic()
        self.timestamp = dataMessage.Timestamp()
        self.messageType = dataMessage.MessageType()
        self.message = agroproto.data.Data.DataCreator(self.messageType, dataMessage.Message())

    # DataMessageT
    def Pack(self, builder):
        if self.message is not None:
            message = self.message.Pack(builder)
        Start(builder)
        AddMagic(builder, self.magic)
        AddTimestamp(builder, self.timestamp)
        AddMessageType(builder, self.messageType)
        if self.message is not None:
            AddMessage(builder, message)
        dataMessage = End(builder)
        return dataMessage
