# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Mustache(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Mustache()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMustache(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Mustache
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Mustache
    def Steering(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # Mustache
    def Points(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 8
            from agroproto.common.Point import Point
            obj = Point()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Mustache
    def PointsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Mustache
    def PointsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Mustache
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Mustache
    def SteererFb(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

def Start(builder): builder.StartObject(4)
def MustacheStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddSteering(builder, steering): builder.PrependFloat64Slot(0, steering, 0.0)
def MustacheAddSteering(builder, steering):
    """This method is deprecated. Please switch to AddSteering."""
    return AddSteering(builder, steering)
def AddPoints(builder, points): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(points), 0)
def MustacheAddPoints(builder, points):
    """This method is deprecated. Please switch to AddPoints."""
    return AddPoints(builder, points)
def StartPointsVector(builder, numElems): return builder.StartVector(8, numElems, 4)
def MustacheStartPointsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartPointsVector(builder, numElems)
def AddType(builder, type): builder.PrependInt8Slot(2, type, 0)
def MustacheAddType(builder, type):
    """This method is deprecated. Please switch to AddType."""
    return AddType(builder, type)
def AddSteererFb(builder, steererFb): builder.PrependFloat64Slot(3, steererFb, 0.0)
def MustacheAddSteererFb(builder, steererFb):
    """This method is deprecated. Please switch to AddSteererFb."""
    return AddSteererFb(builder, steererFb)
def End(builder): return builder.EndObject()
def MustacheEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)
import agroproto.common.Point
try:
    from typing import List
except:
    pass

class MustacheT(object):

    # MustacheT
    def __init__(self):
        self.steering = 0.0  # type: float
        self.points = None  # type: List[agroproto.common.Point.PointT]
        self.type = 0  # type: int
        self.steererFb = 0.0  # type: float

    @classmethod
    def InitFromBuf(cls, buf, pos):
        mustache = Mustache()
        mustache.Init(buf, pos)
        return cls.InitFromObj(mustache)

    @classmethod
    def InitFromObj(cls, mustache):
        x = MustacheT()
        x._UnPack(mustache)
        return x

    # MustacheT
    def _UnPack(self, mustache):
        if mustache is None:
            return
        self.steering = mustache.Steering()
        if not mustache.PointsIsNone():
            self.points = []
            for i in range(mustache.PointsLength()):
                if mustache.Points(i) is None:
                    self.points.append(None)
                else:
                    point_ = agroproto.common.Point.PointT.InitFromObj(mustache.Points(i))
                    self.points.append(point_)
        self.type = mustache.Type()
        self.steererFb = mustache.SteererFb()

    # MustacheT
    def Pack(self, builder):
        if self.points is not None:
            StartPointsVector(builder, len(self.points))
            for i in reversed(range(len(self.points))):
                self.points[i].Pack(builder)
            points = builder.EndVector()
        Start(builder)
        AddSteering(builder, self.steering)
        if self.points is not None:
            AddPoints(builder, points)
        AddType(builder, self.type)
        AddSteererFb(builder, self.steererFb)
        mustache = End(builder)
        return mustache
