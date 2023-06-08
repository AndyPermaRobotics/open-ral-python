from typing import Callable, Dict, List, Optional, TypeVar

from openral_py.model.specific_properties import SpecificProperties
from openral_py.ral_object import RalObject
from openral_py.repository.ral_repository import RalRepository

#todo generics
S = TypeVar('S', bound=SpecificProperties)

class MockRalRepository(RalRepository):
    def __init__(self, docsByUid: Dict[str, dict], docsByContainerId: Dict[str, List[str]]) -> None:
        self.docsByUid = docsByUid
        self.docsByContainerId = docsByContainerId
    
    async def getRalObjectByUid(self, uid: str, specificPropertiesTransform: Optional[Callable] = None) -> RalObject:
        doc = self.docsByUid.get(uid)
        
        if not doc:
            raise Exception(f"No RalObject found for uid '{uid}'")
        
        ral_object = RalObject.from_map(doc)
        
        return ral_object
    
    async def getRalObjectsWithContainerId(self, containerId: str) -> List[RalObject]:
        uids = self.docsByContainerId.get(containerId)
        
        if not uids:
            return []
        
        result = []
        
        for uid in uids:
            object = await self.getRalObjectByUid(uid)
            result.append(object)
        
        return result
