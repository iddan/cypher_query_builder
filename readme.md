# Cypher Query Builder

Python Query builder for [Cypher, the graph query language](https://neo4j.com/cypher-graph-query-language)

### Features

- Pythonic: Syntax is readable and familiar for Python developers. Objects are used wherever possible.
- [Type Safe](http://mypy-lang.org/): Nodes are defined by models which are typed classes. All interfaces are defined by strong types which make sure no call will fail in runtime because of a type bug.

### Roadmap

- [x] Define interfaces
- [x] Cover all examples provided by Neo4j for Match
- [ ] Define test cases for interfaces
- [ ] Implement interfaces
- [ ] Integrate with the [Neo4j Python driver](https://github.com/neo4j/neo4j-python-driver)
- [ ] Cover all operators
- [ ] Cover all functions
- [ ] Cover all clauses

### Prior Art

- [Pypher](https://github.com/emehrkay/Pypher) -
  Pypher is a tiny library that focuses on building Cypher queries by constructing pure Python objects.

### Develop

#### Init workspace

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv --python $(pyenv root)/versions/3.7.0/bin/python
pipenv install --dev
```
