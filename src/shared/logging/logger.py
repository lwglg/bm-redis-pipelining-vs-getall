from .text import Text

__all__ = ["Logger"]


class Logger:
    """Implementation for a generic logger, using the local text formatting layer."""

    @classmethod
    def log(
        cls,
        text: str,
        text_format: str = Text.CWHITE,
        bold: bool = False,
        end: str | None=None,
        flush: bool=False
    ) -> None:
        to_be_logged = Text.format_text(text, text_format)
        to_be_logged = Text.bold(to_be_logged) if bold else to_be_logged 

        print(to_be_logged, end=end, flush=flush)

    @classmethod
    def success(
        cls,
        text: str,
        bold: bool = False,
        end: str | None=None,
        flush: bool=False
    ) -> None:
        Logger.log(text, Text.CGREEN, bold, end, flush)

    @classmethod
    def warning(
        cls,
        text: str,
        bold: bool = False,
        end: str | None=None,
        flush: bool=False
    ) -> None:
        Logger.log(text, Text.CYELLOW, bold, end, flush)

    @classmethod
    def danger(
        cls,
        text: str,
        bold: bool = False,
        end: str | None=None,
        flush: bool=False
    ) -> None:
        Logger.log(text, Text.CRED, bold, end, flush)
