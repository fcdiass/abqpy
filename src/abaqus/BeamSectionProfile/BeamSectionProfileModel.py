from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc, wrap

from ..Model.ModelBase import ModelBase
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
from .Profile import Profile
from .RectangularProfile import RectangularProfile
from .TProfile import TProfile
from .TrapezoidalProfile import TrapezoidalProfile


@abaqus_class_doc
class BeamSectionProfileModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note::
        This object can be accessed by::

            mdb.models[name]
    """

    @abaqus_method_doc
    def beamProfilesFromOdb(self, fileName: str):
        """This method creates Profile objects by reading an output database. The new profiles are placed in the
        profiles repository.

        .. note::
            This function can be accessed by::

                mdb.models[name].beamProfilesFromOdb

        Parameters
        ----------
        fileName
            A String specifying the name of the output database file (including the .odb extension)
            to be read. The String can also be the full path to the output database file if it is
            located in another directory.

        Returns
        -------
        list[Profile]
            A list of Profile objects.
        """
        profiles: dict[str, Profile] = {}
        self.profiles.update(profiles)
        return profiles

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
