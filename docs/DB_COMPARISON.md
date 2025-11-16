# Database Selection — Expense Tracker Application 🗃️💰

## 1. What is an SQL Database? 🧾⚖️
SQL (Structured Query Language) databases are relational systems that store data in tables with a strict schema. They excel at structured data with well-defined relationships.

**Common SQL options**
- PostgreSQL 🐘
- MySQL / MariaDB 🐬
- SQLite 🗂️
- Microsoft SQL Server 🖥️
- Oracle Database ☯️

**Advantages**
- Well-defined schemas → consistent, predictable data
- Strong relational features (foreign keys, constraints)
- ACID-compliant transactions
- Powerful querying (JOINs, aggregations, filtering)
- Mature ecosystem & tooling

**Disadvantages**
- Less schema flexibility
- Requires migrations for structural changes
- Horizontal scaling is more complex
- Not ideal for unstructured or inconsistent data

---

## 2. What is a NoSQL Database? 📦⚡
NoSQL databases provide non-relational, flexible storage using documents, key-value pairs, graphs, or wide-column models.

**Common NoSQL options**
- MongoDB (document store) 🍃
- Redis (in-memory key-value) 🧠
- Cassandra (distributed wide-column) ⛓️
- Firestore (cloud document store) ☁️
- Neo4j (graph) 🔗

**Advantages**
- Schema flexibility
- Excellent horizontal scaling
- High write throughput
- Good for nested or evolving data

**Disadvantages**
- Limited relational integrity (weak/absent foreign keys)
- JOIN-like operations costly or unsupported
- Transactions vary by product
- No single standard query language
- Potential for duplicated/inconsistent data

---

## 3. Application-specific Challenges 🔎
The app needs to track:

- Users — `user_id`, `username`, `password`
- Expenses — `expense_id`, `user_id`, `tag_id`, `amount`, `date`, `description`
- tags — `tag_id`, `tag_name`

Relational requirements:
- A user has many expenses
- A tag has many expenses
- Each expense must reference a valid user & tag

Additional technical needs:
- Maintain strict data integrity (no orphaned expenses)
- Analytical & aggregated queries (monthly totals, tag breakdowns, custom filters)
- Reliable, transactional updates
- Predictable containerized deployments (Docker)
- Low-to-moderate learning curve and strong ecosystem support
- Smooth integration with FastAPI microservices

---

## 4. Comparison: SQL Options (high-level) 🏷️

### PostgreSQL (Recommended) 🐘
**Pros**
- Excellent relational integrity
- Advanced SQL features (window functions, `JSONB`, indexes)
- Strong community & ecosystem
- Works well with ORMs (SQLAlchemy, Prisma, Django ORM)
- Stable official Docker images

**Cons**
- Slightly more complex initial configuration
- Some advanced features require deeper SQL knowledge

### MySQL / MariaDB 🐬
**Pros**
- Easy to start
- Fast for basic ops
- Rich ecosystem & hosting support

**Cons**
- Less flexible for complex relational queries
- Historical JSON/document support weaker vs PostgreSQL
- Some SQL behavior differs from standard

### SQLite 🗂️
**Pros**
- Extremely easy setup
- File-based, lightweight
- Great for local/dev/mobile

**Cons**
- Not ideal for multi-user backend services
- Limited concurrency
- Not the best fit for containerized microservice backends

---

## 5. Comparison: NoSQL Options (high-level) 🔍

### MongoDB 🍃
**Pros**
- Flexible schema, good for varying/unstructured data
- Easy to store nested objects

**Cons**
- Poor fit for relational constraints
- JOIN-like queries expensive
- Expense relationships may become duplicated

### Redis 🧠
**Pros**
- Extremely fast (caching, ephemeral data)
- Simple key-value operations

**Cons**
- Not appropriate as primary persistent store
- No native relational model

---

## 6. Consolidated Comparison (including deployment & FastAPI) 📊

| Evaluation Concern | PostgreSQL (SQL) | Other SQL | NoSQL |
|---|---:|---:|---:|
| Relational support | ★★★★★ | ★★★★☆ | ★☆☆☆☆ |
| Learning curve | ★★★★☆ | ★★★★☆ | ★★★☆☆ |
| Ecosystem support | ★★★★★ | ★★★★☆ | ★★★☆☆ |
| Deployment (Docker) | ★★★★★ | ★★★★☆ | ★★★★☆ |
| FastAPI compatibility | ★★★★★ | ★★★★☆ | ★★☆☆☆ |
| Querying & analytics | ★★★★★ | ★★★★☆ | ★★☆☆☆ |
| Data integrity | ★★★★★ | ★★★★☆ | ★★☆☆☆ |
| Fit for expense tracker | ✅ Excellent | ✅ Good | ❌ Poor |

Summary: PostgreSQL best balances relational modeling, analytics, tooling, and Docker/FastAPI friendliness.

---

## 7. Final Recommendation ✅🚀
Use **PostgreSQL** for the expense-tracking application.

Why:
- Natural fit for `user` → `expenses` → `tags` relationships
- Strong enforcement of referential integrity and transactions
- Excellent support for analytics (aggregations, window functions)
- Rich ecosystem and ORMs that integrate smoothly with FastAPI
- Reliable Docker images and predictable deployment behavior
- Scales cleanly as the application grows