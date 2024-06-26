"""
Roles module.

This module contains class and method definitions for the [user/client] Role
object.

Classes:
  Roles: Provides definitions for the [user/client] role object and it's functionalities.
"""
from enum import Enum


class Roles(Enum):
    """
    Enum class definition of [user/client] role.
    """
    NOT_SET = 0
    PUBLISHER = 1
    SUBSCRIBER = 2
