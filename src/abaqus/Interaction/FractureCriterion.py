import typing

from abaqusConstants import *


class FractureCriterion:
    """The FractureCriterion object specifies fractureCriterion options for a contact
    interaction property.

    Attributes
    ----------
    initTable
        A sequence of sequences of Floats specifying the value defining the fracture criterion.
        The items in the table data are described below.
    type
        A SymbolicConstant specifying the type of data used to define the fracture criterion.
        Possible values are VCCT and ENHANCED VCCT. The default value is VCCT.
    mixedModeBehavior
        A SymbolicConstant specifying the mixed mode behavior type used to define fracture
        criterion. Possible values are BK, POWER, and REEDER. The default value is BK.
    temperatureDependency
        A Boolean specifying whether the fracture criterion data depend on temperature. The
        default value is OFF.
    dependencies
        An Int specifying the number of fracture criterion data field variables. The default
        value is 0.
    tolerance
        A Float specifying the tolerance for VCCT\Enhanced VCCT type. The default value is 0.2.
    specifyUnstableCrackProp
        A SymbolicConstant specifying whether to include unstable crack growth tolerance in
        fracture criterion. Possible values are ON and OFF. The default value is OFF.
    unstableTolerance
        The SymbolicConstant DEFAULT or a Float specifying the tolerance for unstable crack
        propagation. This parameter specified only if **specifyUnstableCrackProp** = ON. The default
        value is DEFAULT.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactionProperties[name].fractureCriterion

    The table data for this object are:
    
    Table data for **initTable**:
    
    If **type** = VCCT for **mixedModeBehavior** = BK or REEDER, the table data specify the following:
    
        - Mode I critical energy release rate, GICGI⁢C.
        - Mode II critical energy release rate, GIICGI⁢I⁢C.
        - Mode III critical energy release rate, GIIICGI⁢I⁢I⁢C.
        - Exponent, ηη.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    If **type** = VCCT for **mixedModeBehavior** = POWER, the table data specify the following:
    
        - Mode I critical energy release rate, GICGI⁢C.
        - Mode II critical energy release rate, GIICGI⁢I⁢C.
        - Mode III critical energy release rate, GIIICGI⁢I⁢I⁢C.
        - Exponent, ama⁢m.
        - Exponent, ana⁢n.
        - Exponent, aoa⁢o.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    If **type** = ENHANCED VCCT for **mixedModeBehavior** = BK or REEDER, the table data specify the following:
    
        - Mode I critical energy release rate for onset crack, GICGI⁢C.
        - Mode II critical energy release rate for onset crack, GIICGI⁢I⁢C.
        - Mode III critical energy release rate for onset crack, GIIICGI⁢I⁢I⁢C.
        - Mode I critical energy release rate for crack propagation, GICGI⁢C.
        - Mode II critical energy release rate for crack propagation, GIICGI⁢I⁢C.
        - Mode III critical energy release rate for crack propagation, GIIICGI⁢I⁢I⁢C.
        - Exponent, ηη.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    If **type** = ENHANCED VCCT for **mixedModeBehavior** = POWER, the table data specify the following:
    
        - Mode I critical energy release rate for onset crack, GICGI⁢C.
        - Mode II critical energy release rate for onset crack, GIICGI⁢I⁢C.
        - Mode III critical energy release rate for onset crack, GIIICGI⁢I⁢I⁢C.
        - Mode I critical energy release rate for crack propagation, GICGI⁢C.
        - Mode II critical energy release rate for crack propagation, GIICGI⁢I⁢C.
        - Mode III critical energy release rate for crack propagation, GIIICGI⁢I⁢I⁢C.
        - Exponent, ama⁢m.
        - Exponent, ana⁢n.
        - Exponent, aoa⁢o.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    The corresponding analysis keywords are:

    - FRACTURE CRITERION
    """

    #: A sequence of sequences of Floats specifying the value defining the fracture criterion.
    #: The items in the table data are described below.
    initTable: tuple

    #: A SymbolicConstant specifying the type of data used to define the fracture criterion.
    #: Possible values are VCCT and ENHANCED VCCT. The default value is VCCT.
    type: SymbolicConstant = VCCT

    #: A SymbolicConstant specifying the mixed mode behavior type used to define fracture
    #: criterion. Possible values are BK, POWER, and REEDER. The default value is BK.
    mixedModeBehavior: SymbolicConstant = BK

    #: A Boolean specifying whether the fracture criterion data depend on temperature. The
    #: default value is OFF.
    temperatureDependency: Boolean = OFF

    #: An Int specifying the number of fracture criterion data field variables. The default
    #: value is 0.
    dependencies: int = 0

    #: A Float specifying the tolerance for VCCT\Enhanced VCCT type. The default value is 0.2.
    tolerance: float = 0

    #: A SymbolicConstant specifying whether to include unstable crack growth tolerance in
    #: fracture criterion. Possible values are ON and OFF. The default value is OFF.
    specifyUnstableCrackProp: SymbolicConstant = OFF

    #: The SymbolicConstant DEFAULT or a Float specifying the tolerance for unstable crack
    #: propagation. This parameter specified only if **specifyUnstableCrackProp** = ON. The default
    #: value is DEFAULT.
    unstableTolerance: typing.Union[SymbolicConstant, float] = DEFAULT

    def __init__(
        self,
        initTable: tuple,
        type: SymbolicConstant = VCCT,
        mixedModeBehavior: SymbolicConstant = BK,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        tolerance: float = 0,
        specifyUnstableCrackProp: SymbolicConstant = OFF,
        unstableTolerance: typing.Union[SymbolicConstant, float] = DEFAULT,
    ):
        r"""This method creates a FractureCriterion object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].interactionProperties[name].FractureCriterion

        Parameters
        ----------
        initTable
            A sequence of sequences of Floats specifying the value defining the fracture criterion.
            The items in the table data are described below.
        type
            A SymbolicConstant specifying the type of data used to define the fracture criterion.
            Possible values are VCCT and ENHANCED VCCT. The default value is VCCT.
        mixedModeBehavior
            A SymbolicConstant specifying the mixed mode behavior type used to define fracture
            criterion. Possible values are BK, POWER, and REEDER. The default value is BK.
        temperatureDependency
            A Boolean specifying whether the fracture criterion data depend on temperature. The
            default value is OFF.
        dependencies
            An Int specifying the number of fracture criterion data field variables. The default
            value is 0.
        tolerance
            A Float specifying the tolerance for VCCT\Enhanced VCCT type. The default value is 0.2.
        specifyUnstableCrackProp
            A SymbolicConstant specifying whether to include unstable crack growth tolerance in
            fracture criterion. Possible values are ON and OFF. The default value is OFF.
        unstableTolerance
            The SymbolicConstant DEFAULT or a Float specifying the tolerance for unstable crack
            propagation. This parameter specified only if **specifyUnstableCrackProp** = ON. The default
            value is DEFAULT.

        Returns
        -------
        FractureCriterion
            A :py:class:`~abaqus.Interaction.FractureCriterion.FractureCriterion` object.
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the FractureCriterion object."""
        pass
