import pytest

from src.openral_py.model.identity import Identity


class TestIdentity:
    @staticmethod
    def from_map(data):
        return Identity(
            uid=data.get("UID"),
            name=data.get("name"),
            siteTag=data.get("siteTag"),
            alternateIDs=data.get("alternateIDs", []),
            alternateNames=data.get("alternateNames", []),
        )

    def test_from_map_with_empty_data(self):
        # arrange
        data = {}

        # act
        identity = self.from_map(data)

        # assert
        assert identity.uid is None
        assert identity.name is None
        assert identity.siteTag is None
        assert identity.alternateIDs == []
        assert identity.alternateNames == []

    def test_from_map_with_full_data(self):
        # arrange
        data = {
            "UID": 123,
            "name": "John",
            "siteTag": "example.com",
            "alternateIDs": [456, 789],
            "alternateNames": ["Johnny"],
        }

        # act
        identity = self.from_map(data)

        # assert
        assert identity.uid == 123
        assert identity.name == "John"
        assert identity.siteTag == "example.com"
        assert identity.alternateIDs == [456, 789]
        assert identity.alternateNames == ["Johnny"]