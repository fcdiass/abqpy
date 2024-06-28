from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, wrap

from ..Step.StepBase import StepBase
from .AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from .AdaptiveMeshDomain import AdaptiveMeshDomain
from .DisplacementAdaptiveMeshConstraintState import (
    DisplacementAdaptiveMeshConstraintState,
)
from .VelocityAdaptiveMeshConstraintState import VelocityAdaptiveMeshConstraintState


@abaqus_class_doc
class AdaptivityStep(StepBase):
    """The Step object stores the parameters that determine the context of the step. The Step object is the
    abstract base type for other Step objects. The Step object has no explicit constructor. The methods and
    members of the Step object are common to all objects derived from the Step.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]
    """

    AdaptiveMeshConstraintState = wrap(
        AdaptiveMeshConstraintState, attr="adaptiveMeshConstraintStates", key="amplitude", index=2
    )
    DisplacementAdaptiveMeshConstraintState = wrap(
        DisplacementAdaptiveMeshConstraintState, attr="adaptiveMeshConstraintStates", key="amplitude", index=14
    )
    VelocityAdaptiveMeshConstraintState = wrap(
        VelocityAdaptiveMeshConstraintState, attr="adaptiveMeshConstraintStates", key="amplitude", index=14
    )
    AdaptiveMeshDomain = wrap(AdaptiveMeshDomain, attr="adaptiveMeshDomains", key="controls", index=1)
