from __future__ import annotations

from typing import TYPE_CHECKING

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Mesh.MeshElement import MeshElement
from ..Mesh.MeshNode import MeshNode
from ..UtilityAndView.abaqusConstants import OFF, Boolean

if TYPE_CHECKING:  # to avoid circular imports
    from ..Mesh.MeshElementArray import MeshElementArray
    from ..Mesh.MeshNodeArray import MeshNodeArray
    from .EdgeArray import EdgeArray


@abaqus_class_doc
class Edge:
    """Edges are one-dimensional regions of geometry.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSets[name].edges[i]
            mdb.models[name].parts[name].allInternalSurfaces[name].edges[i]
            mdb.models[name].parts[name].allSets[name].edges[i]
            mdb.models[name].parts[name].allSurfaces[name].edges[i]
            mdb.models[name].parts[name].edges[i]
            mdb.models[name].parts[name].sets[name].edges[i]
            mdb.models[name].parts[name].surfaces[name].edges[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].edges[i]
            mdb.models[name].rootAssembly.allInstances[name].sets[name].edges[i]
            mdb.models[name].rootAssembly.allInstances[name].surfaces[name].edges[i]
            mdb.models[name].rootAssembly.allInternalSets[name].edges[i]
            mdb.models[name].rootAssembly.allInternalSurfaces[name].edges[i]
            mdb.models[name].rootAssembly.allSets[name].edges[i]
            mdb.models[name].rootAssembly.allSurfaces[name].edges[i]
            mdb.models[name].rootAssembly.edges[i]
            mdb.models[name].rootAssembly.instances[name].edges[i]
            mdb.models[name].rootAssembly.instances[name].sets[name].edges[i]
            mdb.models[name].rootAssembly.instances[name].surfaces[name].edges[i]
            mdb.models[name].rootAssembly.modelInstances[i].edges[i]
            mdb.models[name].rootAssembly.modelInstances[i].sets[name].edges[i]
            mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].edges[i]
            mdb.models[name].rootAssembly.sets[name].edges[i]
            mdb.models[name].rootAssembly.surfaces[name].edges[i]
    """

    #: An Int specifying the index of the edge in the EdgeArray.
    index: int | None = None

    #: A Boolean specifying whether the edge belongs to the reference representation of the
    #: Part or Instance.
    isReferenceRep: Boolean = OFF

    #: A tuple of Floats specifying the **X**, **Y**, and **Z** coordinates of a point located on
    #: the edge.
    pointOn: tuple[float, ...] = ()

    #: A tuple of Floats specifying the name of the feature that created this edge.
    featureName: tuple[float, ...] = ()

    #: A tuple of Floats specifying the name of the part instance for this edge (if
    #: applicable).
    instanceName: tuple[float, ...] = ()

    @abaqus_method_doc
    def isTangentFlipped(self) -> Boolean:
        """This method determines whether the tangent to the edge is flipped from its default direction by the
        use of the flipTangent method on a Part object.

        Returns
        -------
        Boolean
            A Boolean value of True if the tangent is flipped and False if not.
        """
        return True

    @abaqus_method_doc
    def getCurvature(self, parameter: float, point: tuple[float, float, float]) -> dict[str, float]:
        """This method returns curvature information at a location on the edge.

        Parameters
        ----------
        parameter
            A Float specifying the normalized parameter location on the edge where the curvature is
            to be computed. This argument is mutually exclusive with the argument **point**.
        point
            A tuple of **X**, **Y**, and **Z** coordinates of a point at which the curvature is to be
            computed. If **point** does not lie on the edge an attempt is made to project it onto the
            edge and use the projected point.

        Returns
        -------
        dict
            A dictionary with keys 'evaluationPoint', 'curvature', 'radius', and 'tangent', where
            'evaluationPoint' specifies the location at which the curvature was computed;
            'curvature' specifies the curvature vector at that location; 'radius' is the radius of
            curvature; and 'tangent' specifies the tangent to the edge at that location.

        Raises
        ------
        The given edge is straight
        """
        return {"evaluationPoint": 0.0, "curvature": 0.0, "radius": 0.0, "tangent": 0.0}

    @abaqus_method_doc
    def getFaces(self) -> tuple[int]:
        """This method returns a sequence consisting of the face ids of the faces which share this edge.

        Returns
        -------
        tuple[int]
            A tuple of integers.
        """
        return (0,)

    @abaqus_method_doc
    def getAdjacentEdges(self) -> EdgeArray:
        """This method returns an array of Edge objects that share at least one vertex of the edge.

        Returns
        -------
        EdgeArray
            An EdgeArray object, which is a sequence of Edge objects.
        """
        return EdgeArray([Edge()])

    @abaqus_method_doc
    def getEdgesByEdgeAngle(self, angle: str) -> EdgeArray:
        """This method returns an array of Edge objects that are obtained by recursively finding adjacent edges
        that are at an angle of less than or equal to the specified face angle.

        Parameters
        ----------
        angle
            A float specifying the value of the face angle in degrees.

        Returns
        -------
        EdgeArray
            An EdgeArray object, which is a sequence of Edgeobjects.
        """
        return EdgeArray([Edge()])

    @abaqus_method_doc
    def getNodes(self) -> MeshNodeArray:
        """This method returns an array of node objects that are associated with the edge.

        Returns
        -------
        MeshNodeArray
            A MeshNodeArray object, which is a sequence of MeshNode objects.
        """
        return MeshNodeArray([MeshNode((0.0, 0.0, 0.0))])

    @abaqus_method_doc
    def getElements(self) -> MeshElementArray:
        """This method returns an array of element objects that are associated with the edge.

        Returns
        -------
        MeshElementArray
            A MeshElementArray object which is a sequence of MeshElement objects.
        """
        return MeshElementArray([MeshElement()])

    @abaqus_method_doc
    def getRadius(self) -> float:
        """This method returns the radius of circular edges.

        Returns
        -------
        float
            A Float specifying the radius.

        Raises
        ------
        The given edges is not circular
        """
        return 0.0

    @abaqus_method_doc
    def getSize(self, printResults: bool = True) -> float:
        """This method returns a Float indicating the length of the edge.

        Parameters
        ----------
        printResults
            A Bool specifying whether verbose output is printed. The default is True.

        Returns
        -------
        float
            A Float.
        """
        return 0.0

    @abaqus_method_doc
    def getVertices(self) -> tuple[int]:
        """This method returns a sequence of indices of the vertices that bound this edge. The
        first index refers to the vertex where the normalized curve parameter = 0.0, and the
        second index refers to the vertex where the normalized curve parameter = 1.0. If the
        edge is a closed curve, only one vertex index is returned.

        Returns
        -------
        tuple[int]
            A tuple of integers.

        """
        return (0,)
