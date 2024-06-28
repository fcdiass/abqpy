from abqpy.decorators import abaqus_class_doc, wrap

from ..Odb.OdbBase import OdbBase
from .ArbitraryProfile import ArbitraryProfile
from .BoxProfile import BoxProfile
from .ChannelProfile import ChannelProfile
from .CircularProfile import CircularProfile
from .GeneralizedProfile import GeneralizedProfile
from .HatProfile import HatProfile
from .HexagonalProfile import HexagonalProfile
from .IProfile import IProfile
from .LProfile import LProfile
from .PipeProfile import PipeProfile
from .RectangularProfile import RectangularProfile
from .TProfile import TProfile
from .TrapezoidalProfile import TrapezoidalProfile


@abaqus_class_doc
class BeamSectionProfileOdb(OdbBase):
    """The Odb object is the in-memory representation of an output database (ODB) file.

    .. note::
        This object can be accessed by::

            import odbAccess
            session.odbs[name]
    """

    ArbitraryProfile = wrap(ArbitraryProfile, attr="profiles", key="name", index=0)
    BoxProfile = wrap(BoxProfile, attr="profiles", key="name", index=0)
    ChannelProfile = wrap(ChannelProfile, attr="profiles", key="name", index=0)
    CircularProfile = wrap(CircularProfile, attr="profiles", key="name", index=0)
    GeneralizedProfile = wrap(GeneralizedProfile, attr="profiles", key="name", index=0)
    HatProfile = wrap(HatProfile, attr="profiles", key="name", index=0)
    HexagonalProfile = wrap(HexagonalProfile, attr="profiles", key="name", index=0)
    IProfile = wrap(IProfile, attr="profiles", key="name", index=0)
    LProfile = wrap(LProfile, attr="profiles", key="name", index=0)
    PipeProfile = wrap(PipeProfile, attr="profiles", key="name", index=0)
    RectangularProfile = wrap(RectangularProfile, attr="profiles", key="name", index=0)
    TProfile = wrap(TProfile, attr="profiles", key="name", index=0)
    TrapezoidalProfile = wrap(TrapezoidalProfile, attr="profiles", key="name", index=0)
