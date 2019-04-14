# coding: utf-8

from typing import Type

from .exit_menu import ExitMenu

from tools.models.menus import Menu, Option


class MainMenu(Menu):
    """Structure 'MainMenu' singleton instance."""

    _instance = None

    def __new__(cls: Type['MainMenu'], *args, **kwargs) -> 'MainMenu':
        """Create 'MainMenu' singleton instance."""
        if not MainMenu._instance:
            MainMenu._instance = super(MainMenu, cls).__new__(cls, *args, **kwargs)
        return MainMenu._instance

    def __init__(self: 'MainMenu') -> None:
        """Init 'MainMenu' singleton instance."""
        self._PLAY = Option(message="PLAY")
        self._EDITOR = Option(message="EDITOR")
        self._OPTIONS = Option(message="OPTIONS")
        self._EXIT = Option(message="EXIT")
        super(MainMenu, self).__init__(options=[self._PLAY, self._EDITOR, self._OPTIONS, self._EXIT])

    def apply(self: 'MainMenu') -> None:
        """Apply 'MainMenu' focused option."""
        print(self.option.message)
        if self.option == self._EXIT:
            ExitMenu().loop()
