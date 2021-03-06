# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Gps(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Gps()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGps(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Gps
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Gps
    def Nord(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # Gps
    def East(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # Gps
    def Alt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # Gps
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(4)
def GpsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddNord(builder, nord): builder.PrependFloat64Slot(0, nord, 0.0)
def GpsAddNord(builder, nord):
    """This method is deprecated. Please switch to AddNord."""
    return AddNord(builder, nord)
def AddEast(builder, east): builder.PrependFloat64Slot(1, east, 0.0)
def GpsAddEast(builder, east):
    """This method is deprecated. Please switch to AddEast."""
    return AddEast(builder, east)
def AddAlt(builder, alt): builder.PrependFloat64Slot(2, alt, 0.0)
def GpsAddAlt(builder, alt):
    """This method is deprecated. Please switch to AddAlt."""
    return AddAlt(builder, alt)
def AddTimestamp(builder, timestamp): builder.PrependInt64Slot(3, timestamp, 0)
def GpsAddTimestamp(builder, timestamp):
    """This method is deprecated. Please switch to AddTimestamp."""
    return AddTimestamp(builder, timestamp)
def End(builder): return builder.EndObject()
def GpsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class GpsT(object):

    # GpsT
    def __init__(self):
        self.nord = 0.0  # type: float
        self.east = 0.0  # type: float
        self.alt = 0.0  # type: float
        self.timestamp = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        gps = Gps()
        gps.Init(buf, pos)
        return cls.InitFromObj(gps)

    @classmethod
    def InitFromObj(cls, gps):
        x = GpsT()
        x._UnPack(gps)
        return x

    # GpsT
    def _UnPack(self, gps):
        if gps is None:
            return
        self.nord = gps.Nord()
        self.east = gps.East()
        self.alt = gps.Alt()
        self.timestamp = gps.Timestamp()

    # GpsT
    def Pack(self, builder):
        Start(builder)
        AddNord(builder, self.nord)
        AddEast(builder, self.east)
        AddAlt(builder, self.alt)
        AddTimestamp(builder, self.timestamp)
        gps = End(builder)
        return gps
