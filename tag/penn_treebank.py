from .abstract import AbstractTagger


class PennTreebankTagger(AbstractTagger):
    @property
    def _function_word_tags(self) -> list[str]:
        return [
            "CC",
            "DT",
            "EX",
            "IN",
            "MD",
            "POS",
            "PRP",
            "PRP$",
            "RP",
            "TO",
            "UH",
            "VB",
            "VBD",
            "VBG",
            "VBN",
            "VBP",
            "VBZ",
            "WDT",
            "WP",
            "WP$",
            "WRB"
        ]

    @property
    def _removed_tags(self) -> list[str]:
        return [
            "#",
            "$",
            "''",
            "(",
            ")",
            ",",
            ".",
            ":",
            "CD",
            "FW",
            "SENT",
            "SYM",
            "``",
        ]
