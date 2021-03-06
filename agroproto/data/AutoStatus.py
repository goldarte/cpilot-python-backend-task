# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AutoStatus(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AutoStatus()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAutoStatus(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # AutoStatus
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AutoStatus
    def IsAutoEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # AutoStatus
    def IsAutoAvailable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # AutoStatus
    def EnabledStatus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # AutoStatus
    def AvailableStatus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # AutoStatus
    def SpeedControllingStatus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from agroproto.data.SpeedControllingStatus import SpeedControllingStatus
            obj = SpeedControllingStatus()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Start(builder): builder.StartObject(5)
def AutoStatusStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddIsAutoEnabled(builder, isAutoEnabled): builder.PrependBoolSlot(0, isAutoEnabled, 0)
def AutoStatusAddIsAutoEnabled(builder, isAutoEnabled):
    """This method is deprecated. Please switch to AddIsAutoEnabled."""
    return AddIsAutoEnabled(builder, isAutoEnabled)
def AddIsAutoAvailable(builder, isAutoAvailable): builder.PrependBoolSlot(1, isAutoAvailable, 0)
def AutoStatusAddIsAutoAvailable(builder, isAutoAvailable):
    """This method is deprecated. Please switch to AddIsAutoAvailable."""
    return AddIsAutoAvailable(builder, isAutoAvailable)
def AddEnabledStatus(builder, enabledStatus): builder.PrependUint32Slot(2, enabledStatus, 0)
def AutoStatusAddEnabledStatus(builder, enabledStatus):
    """This method is deprecated. Please switch to AddEnabledStatus."""
    return AddEnabledStatus(builder, enabledStatus)
def AddAvailableStatus(builder, availableStatus): builder.PrependUint32Slot(3, availableStatus, 0)
def AutoStatusAddAvailableStatus(builder, availableStatus):
    """This method is deprecated. Please switch to AddAvailableStatus."""
    return AddAvailableStatus(builder, availableStatus)
def AddSpeedControllingStatus(builder, speedControllingStatus): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(speedControllingStatus), 0)
def AutoStatusAddSpeedControllingStatus(builder, speedControllingStatus):
    """This method is deprecated. Please switch to AddSpeedControllingStatus."""
    return AddSpeedControllingStatus(builder, speedControllingStatus)
def End(builder): return builder.EndObject()
def AutoStatusEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)
import agroproto.data.SpeedControllingStatus
try:
    from typing import Optional
except:
    pass

class AutoStatusT(object):

    # AutoStatusT
    def __init__(self):
        self.isAutoEnabled = False  # type: bool
        self.isAutoAvailable = False  # type: bool
        self.enabledStatus = 0  # type: int
        self.availableStatus = 0  # type: int
        self.speedControllingStatus = None  # type: Optional[agroproto.data.SpeedControllingStatus.SpeedControllingStatusT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        autoStatus = AutoStatus()
        autoStatus.Init(buf, pos)
        return cls.InitFromObj(autoStatus)

    @classmethod
    def InitFromObj(cls, autoStatus):
        x = AutoStatusT()
        x._UnPack(autoStatus)
        return x

    # AutoStatusT
    def _UnPack(self, autoStatus):
        if autoStatus is None:
            return
        self.isAutoEnabled = autoStatus.IsAutoEnabled()
        self.isAutoAvailable = autoStatus.IsAutoAvailable()
        self.enabledStatus = autoStatus.EnabledStatus()
        self.availableStatus = autoStatus.AvailableStatus()
        if autoStatus.SpeedControllingStatus() is not None:
            self.speedControllingStatus = agroproto.data.SpeedControllingStatus.SpeedControllingStatusT.InitFromObj(autoStatus.SpeedControllingStatus())

    # AutoStatusT
    def Pack(self, builder):
        if self.speedControllingStatus is not None:
            speedControllingStatus = self.speedControllingStatus.Pack(builder)
        Start(builder)
        AddIsAutoEnabled(builder, self.isAutoEnabled)
        AddIsAutoAvailable(builder, self.isAutoAvailable)
        AddEnabledStatus(builder, self.enabledStatus)
        AddAvailableStatus(builder, self.availableStatus)
        if self.speedControllingStatus is not None:
            AddSpeedControllingStatus(builder, speedControllingStatus)
        autoStatus = End(builder)
        return autoStatus
