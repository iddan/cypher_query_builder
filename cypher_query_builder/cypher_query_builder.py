from functools import singledispatch
from typing import Type, Union, Any, TypeVar, Tuple

T = TypeVar("T")
InstanceOrType = Union[T, Type[T]]


class Attributable:
    def __getattr__(self, name: str) -> "AttributeReference":
        raise NotImplementedError()


class AttributeReference(Attributable):
    pass


class RelationMeta(type):
    def __or__(self, relation):
        raise NotImplementedError()

    def __mul__(self, times: Union[range, int]):
        raise NotImplementedError()


class Relation(Attributable, metaclass=RelationMeta):
    def __init__(self, **kwargs):
        pass

    def __or__(self, relation: "Relation") -> "Relation":
        raise NotImplementedError()

    def __mul__(self, times: Union[range, int]) -> "Relation":
        raise NotImplementedError()

    @classmethod
    def Not(cls) -> "Relation":
        raise NotImplementedError()

    @classmethod
    def many(cls) -> "Relation":
        raise NotImplementedError()

    @staticmethod
    def id(count: int) -> "Relation":
        raise NotImplementedError()


class ByConnector:
    def to(self, node: Union["Node", Type["Node"]]) -> "Path":
        raise NotImplementedError()


class Connectable:
    def relates_to(self, node: InstanceOrType[Node]) -> "Path":
        raise NotImplementedError()

    def relates_by(self, relation: InstanceOrType[Relation]) -> ByConnector:
        raise NotImplementedError()

    def outgoes_to(self, node: InstanceOrType[Node]) -> "Path":
        raise NotImplementedError()

    def outgoes_by(self, relation: InstanceOrType[Relation]) -> ByConnector:
        raise NotImplementedError()

    def ingoes_to(self, node: InstanceOrType[Node]) -> "Path":
        raise NotImplementedError()

    def ingoes_by(self, relation: InstanceOrType[Relation]) -> ByConnector:
        raise NotImplementedError()


class Path(Connectable):
    @staticmethod
    def shortest(path: "Path") -> "Path":
        raise NotImplementedError()

    @staticmethod
    def all_shortest(path: "Path") -> "Path":
        raise NotImplementedError()


class Node(Connectable, Attributable):
    def __init__(self, **kwargs):
        raise NotImplementedError()

    def __getattr__(self, name: str) -> AttributeReference:
        raise NotImplementedError()

    @staticmethod
    def id(count: Union[int, Tuple[int, ...]]) -> "Node":
        raise NotImplementedError()


class Model:
    pass


_Node = Node
_Relation = Relation


class NodeModel(Model):
    Node: Type[_Node]


class RelationModel(Model):
    Relation: Type[_Relation]


Projection = Union[
    Node,
    AttributeReference,
    Relation,
    Type[Relation],
    Tuple[Union[Node, AttributeReference, Relation, Type[Relation]], ...],
    Path,
]


class Clause:
    def __init__(self, val):
        raise NotImplementedError()

    def create(self, val: Path) -> "Clause":
        raise NotImplementedError()

    # TODO define as singledispatch and define return type for each input
    def project(self, projection: Projection) -> Any:
        raise NotImplementedError()


class match(Clause):
    def __init__(self, val: Union[Node, Path, Tuple[Node, ...]]) -> None:
        raise NotImplementedError()
