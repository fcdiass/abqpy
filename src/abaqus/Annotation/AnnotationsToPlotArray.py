import typing

from .Annotation import Annotation
from .._decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class AnnotationsToPlotArray(typing.List[Annotation]):
    """The AnnotationsToPlotArray object is a sequence that stores references to plotted
    annotations. By adding annotations to and removing annotations from this sequence, you
    can control which annotations are displayed in a particular viewport.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import annotationToolset
            session.viewports[name].annotationsToPlot
    """

    @abaqus_method_doc
    def bringForward(self, index: str):
        """This method brings the Annotation object one position forward in the
        AnnotationsToPlotArray sequence.

        Parameters
        ----------
        index
            An Int specifying the index of the Annotation object in the AnnotationsToPlotArray
            sequence.

        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def bringToFront(self, index: str):
        """This method brings the Annotation object to the beginning of the AnnotationsToPlotArray
        sequence.

        Parameters
        ----------
        index
            An Int specifying the index of the Annotation object in the AnnotationsToPlotArray
            sequence.

        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def moveAfter(self, index: str, other: str):
        """This method moves the Annotation object after another object in the same
        AnnotationsToPlotArray sequence.

        Parameters
        ----------
        index
            An Integer specifying the index of the Annotation object in the AnnotationsToPlotArray
            sequence.
        other
            An Integer specifying the index of the other Annotation object in the
            AnnotationsToPlotArray sequence after which this object will be moved.

        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def moveBefore(self, index: str, other: str):
        """This method moves the Annotation object before another object in the same
        AnnotationsToPlotArray sequence.

        Parameters
        ----------
        index
            An Int specifying the index of the Annotation object in the AnnotationsToPlotArray
            sequence.
        other
            An Int specifying the index of the other Annotation object in the AnnotationsToPlotArray
            sequence before which this object will be moved.

        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def sendBackward(self, index: str):
        """This method sends the Annotation object one position backward in the
        AnnotationsToPlotArray sequence.

        Parameters
        ----------
        index
            An Int specifying the index of the Annotation object in the AnnotationsToPlotArray
            sequence.

        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def sendToBack(self, index: str):
        """This method sends the Annotation object to the end of the AnnotationsToPlotArray
        sequence.

        Parameters
        ----------
        index
            An Int specifying the index of the Annotation object in the AnnotationsToPlotArray
            sequence.

        """
        # TODO: implement this method
        ...
