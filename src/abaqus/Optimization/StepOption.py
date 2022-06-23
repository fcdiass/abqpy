from abaqusConstants import *


class StepOption:
    """A StepOption is an object used to define step options in a design response.

    Attributes
    ----------
    lowerMode: SymbolicConstant
        The SymbolicConstant ALL or an Int specifying the lower mode in the range of modes to
        consider in the step. **lowerMode** is ignored for steps without modes. The default value
        is ALL.
    upperMode: SymbolicConstant
        The SymbolicConstant ALL or an Int specifying the upper mode in the range of modes to
        consider in the step. **upperMode** is ignored for steps without modes. The default value
        is ALL.
    loadCase: SymbolicConstant
        The SymbolicConstant ALL or a String specifying the name of the load case. **loadCase** is
        ignored when the specified **step** does not contain a load case. The default value is
        ALL.
    step: SymbolicConstant
        The SymbolicConstant ALL or a String specifying the name of the step. The default value
        is ALL.
    model: str
        A string specifying the name of the model from which the steps are supposed to be used
        in the design response. Specify only if the steps are not from the current model.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].designResponses[name].stepOptions[i]
    """

    #: The SymbolicConstant ALL or an Int specifying the lower mode in the range of modes to
    #: consider in the step. **lowerMode** is ignored for steps without modes. The default value
    #: is ALL.
    lowerMode: SymbolicConstant = ALL

    #: The SymbolicConstant ALL or an Int specifying the upper mode in the range of modes to
    #: consider in the step. **upperMode** is ignored for steps without modes. The default value
    #: is ALL.
    upperMode: SymbolicConstant = ALL

    #: The SymbolicConstant ALL or a String specifying the name of the load case. **loadCase** is
    #: ignored when the specified **step** does not contain a load case. The default value is
    #: ALL.
    loadCase: SymbolicConstant = ALL

    #: The SymbolicConstant ALL or a String specifying the name of the step. The default value
    #: is ALL.
    step: SymbolicConstant = ALL

    #: A string specifying the name of the model from which the steps are supposed to be used
    #: in the design response. Specify only if the steps are not from the current model.
    model: str = ""
