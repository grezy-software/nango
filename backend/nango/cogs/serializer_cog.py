from nango.utils import AbstractCog


class SerializerCog(AbstractCog):
    """Generate serializer from each django's models."""

    id = "serializer"

    def run(self) -> None:
        """Generate a serializer for each django's model."""
        if not self.is_executable():
            return
