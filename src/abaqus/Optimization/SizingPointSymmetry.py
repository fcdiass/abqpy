from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *
from .._decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class SizingPointSymmetry(GeometricRestriction):
    """The SizingPointSymmetry object defines a sizing point symmetry geometric restriction.
    The SizingPointSymmetry object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    region: Region

    #: None or a DatumCsys object specifying the position of the symmetry point defined as the
    #: origin of a local coordinate system. If **csys** = None, the global coordinate system is
    #: used. When this member is queried, it returns an Int. The default value is None.
    csys: int = None

    #: A Boolean specifying whether to ignore frozen areas. The default value is OFF.
    ignoreFrozenArea: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        csys: int = None,
        ignoreFrozenArea: Boolean = OFF,
    ):
        """This method creates a SizingPointSymmetry object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].optimizationTasks[name].SizingPointSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys** = None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        SizingPointSymmetry
            A :py:class:`~abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, csys: int = None, ignoreFrozenArea: Boolean = OFF):
        """This method modifies the SizingPointSymmetry object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys** = None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.
        """
        ...
