from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import OFF, Boolean
from .CrushStressVelocityFactor import CrushStressVelocityFactor


@abaqus_class_doc
class CrushStress:
    """The CrushStress object specifies the crush stress of a material.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].crushStress
            import odbMaterial
            session.odbs[name].materials[name].crushStress

        The table data for this object are:

        - Scaling factor.
        - Relative velocity.

        The corresponding analysis keywords are:

        - CRUSH STRESS

    .. versionadded:: 2022
        The ``CrushStress`` class was added.
    """

    #: A sequence of sequences of Floats specifying the items described below.
    crushStressTable: tuple[tuple[float, ...], ...] = ()

    #: A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    # An Int specifying the number of field variable dependencies. The default value is 0.
    dependencies: int = 0

    #: A CrushStressVelocityFactor object.
    crushStressVelocityFactor: CrushStressVelocityFactor = CrushStressVelocityFactor(((),))

    @abaqus_method_doc
    def __init__(
        self,
        crushStressTable: tuple[tuple[float, ...], ...],
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a CrushStress object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].CrushStress
                session.odbs[name].materials[name].CrushStress

        Parameters
        ----------
        crushStressTable
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        """
        self.crushStressTable = crushStressTable
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies

    @abaqus_method_doc
    def setValues(
        self,
        crushStressTable: tuple[tuple[float, ...], ...] = (),
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a CrushStress object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].CrushStress
                session.odbs[name].materials[name].CrushStress

        Parameters
        ----------
        crushStressTable
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        """
        self.crushStressTable = crushStressTable
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies
