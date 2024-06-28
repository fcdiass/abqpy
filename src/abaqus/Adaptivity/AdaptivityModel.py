from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc, wrap

from ..Model.ModelBase import ModelBase
from ..Odb.Odb import Odb
from .AdaptiveMeshConstraint import AdaptiveMeshConstraint
from .AdaptiveMeshControl import AdaptiveMeshControl
from .DisplacementAdaptiveMeshConstraint import DisplacementAdaptiveMeshConstraint
from .RemeshingRule import RemeshingRule
from .VelocityAdaptiveMeshConstraint import VelocityAdaptiveMeshConstraint


@abaqus_class_doc
class AdaptivityModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note::
        This object can be accessed by::

            mdb.models[name]
    """

    @abaqus_method_doc
    def adaptiveRemesh(self, odb: Odb):
        """This method remeshes the model using the active remesh rules in the model and the error indicator
        results from a previous analysis.

        Parameters
        ----------
        odb
            An Odb object containing error output field results.

        Returns
        -------
        AdaptivityIteration
            An AdaptivityIteration object.
        """
        ...

    AdaptiveMeshConstraint = wrap(AdaptiveMeshConstraint, attr="adaptiveMeshConstraints", key="name", index=0)
    AdaptiveMeshControl = wrap(AdaptiveMeshControl, attr="adaptiveMeshControls", key="name", index=0)
    DisplacementAdaptiveMeshConstraint = wrap(
        DisplacementAdaptiveMeshConstraint, attr="adaptiveMeshConstraints", key="name", index=0
    )
    RemeshingRule = wrap(RemeshingRule, attr="remeshingRules", key="name", index=0)
    VelocityAdaptiveMeshConstraint = wrap(
        VelocityAdaptiveMeshConstraint, attr="adaptiveMeshConstraints", key="name", index=0
    )
