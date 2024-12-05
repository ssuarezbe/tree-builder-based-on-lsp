# Whats parts have a query planner

* https://planetscale.com/blog/what-is-a-query-planner	
* https://medium.com/@ahmed.abdelfaheem/query-plan-in-a-nutshell-6da5c89bb9b

1. Lexing & Parse the query
2. Generate candidate plans
3. Cost estimation
4. Plan selection
5. Execution

## guide to implementing a cost-based query planner

* https://github.com/tuannh982/query-planner-guide

## Simple query planner code sample

* Query Planning with Apache Calcite: Part 1 
  * https://medium.com/@mpathirage/query-planning-with-apache-calcite-part-1-fe957b011c36
  * https://github.com/milinda/calcite-tutorial/blob/master/src/main/java/org/pathirage/calcite/tutorial/planner/SimpleQueryPlanner.java#L31

* Assembling a query optimizer with Apache Calcite
  * https://www.querifylabs.com/blog/assembling-a-query-optimizer-with-apache-calcite

DEMOSTRATION of a QUERY PLANNER creation
| | | |


* One query plan, three different engines.
  * https://medium.com/@omri-levy/one-query-plan-three-different-engines-e5dc74aeb52f

* Substrait: Cross-Language Serialization for Relational Algebra¶
  * https://substrait.io/
  * WARNING: The query plan are not designed for humans

### Should we use Apache Calcite or Substrait? #7

* https://github.com/sutoiku/puffin/issues/7

```
Calcite and DataFusion are both good choices. Calcite is implemented in Java, and DataFusion is implemented in Rust, so that maybe will influence the decision here.

It looks like you are planning to use Arrow, and DataFusion is part of the Arrow project and designed for Arrow. If you are just using logical plans, it won't have any impact, but if you use DataFusion's physical plans then it may be better aligned.

Ballista is a distributed scheduler currently tied to DataFusion for the query engine. Ballista has a proprietary protobuf format for query plans (created before Substrait existed). I would like to add Substrait support to Ballista so that it can be a distributed scheduler for any query engine that supports Substrait (such as DuckDB), but I do not use Ballista in my day job, so cannot spend much time on it these days.
```

* The goal of this project is to assess which query engines can realistically run inside cloud functions (in particular AWS Lambda) and have a first feeling about their performances in this highly constrained environment.
  * https://github.com/cloudfuse-io/lambdatization

* Example of metric that can be used for optmization
  * https://www.cloudfuse.io/dashboards/standalone-engines


# Why write a query planner

* https://vitess.io/blog/2021-11-02-why-write-new-planner/