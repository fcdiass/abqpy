from abaqusConstants import *


class BoundaryConditionState:
    """The BoundaryConditionState object is the abstract base type for other
    BoundaryConditionState objects. The BoundaryConditionState object has no explicit
    constructor or methods. The members of the BoundaryConditionState object are common to
    all objects derived from the BoundaryConditionState object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].steps[name].boundaryConditionStates[name]
    """

    #: A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
    #: values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    amplitudeState: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:
    #:
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - NO_LONGER_ACTIVE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: - PROPAGATED_FROM_BASE_STATE
    #: - MODIFIED_FROM_BASE_STATE
    #: - DEACTIVATED_FROM_BASE_STATE
    #: - BUILT_INTO_MODES
    status: SymbolicConstant = None

    #: A String specifying the name of the amplitude reference. The String is empty if the
    #: boundary condition has no amplitude reference.
    amplitude: str = ""
