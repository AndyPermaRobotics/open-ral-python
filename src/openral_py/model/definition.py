from typing import Optional


class Definition:
    def __init__(self, definition_text: Optional[str] = None, definition_url: Optional[str] = None):
        self.definition_text = definition_text
        self.definition_url = definition_url

    def to_map(self):
        return {
            'definitionText': self.definition_text,
            'definitionURL': self.definition_url,
        }