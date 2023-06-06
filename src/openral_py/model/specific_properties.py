from typing import Any, Dict, List, Optional

from specific_property import SpecificProperty


class SpecificProperties:
    def __init__(self, specific_properties: Dict[str, SpecificProperty]):
        self._specific_properties = specific_properties

    def __getitem__(self, key: str) -> Optional[Any]:
        specific_property = self._specific_properties.get(key, None)
        return specific_property.value if specific_property is not None else None
        
    def contains_key(self, key: str) -> bool:
        return key in self._specific_properties

    def get(self, key: str) -> Optional[SpecificProperty]:
        return self._specific_properties.get(key, None)

    @property
    def map(self) -> Dict[str, SpecificProperty]:
        return self._specific_properties.copy()

    def to_maps(self) -> List[Dict[str, Any]]:
        return [value.to_map() for value in self._specific_properties.values()]
