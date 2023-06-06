from typing import Any, Dict, Optional

from openral_py.model.container import Container


class CurrentGeoLocation:
    def __init__(self, container: Optional[Container] = None):
        self.container = container

    def to_map(self) -> Dict[str, Any]:
        return {
            'container': self.container.to_map() if self.container is not None else None,
        }