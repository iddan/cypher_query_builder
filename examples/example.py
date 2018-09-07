from cypher_query_builder import NodeModel, RelationModel, match, Node, Relation, Path

# Get all nodes
node = Node()
match(node).project(node)

# Get all nodes with a label
class Movie(NodeModel):
    title: str


movie = Movie.Node()
match(movie).project(movie.title)

# Related nodes
class Person(NodeModel):
    name: str


class Director(Person):
    pass


movie = Movie.Node()
match(movie.relates_to(Director.Node(name="Oliver Stone"))).project(movie.title)

# Match with labels
movie = Movie.Node()
match(Person.Node(name="Oliver Stone").relates_to(movie)).project(movie.title)

# Outgoing relationships
movie = Movie.Node()
match(Person.Node(name="Oliver Stone").outgoes_to(movie)).project(movie.title)

# Directed relationships and variable
movie = Movie.Node()
relation = Relation()
match(Person.Node(name="Oliver Stone").outgoes_by(relation).to(movie)).project(
    type(relation)
)

# Match on relationship type
class ActedIn(RelationModel):
    role: str


class Actor(Person):
    pass


actor = Actor.Node()
match(Movie.Node(title="Wall Street").ingoes_by(ActedIn.Relation).to(actor)).project(
    actor.name
)

# Match on multiple relationship types
class Directed(RelationModel):
    pass


person = Person.Node()
match(
    Movie.Node(title="Wall Street")
    .ingoes_by(ActedIn.Relation | Directed.Relation)
    .to(person)
).project(person.name)

# Match on relationship type and use a variable
acted_in = ActedIn.Relation()
match(Movie.Node(title="Wall Street").ingoes_by(acted_in).to(Actor.Node)).project(
    acted_in.role
)

# Multiple relationships
director = Director.Node()
movie = Movie.Node()
match(
    Person.Node(name="Charlie Sheen")
    .outgoes_by(ActedIn.Relation)
    .to(movie)
    .ingoes_by(Directed.Relation)
    .to(director)
).project((movie.title, director.name))

# Variable length relationships
movie = Movie.Node()
match(
    Person.Node(name="Charlie Sheen")
    .relates_by(ActedIn.Relation * range(1, 3))
    .to(movie)
).project(movie.title)

# Relationship variable in variable length relationships
match(
    Actor.Node(name="Charlie Sheen").relates_by(ActedIn.Relation * 2).to(Actor.Node)
).project(Relation.many())

# Match with properties on a variable length path
charlie = Person.Node(name="Charlie Sheen")
martin = Person.Node(name="Martin Sheen")


class X(RelationModel):
    blocked: bool


class Unblocked(NodeModel):
    pass


class Blocked(NodeModel):
    pass


match((charlie, martin)).create(
    charlie.outgoes_by(X.Relation(blocked=False))
    .to(Unblocked.Node)
    .ingoes_by(X.Relation(blocked=False))
    .to(martin)
).create(
    charlie.outgoes_by(X.Relation(blocked=True))
    .to(Blocked.Node)
    .ingoes_by(X.Relation(blocked=True))
    .to(martin)
)


charlie = Person.Node(name="Charlie Sheen")
martin = Person.Node(name="Martin Sheen")
p = charlie.relates_by(Relation(blocked=False)).to(martin)
match(p).project(p)

# Zero length paths
x = Node()
match(Movie.Node(title="Wall Street").relates_by(Relation * range(0, 1)).to(x)).project(
    x
)

# Named paths
p = Node(name="Michael Douglas").relates_to(Node)
match(p).project(p)

# Matching on a bound relationship
a = Node()
b = Node()
match(a.relates_by(Relation.id(0)).to(b)).project((a, b))

# Single shortest path
martin = Person.Node(name="Martin Sheen")
oliver = Person.Node(name="Oliver Stone")
p = Path.shortest(martin.relates_by(Relation * range(15)).to(oliver))
match(p).project(p)

# Single shortest path with predicates
class Father(Relation):
    pass


charlie = Person.Node(name="Charlie Sheen")
martin = Person.Node(name="Martin Sheen")
p = Path.shortest(charlie.relates_by(Father.Not()).to(martin))

match(p).project(p)

# All shortest paths
martin = Person.Node(name="Martin Sheen")
michael = Person.Node(name="Michael Douglas")
p = Path.all_shortest(martin.relates_to(michael))
match(p).project(p)

# Node by id
n = Node.id(0)
match(n).project(n)

# Relationship by id
r = Relation.id(0)
match(Node().relates_by(r).to(Node())).project(r)

# Multiple nodes by id
n = Node.id((0, 3, 5))
match(n).project(n)
