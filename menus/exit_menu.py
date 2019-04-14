# coding: utf-8

from typing import Type

from tools.models.menus import Menu, Option


class ExitMenu(Menu):
    """Structure 'ExitMenu' singleton instance."""

    _instance = None

    def __new__(cls: Type['ExitMenu'], *args, **kwargs) -> 'ExitMenu':
        """Create 'ExitMenu' singleton instance."""
        if not ExitMenu._instance:
            ExitMenu._instance = super(ExitMenu, cls).__new__(cls, *args, **kwargs)
        return ExitMenu._instance

    def __init__(self: 'ExitMenu') -> None:
        """Init 'ExitMenu' singleton instance."""
        self._YES = Option(message="YES")
        self._NO = Option(message="NO")
        super(ExitMenu, self).__init__(options=[self._YES, self._NO])

    def apply(self: 'ExitMenu') -> None:
        """Apply 'ExitMenu' focused option."""
        if self.option == self._YES:
            self.screen.running = False
        elif self.option == self._NO:
            self.running = False
