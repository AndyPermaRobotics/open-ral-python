


from ast import Dict
from typing import Any

import pytest

from openral_py.repository import MockRalRepository


class TestMockRalRepository:

    @pytest.fixture
    def docs_by_uid(self) -> dict[str, Any]:
        return {
            "myUid": {
                "identity": {
                    "UID": "myUid",
                    "name": "PC instance",
                    "siteTag": "PER",
                },
                "definition": {
                    "definitionText": "Is a software that serves MQTT messages.",
                    "definitionURL": "",
                },
                "objectState": "undefined",
                "template": {
                    "RALType": "pc_instance",
                    "version": "1",
                    "objectStateTemplates": "",
                },
                "specificProperties": [
                    {"key": "lastUpdateTimestamp", "value": "value", "unit": "timestamp"},
                    {"key": "ipAddress", "value": "[add IP address here]", "unit": "string"},
                    {"key": "port", "value": "[add port here]", "unit": "string"}
                ],
                "currentGeolocation": {
                    "container": {"UID": "container1"}
                },
                "locationHistoryRef": [],
                "ownerHistoryRef": [],
                "methodHistoryRef": [],
                "linkedObjectRef": []
            }
        }
    
    @pytest.fixture
    def docs_by_container_id(self) -> dict[str, list[str]]:
        return {
            "container1": ["myUid"]
        }

    @pytest.mark.asyncio
    async def test_get_ral_object_by_uid_success(
            self, 
            docs_by_uid: dict[str, Any],
            docs_by_container_id: dict[str, list[str]],
        ):
        
        repository = MockRalRepository(docs_by_uid, docs_by_container_id)
        ral_object = await repository.getRalObjectByUid("myUid")
        
        assert ral_object.identity.uid == "myUid", "Expected uid to be 'myUid'"
        