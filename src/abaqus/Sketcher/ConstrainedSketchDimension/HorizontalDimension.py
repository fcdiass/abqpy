from typing import Optional, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchDimension import ConstrainedSketchDimension
from ..ConstrainedSketchVertex.ConstrainedSketchVertex import ConstrainedSketchVertex
from ...UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class HorizontalDimension(ConstrainedSketchDimension):
    @abaqus_method_doc
    def __init__(
        self,
        vertex1: ConstrainedSketchVertex,
        vertex2: ConstrainedSketchVertex,
        textPoint: Sequence[float],
        value: Optional[float] = None,
        reference: Boolean = OFF,
    ):
        """This method constructs a ConstrainedSketchDimension object between two vertices. A horizontal
        dimension indicates the horizontal distance along the **X** axis between two vertices.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].HorizontalDimension

        Parameters
        ----------
        vertex1
            A ConstrainedSketchVertex object specifying the first endpoint.
        vertex2
            A ConstrainedSketchVertex object specifying the second endpoint.
        textPoint
            A pair of Floats specifying the location of the dimension text.
        value
            A Float distance between the two vertices.
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it
            simply measures the distance between the two vertices.

        Returns
        -------
        ConstrainedSketchDimension
            A ConstrainedSketchDimension object (None if the dimension cannot be created).
        """
        ...
