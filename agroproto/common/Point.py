# automatically generated by the FlatBuffers compiler, do not modify

# namespace: common

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Point(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 8

    # Point
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Point
    def X(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # Point
    def Y(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))

def CreatePoint(builder, x, y):
    builder.Prep(4, 8)
    builder.PrependFloat32(y)
    builder.PrependFloat32(x)
    return builder.Offset()


class PointT(object):

    # PointT
    def __init__(self):
        self.x = 0.0  # type: float
        self.y = 0.0  # type: float

    @classmethod
    def InitFromBuf(cls, buf, pos):
        point = Point()
        point.Init(buf, pos)
        return cls.InitFromObj(point)

    @classmethod
    def InitFromObj(cls, point):
        x = PointT()
        x._UnPack(point)
        return x

    # PointT
    def _UnPack(self, point):
        if point is None:
            return
        self.x = point.X()
        self.y = point.Y()

    # PointT
    def Pack(self, builder):
        return CreatePoint(builder, self.x, self.y)
