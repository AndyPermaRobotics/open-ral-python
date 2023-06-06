from typing import Any, Dict, Optional


class Template:
    def __init__(self, ral_type: str, version: str, object_state_templates: Optional[str] = None):
        self.ral_type = ral_type
        self.version = version
        self.object_state_templates = object_state_templates

    def to_map(self) -> Dict[str, Any]:
        return {
            'RALType': self.ral_type,
            'version': self.version,
            'objectStateTemplates': self.object_state_templates,
        }