from rubicon.objc import *

from .base import Widget
from ..libs import *


class Box(Widget):
    def create(self):
        self.native = None
        self.constraints = None