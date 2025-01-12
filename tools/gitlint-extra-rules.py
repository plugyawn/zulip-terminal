from typing import Any, List, Optional

from gitlint.options import ListOption
from gitlint.rules import CommitRule, RuleViolation


class EndsWithDot(CommitRule):
    name = "title-doesn't-end-with-dot"
    id = "ZT1"

    def validate(self, commit: Any) -> Optional[List[RuleViolation]]:
        error = "Title does not end with a '.' character"
        if not commit.message.title.endswith("."):
            return [RuleViolation(self.id, error, line_nr=1)]
        return None


class AreaFormatting(CommitRule):
    name = "area-formatting"
    id = "ZT2"

    options_spec = [
        ListOption("exclusions", ["WIP"], "Exclusions to area lower-case rule")
    ]

    def validate(self, commit: Any) -> Optional[List[RuleViolation]]:
        title_components = commit.message.title.split(": ")

        violations = []

        # Return just this violation, since latter checks assume an area
        error = (
            "Title should start with at least one area, followed by a colon and space"
        )
        if len(title_components) < 2:
            return [RuleViolation(self.id, error, line_nr=1)]

        exclusions = self.options["exclusions"].value
        exclusions_text = ", or ".join(exclusions)
        if exclusions_text:
            exclusions_text = " (or {})".format(exclusions_text)
        error = (
            f"Areas at start of title should be lower case{exclusions_text}, "
            "followed by ': '"
        )

        def deny_capital_text(text: str) -> bool:
            if text in exclusions:
                return False
            if not text.islower():
                return True
            return False

        for area in title_components[:-1]:
            if any(deny_capital_text(word) for word in area.split("/")) or " " in area:
                violations += [RuleViolation(self.id, error, line_nr=1)]

        error = "Summary of change, after area(s), should be capitalized"
        if not title_components[-1][0].isupper():
            violations += [RuleViolation(self.id, error, line_nr=1)]

        return violations
