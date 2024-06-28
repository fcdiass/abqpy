from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, wrap, wrap_bc

from ..Model.ModelBase import ModelBase
from .AccelerationBaseMotionBC import AccelerationBaseMotionBC
from .AccelerationBaseMotionBCState import AccelerationBaseMotionBCState
from .AccelerationBC import AccelerationBC
from .AccelerationBCState import AccelerationBCState
from .AcousticPressureBC import AcousticPressureBC
from .AcousticPressureBCState import AcousticPressureBCState
from .ConcentrationBC import ConcentrationBC
from .ConcentrationBCState import ConcentrationBCState
from .ConnAccelerationBC import ConnAccelerationBC
from .ConnAccelerationBCState import ConnAccelerationBCState
from .ConnDisplacementBC import ConnDisplacementBC
from .ConnDisplacementBCState import ConnDisplacementBCState
from .ConnVelocityBC import ConnVelocityBC
from .ConnVelocityBCState import ConnVelocityBCState
from .DisplacementBaseMotionBC import DisplacementBaseMotionBC
from .DisplacementBaseMotionBCState import DisplacementBaseMotionBCState
from .DisplacementBC import DisplacementBC
from .DisplacementBCState import DisplacementBCState
from .ElectricPotentialBC import ElectricPotentialBC
from .ElectricPotentialBCState import ElectricPotentialBCState
from .EulerianBC import EulerianBC
from .EulerianBCState import EulerianBCState
from .EulerianMotionBC import EulerianMotionBC
from .EulerianMotionBCState import EulerianMotionBCState
from .FluidCavityPressureBC import FluidCavityPressureBC
from .FluidCavityPressureBCState import FluidCavityPressureBCState
from .MagneticVectorPotentialBC import MagneticVectorPotentialBC
from .MaterialFlowBC import MaterialFlowBC
from .MaterialFlowBCState import MaterialFlowBCState
from .PorePressureBC import PorePressureBC
from .PorePressureBCState import PorePressureBCState
from .RetainedNodalDofsBC import RetainedNodalDofsBC
from .SecondaryBaseBC import SecondaryBaseBC
from .SecondaryBaseBCState import SecondaryBaseBCState
from .SubmodelBC import SubmodelBC
from .SubmodelBCState import SubmodelBCState
from .TemperatureBC import TemperatureBC
from .TemperatureBCState import TemperatureBCState
from .TypeBC import TypeBC
from .TypeBCState import TypeBCState
from .VelocityBaseMotionBC import VelocityBaseMotionBC
from .VelocityBaseMotionBCState import VelocityBaseMotionBCState
from .VelocityBC import VelocityBC
from .VelocityBCState import VelocityBCState


@abaqus_class_doc
class BoundaryConditionModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note::
        This object can be accessed by::

            mdb.models[name]
    """

    AccelerationBaseMotionBC = wrap_bc(
        AccelerationBaseMotionBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=AccelerationBaseMotionBCState,
    )
    AccelerationBC = wrap_bc(
        AccelerationBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=AccelerationBCState,
    )
    AcousticPressureBC = wrap_bc(
        AcousticPressureBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=AcousticPressureBCState,
    )
    ConcentrationBC = wrap_bc(
        ConcentrationBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=ConcentrationBCState,
    )
    ConnAccelerationBC = wrap_bc(
        ConnAccelerationBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=ConnAccelerationBCState,
    )
    ConnDisplacementBC = wrap_bc(
        ConnDisplacementBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=ConnDisplacementBCState,
    )
    ConnVelocityBC = wrap_bc(
        ConnVelocityBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=ConnVelocityBCState,
    )
    DisplacementBaseMotionBC = wrap_bc(
        DisplacementBaseMotionBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=DisplacementBaseMotionBCState,
    )
    DisplacementBC = wrap_bc(
        DisplacementBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=DisplacementBCState,
    )
    ElectricPotentialBC = wrap_bc(
        ElectricPotentialBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=ElectricPotentialBCState,
    )
    EulerianBC = wrap_bc(
        EulerianBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=EulerianBCState,
    )
    EulerianMotionBC = wrap_bc(
        EulerianMotionBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=EulerianMotionBCState,
    )
    FluidCavityPressureBC = wrap_bc(
        FluidCavityPressureBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=FluidCavityPressureBCState,
    )
    MagneticVectorPotentialBC = wrap(MagneticVectorPotentialBC, attr="boundaryConditions", key="name", index=0)
    MaterialFlowBC = wrap_bc(
        MaterialFlowBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=MaterialFlowBCState,
    )
    PorePressureBC = wrap_bc(
        PorePressureBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=PorePressureBCState,
    )
    RetainedNodalDofsBC = wrap(RetainedNodalDofsBC, attr="boundaryConditions", key="name", index=0)
    SecondaryBaseBC = wrap_bc(
        SecondaryBaseBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=SecondaryBaseBCState,
    )
    SubmodelBC = wrap_bc(
        SubmodelBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=SubmodelBCState,
    )
    TemperatureBC = wrap_bc(
        TemperatureBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=TemperatureBCState,
    )
    VelocityBaseMotionBC = wrap_bc(
        VelocityBaseMotionBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=VelocityBaseMotionBCState,
    )
    VelocityBC = wrap_bc(
        VelocityBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=VelocityBCState,
    )
    EncastreBC = wrap_bc(
        TypeBC.EncastreBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=TypeBCState,
    )
    PinnedBC = wrap_bc(
        TypeBC.PinnedBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=TypeBCState,
    )
    XsymmBC = wrap_bc(
        TypeBC.XsymmBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=TypeBCState,
    )
    YsymmBC = wrap_bc(
        TypeBC.YsymmBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=TypeBCState,
    )
    ZsymmBC = wrap_bc(
        TypeBC.ZsymmBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=TypeBCState,
    )
    XasymmBC = wrap_bc(
        TypeBC.XasymmBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=TypeBCState,
    )
    YasymmBC = wrap_bc(
        TypeBC.YasymmBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=TypeBCState,
    )
    ZasymmBC = wrap_bc(
        TypeBC.ZasymmBC,
        attr="boundaryConditions",
        key="name",
        index=0,
        stepKey="createStepName",
        stepIndex=1,
        stateType=TypeBCState,
    )
