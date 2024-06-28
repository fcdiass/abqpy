from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, wrap

from ..Odb.OdbBase import OdbBase
from .ActuatorAmplitude import ActuatorAmplitude
from .DecayAmplitude import DecayAmplitude
from .EquallySpacedAmplitude import EquallySpacedAmplitude
from .ModulatedAmplitude import ModulatedAmplitude
from .PeriodicAmplitude import PeriodicAmplitude
from .PsdDefinition import PsdDefinition
from .SmoothStepAmplitude import SmoothStepAmplitude
from .SolutionDependentAmplitude import SolutionDependentAmplitude
from .SpectrumAmplitude import SpectrumAmplitude
from .TabularAmplitude import TabularAmplitude


@abaqus_class_doc
class AmplitudeOdb(OdbBase):
    """The Odb object is the in-memory representation of an output database (ODB) file.

    .. note::
        This object can be accessed by::

            import odbAccess
            session.odbs[name]
    """

    ActuatorAmplitude = wrap(ActuatorAmplitude, attr="amplitudes", key="name", index=0)
    DecayAmplitude = wrap(DecayAmplitude, attr="amplitudes", key="name", index=0)
    EquallySpacedAmplitude = wrap(EquallySpacedAmplitude, attr="amplitudes", key="name", index=0)
    ModulatedAmplitude = wrap(ModulatedAmplitude, attr="amplitudes", key="name", index=0)
    PeriodicAmplitude = wrap(PeriodicAmplitude, attr="amplitudes", key="name", index=0)
    PsdDefinition = wrap(PsdDefinition, attr="amplitudes", key="name", index=0)
    SmoothStepAmplitude = wrap(SmoothStepAmplitude, attr="amplitudes", key="name", index=0)
    SolutionDependentAmplitude = wrap(SolutionDependentAmplitude, attr="amplitudes", key="name", index=0)
    SpectrumAmplitude = wrap(SpectrumAmplitude, attr="amplitudes", key="name", index=0)
    TabularAmplitude = wrap(TabularAmplitude, attr="amplitudes", key="name", index=0)
