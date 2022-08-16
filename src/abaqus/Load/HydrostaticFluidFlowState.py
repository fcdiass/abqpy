from .LoadState import LoadState
from ..UtilityAndView.abaqusConstants import *


class HydrostaticFluidFlowState(LoadState):
    """The HydrostaticFluidFlowState object stores the propagating data for a concentrated
    HydrostaticFluidFlow object in a step. One instance of this object is created internally
    by the HydrostaticFluidFlow object for each step. The instance is also deleted
    internally by the HydrostaticFluidFlow object.
    The HydrostaticFluidFlowState object has no constructor or methods.
    The HydrostaticFluidFlowState object is derived from the LoadState object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - FLUID FLUX
    """

    #: A Float specifying the load magnitude.
    magnitude: float = None

    #: A SymbolicConstant specifying the propagation state of the load magnitude. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    magnitudeState: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the LoadState object. Possible
    #: values are:
    #: 
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - NO_LONGER_ACTIVE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: - BUILT_INTO_BASE_STATE
    status: SymbolicConstant = None

    #: A String specifying the name of the amplitude reference. The String is empty if the load
    #: has no amplitude reference.
    amplitude: str = ""
