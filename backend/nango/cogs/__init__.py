"""Cogs are nango's plugins that give it flexibility.

Every Nango function is linked to a cog.

Note: Order of the __all__ matches the order of cogs execution.
"""

from .serializer_cog import SerializerCog

__all__ = ["SerializerCog"]
