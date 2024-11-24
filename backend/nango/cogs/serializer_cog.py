from nango.utils import AbstractCog


class SerializerCog(AbstractCog):
    """Generate serializer from each django's models.

    Settings:
    --------
    """

    id = "serializer"

    def run(self) -> None:
        """Generate a serializer for each django's model."""
        super().run()
