# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Warning(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Warning()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsWarning(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Warning
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Warning
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(1)
def WarningStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddType(builder, type): builder.PrependUint32Slot(0, type, 0)
def WarningAddType(builder, type):
    """This method is deprecated. Please switch to AddType."""
    return AddType(builder, type)
def End(builder): return builder.EndObject()
def WarningEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class WarningT(object):

    # WarningT
    def __init__(self):
        self.type = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        warning = Warning()
        warning.Init(buf, pos)
        return cls.InitFromObj(warning)

    @classmethod
    def InitFromObj(cls, warning):
        x = WarningT()
        x._UnPack(warning)
        return x

    # WarningT
    def _UnPack(self, warning):
        if warning is None:
            return
        self.type = warning.Type()

    # WarningT
    def Pack(self, builder):
        Start(builder)
        AddType(builder, self.type)
        warning = End(builder)
        return warning
