"""
Fixer that turns 'long' into 'int' everywhere.
"""

from lib2to3 import fixer_base
from typing import ClassVar, Literal

class FixLong(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[Literal["'long'"]]
    def transform(self, node, results) -> None: ...
