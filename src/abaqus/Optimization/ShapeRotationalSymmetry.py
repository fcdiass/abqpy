from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *
from .._decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class ShapeRotationalSymmetry(GeometricRestriction):
    """The ShapeRotationalSymmetry object defines a shape rotational symmetry geometric
    restriction.
    The ShapeRotationalSymmetry object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the vector positioned at the **csys** origin,
    #: used as the axis of symmetry. Instead of through a ConstrainedSketchVertex, each point might be specified
    #: through a tuple of coordinates.
    clientDirection: tuple

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region

    #: A Float specifying the segment size of the repeating pattern in degrees. If the **angle**
    #: value is 0, no repeating pattern is created. The default value is 0.0.
    angle: float = 0

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. The
    #: default value is None.
    csys: int = None

    #: A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
    #: restriction. The default value is TRUE.
    allowNonSymmetricMesh: Boolean = TRUE

    #: None or a Region object specifying the master point used when **masterPointDetermination** is
    #: SPECIFY. The default value is None.
    masterPoint: str = None

    #: A SymbolicConstant specifying the rule for determining the master node. Possible values
    #: are MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.
    masterPointDetermination: SymbolicConstant = MAXIMUM

    #: A Boolean specifying whether to ignore the geometric restriction in the first design
    #: cycle. The default value is ON.
    presumeFeasibleRegionAtStart: Boolean = ON

    #: A tuple of Floats representing the coordinates of a start point of the rotational
    #: symmetry.
    startPoint: float = None

    #: A Float specifying the geometric tolerance in the 1-direction. The default value is
    #: 0.01.
    tolerance1: float = 0

    #: A Float specifying the geometric tolerance in the 2-direction. The default value is
    #: 0.01.
    tolerance2: float = 0

    #: A Float specifying the geometric tolerance in the 3-direction. The default value is
    #: 0.01.
    tolerance3: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        clientDirection: tuple,
        region: Region,
        allowNonSymmetricMesh: Boolean = TRUE,
        angle: float = 0,
        csys: int = None,
        masterPoint: str = None,
        masterPointDetermination: SymbolicConstant = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        startPoint: float = None,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ):
        """This method creates a ShapeRotationalSymmetry object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].optimizationTasks[name].ShapeRotationalSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        clientDirection
            A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the vector positioned at the **csys** origin,
            used as the axis of symmetry. Instead of through a ConstrainedSketchVertex, each point might be specified
            through a tuple of coordinates.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        allowNonSymmetricMesh
            A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
            restriction. The default value is TRUE.
        angle
            A Float specifying the segment size of the repeating pattern in degrees. If the **angle**
            value is 0, no repeating pattern is created. The default value is 0.0.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        masterPoint
            None or a Region object specifying the master point used when **masterPointDetermination** is
            SPECIFY. The default value is None.
        masterPointDetermination
            A SymbolicConstant specifying the rule for determining the master node. Possible values
            are MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        startPoint
            A tuple of Floats representing the coordinates of a start point of the rotational
            symmetry.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.

        Returns
        -------
        ShapeRotationalSymmetry
            A :py:class:`~abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        allowNonSymmetricMesh: Boolean = TRUE,
        angle: float = 0,
        csys: int = None,
        masterPoint: str = None,
        masterPointDetermination: SymbolicConstant = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        startPoint: float = None,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ):
        """This method modifies the ShapeRotationalSymmetry object.

        Parameters
        ----------
        allowNonSymmetricMesh
            A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
            restriction. The default value is TRUE.
        angle
            A Float specifying the segment size of the repeating pattern in degrees. If the **angle**
            value is 0, no repeating pattern is created. The default value is 0.0.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        masterPoint
            None or a Region object specifying the master point used when **masterPointDetermination** is
            SPECIFY. The default value is None.
        masterPointDetermination
            A SymbolicConstant specifying the rule for determining the master node. Possible values
            are MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        startPoint
            A tuple of Floats representing the coordinates of a start point of the rotational
            symmetry.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.
        """
        ...
