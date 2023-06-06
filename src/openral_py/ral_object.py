
from typing import Callable

from openral_py.model.current_geo_location import CurrentGeoLocation

from .model.definition import Definition
from .model.identity import Identity
from .model.specific_properties import SpecificProperties
from .model.template import Template


class RalObject:
    def __init__(
            self, 
            identity: Identity, 
            definition: Definition,  
            template: Template, 
            specificProperties: SpecificProperties, 
            currentGeolocation: CurrentGeoLocation = CurrentGeoLocation(), 
            currentOwners: list[str] = [], 
            objectState: str = "undefined", 
            locationHistoryRef: list[str] = [], 
            ownerHistoryRef: list[str] = [], 
            methodHistoryRef: list[str] = [], 
            linkedObjectRef: list[str] = []
        ):
        self.identity = identity
        self.currentOwners = currentOwners
        self.definition = definition
        self.objectState = objectState
        self.template = template
        self._specificProperties = specificProperties
        self.currentGeolocation = currentGeolocation
        self.locationHistoryRef = locationHistoryRef
        self.ownerHistoryRef = ownerHistoryRef
        self.methodHistoryRef = methodHistoryRef
        self.linkedObjectRef = linkedObjectRef
    
    @property
    def specificProperties(self):
        return self._specificProperties
    
    # @staticmethod
    # def fromMap(map: dict, specificPropertiesTransform: callable = None) -> Either[RalObject, ParsingError]:
    #     parserFactory = RalObjectParser()
    #     parsingResult = parserFactory.fromMap(map)
    #     if parsingResult.isRight:
    #         return Right(parsingResult.right)
    #     else:
    #         originalObject = parsingResult.left
    #         if specificPropertiesTransform is not None:
    #             transformed = originalObject.transformTo(specificPropertiesTransform)
    #             return Left(transformed)
    #         else:
    #             return Left(parsingResult.left)

    def transformTo(self, specificPropertiesTransform: Callable) -> 'RalObject':
        return RalObject(
            identity=self.identity,
            currentOwners=self.currentOwners,
            definition=self.definition,
            objectState=self.objectState,
            template=self.template,
            specificProperties=specificPropertiesTransform(self._specificProperties),
            currentGeolocation=self.currentGeolocation,
            locationHistoryRef=self.locationHistoryRef,
            ownerHistoryRef=self.ownerHistoryRef,
            methodHistoryRef=self.methodHistoryRef,
            linkedObjectRef=self.linkedObjectRef
        )

    def to_map(self) -> dict:
        return {
            "identity": self.identity.to_map(),
            "currentOwners": self.currentOwners,
            "definition": self.definition.to_map(),
            "objectState": self.objectState,
            "template": self.template.to_map(),
            "specificProperties": self.specificProperties.to_maps(),
            "currentGeolocation": self.currentGeolocation.to_map(),
            "locationHistoryRef": self.locationHistoryRef,
            "ownerHistoryRef": self.ownerHistoryRef,
            "methodHistoryRef": self.methodHistoryRef,
            "linkedObjectRef": self.linkedObjectRef
        }
