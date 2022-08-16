from .Constraint import Constraint
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


class RigidBody(Constraint):
    """The RigidBody object constrains all the degrees of freedom on the specified regions to
    the degree of freedom of its associated reference point.
    The RigidBody object is derived from the ConstrainedSketchConstraint object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import interaction
            mdb.models[name].constraints[name]

        The corresponding analysis keywords are:

        - RIGID BODY
    """

    #: A Boolean specifying whether the constraint is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    #: A String specifying the constraint repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the reference point.
    refPointRegion: Region

    #: None or a Region object specifying the elements constrained to the movement of the
    #: reference point. The default value is None.
    bodyRegion: str = None

    #: None or a Region object specifying the nodes tied to the movement of the reference
    #: point. The default value is None.
    tieRegion: str = None

    #: None or a Region object specifying the nodes pinned to the movement of the reference
    #: point. The default value is None.
    pinRegion: str = None

    #: None or a Region object specifying the analytic surface constrained to the movement of
    #: the reference point. The default value is None.
    surfaceRegion: str = None

    #: A Boolean specifying whether the analysis product should recompute the reference point
    #: position to be at the center of mass. The default value is OFF.
    refPointAtCOM: Boolean = OFF

    #: A Boolean specifying whether the temperature degree of freedom should be constrained.
    #: The default value is OFF.
    isothermal: Boolean = OFF

    def __init__(
        self,
        name: str,
        refPointRegion: Region,
        bodyRegion: str = None,
        tieRegion: str = None,
        pinRegion: str = None,
        surfaceRegion: str = None,
        refPointAtCOM: Boolean = OFF,
        isothermal: Boolean = OFF,
    ):
        """This method creates a RigidBody object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].RigidBody

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        refPointRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the reference point.
        bodyRegion
            None or a Region object specifying the elements constrained to the movement of the
            reference point. The default value is None.
        tieRegion
            None or a Region object specifying the nodes tied to the movement of the reference
            point. The default value is None.
        pinRegion
            None or a Region object specifying the nodes pinned to the movement of the reference
            point. The default value is None.
        surfaceRegion
            None or a Region object specifying the analytic surface constrained to the movement of
            the reference point. The default value is None.
        refPointAtCOM
            A Boolean specifying whether the analysis product should recompute the reference point
            position to be at the center of mass. The default value is OFF.
        isothermal
            A Boolean specifying whether the temperature degree of freedom should be constrained.
            The default value is OFF.

        Returns
        -------
        RigidBody
            A :py:class:`~abaqus.Constraint.RigidBody.RigidBody` object.
        """
        super().__init__()

    def setValues(
        self,
        bodyRegion: str = None,
        tieRegion: str = None,
        pinRegion: str = None,
        surfaceRegion: str = None,
        refPointAtCOM: Boolean = OFF,
        isothermal: Boolean = OFF,
    ):
        """This method modifies the RigidBody object.

        Parameters
        ----------
        bodyRegion
            None or a Region object specifying the elements constrained to the movement of the
            reference point. The default value is None.
        tieRegion
            None or a Region object specifying the nodes tied to the movement of the reference
            point. The default value is None.
        pinRegion
            None or a Region object specifying the nodes pinned to the movement of the reference
            point. The default value is None.
        surfaceRegion
            None or a Region object specifying the analytic surface constrained to the movement of
            the reference point. The default value is None.
        refPointAtCOM
            A Boolean specifying whether the analysis product should recompute the reference point
            position to be at the center of mass. The default value is OFF.
        isothermal
            A Boolean specifying whether the temperature degree of freedom should be constrained.
            The default value is OFF.
        """
        ...
