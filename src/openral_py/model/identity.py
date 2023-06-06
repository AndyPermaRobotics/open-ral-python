

from typing import Optional


class Identity:
    def __init__(
        self, 
        uid: str, 
        name: Optional[str] = None, 
        siteTag: Optional[str] = None, 
        alternateIDs: list = [], 
        alternateNames: list = []
    ):
        self.uid = uid
        self.name = name
        self.siteTag = siteTag
        self.alternateIDs = alternateIDs
        self.alternateNames = alternateNames

    def to_map(self):
        return {
            "UID": self.uid,
            "name": self.name,
            "siteTag": self.siteTag,
            "alternateIDs": self.alternateIDs,
            "alternateNames": self.alternateNames,
        }
    
    @staticmethod
    def from_map(data):
        return Identity(
            uid=data.get("UID"),
            name=data.get("name"),
            siteTag=data.get("siteTag"),
            alternateIDs=data.get("alternateIDs", []),
            alternateNames=data.get("alternateNames", []),
        )