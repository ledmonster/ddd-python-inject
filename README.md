# Todo List

DDD, CQRS and Hexagonal Architecture example using inject package.

Presentation slide in PyCon JP 2017: [Python におけるドメイン駆動設計(戦術面)の勘どころ](https://www.slideshare.net/secret/6DnooTLkqmnXsz)

# Architecture

![architecture](image/architecture.png?raw=true "Architecture")

# Requirements

- click
- enum34
- inject
- gxredis
- pytest

# Setup

```
$ git clone https://github.com/ledmonster/ddd-python-inject
$ cd todolist
$ python setup.py develop
```

Also, you need to run redis.

# Usage

``` bash
$ ./bin/todo add --name foo
#1: foo

$ ./bin/todo add --name bar
#2: bar

$ ./bin/todo add --name baz
#3: baz

$ ./bin/todo list
[ ] #1: foo
[ ] #3: baz
[ ] #2: bar

$ ./bin/todo done 2
[x] #2: bar

$ ./bin/todo list
[ ] #1: foo
[ ] #3: baz
[x] #2: bar
```
