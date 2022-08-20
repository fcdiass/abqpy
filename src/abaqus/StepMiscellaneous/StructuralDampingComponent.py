from .._decorators import abaqus_class_doc


@abaqus_class_doc
class StructuralDampingComponent:
    """A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingComponent.StructuralDampingComponent` object is used to define structural damping over a range of
    modes.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name].structuralDamping.components[i]
    """

    #: An Int specifying the mode number of the lowest mode of a range.
    start: int = None

    #: An Int specifying the mode number of the highest mode of a range.
    end: int = None

    #: A Float specifying the damping factor, s.
    factor: float = None
