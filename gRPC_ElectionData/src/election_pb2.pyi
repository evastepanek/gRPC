from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ElectionData(_message.Message):
    __slots__ = ("regionID", "electionRegion", "partys")
    REGIONID_FIELD_NUMBER: _ClassVar[int]
    ELECTIONREGION_FIELD_NUMBER: _ClassVar[int]
    PARTYS_FIELD_NUMBER: _ClassVar[int]
    regionID: str
    electionRegion: str
    partys: _containers.RepeatedCompositeFieldContainer[Party]
    def __init__(self, regionID: _Optional[str] = ..., electionRegion: _Optional[str] = ..., partys: _Optional[_Iterable[_Union[Party, _Mapping]]] = ...) -> None: ...

class Party(_message.Message):
    __slots__ = ("partyID", "partyName", "vorzug", "votes")
    PARTYID_FIELD_NUMBER: _ClassVar[int]
    PARTYNAME_FIELD_NUMBER: _ClassVar[int]
    VORZUG_FIELD_NUMBER: _ClassVar[int]
    VOTES_FIELD_NUMBER: _ClassVar[int]
    partyID: int
    partyName: str
    vorzug: _containers.RepeatedCompositeFieldContainer[Vorzugsstimmen]
    votes: int
    def __init__(self, partyID: _Optional[int] = ..., partyName: _Optional[str] = ..., vorzug: _Optional[_Iterable[_Union[Vorzugsstimmen, _Mapping]]] = ..., votes: _Optional[int] = ...) -> None: ...

class Vorzugsstimmen(_message.Message):
    __slots__ = ("vorzugName", "stimmenAnzahl", "listennummer")
    VORZUGNAME_FIELD_NUMBER: _ClassVar[int]
    STIMMENANZAHL_FIELD_NUMBER: _ClassVar[int]
    LISTENNUMMER_FIELD_NUMBER: _ClassVar[int]
    vorzugName: str
    stimmenAnzahl: int
    listennummer: int
    def __init__(self, vorzugName: _Optional[str] = ..., stimmenAnzahl: _Optional[int] = ..., listennummer: _Optional[int] = ...) -> None: ...

class MessageRequest(_message.Message):
    __slots__ = ("regionID",)
    REGIONID_FIELD_NUMBER: _ClassVar[int]
    regionID: str
    def __init__(self, regionID: _Optional[str] = ...) -> None: ...

class MessageResponse(_message.Message):
    __slots__ = ("responseData",)
    RESPONSEDATA_FIELD_NUMBER: _ClassVar[int]
    responseData: str
    def __init__(self, responseData: _Optional[str] = ...) -> None: ...
