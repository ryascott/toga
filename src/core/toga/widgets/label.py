from .base import Widget
from toga.constants import *


class Label(Widget):
    """
    Label widget
    """
    def __init__(self, text, id=None, style=None, factory=None, alignment=LEFT_ALIGNED):
        """ Instantiate a new instance of the label widget

        :param text:        Text of the label
        :type  text:        ``str``

        :param id:          An identifier for this widget.
        :type  id:          ``str``

        :param style:       an optional style object. If no style is provided then a
                            new one will be created for the widget.
        :type style:        :class:`colosseum.CSSNode`

        :param alignment:   Alignment of the label, default is left. Alignments can be found
                            in toga.constants
        :type alignment:    ``int``
        """
        super().__init__(id=id, style=style, factory=factory)

        # Create a platform specific implementation of a Label
        self._impl = self.factory.Label(interface=self)

        self.text = text
        self.alignment = alignment

    @property
    def alignment(self):
        """
        The alignment of the label text

        :returns: Alignment of the label, default is left. Alignments can be found
                            in toga.constants
        :rtype: ``int``
        """
        return self._alignment

    @alignment.setter
    def alignment(self, value):
        self._alignment = value
        self._impl.set_alignment(value)

    @property
    def text(self):
        """
        The text of the label

        :rtype: ``str``
        """
        return self._text

    @text.setter
    def text(self, value):
        if value is None:
            self._text = ''
        else:
            self._text = str(value)
        self._impl.set_text(self._text)
        self.rehint()
