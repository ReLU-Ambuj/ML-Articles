# 🗄️ DATABASE MODELLING — MIDSEM CRASH PREP (25 MARKS)
### Score 20+/25 using the Pareto Principle

> **Exam Tomorrow | Focus: Module I + Module III (1NF, 2NF only)**
> Modules IV and V → IGNORED

---

# 📑 TABLE OF CONTENTS

| Section | Topics |
|---------|--------|
| A | ER Modelling (Entity, Attributes, Relationships) |
| B | Relational Model (Integrity Constraints, DDL, DML, SQL) |
| C | Relational Algebra |
| D | ER → Relational Mapping |
| E | Functional Dependency |
| F | Normalization (1NF, 2NF) |
| G | Ultimate 5-Page Revision Sheet |
| H | Predicted Questions + Mock Test |

---

# ═══════════════════════════════════
# SECTION A : ER MODELLING
# ═══════════════════════════════════

---

## 📌 TOPIC 1 : ER DIAGRAM

### 1. Exam Definition (2 Marker)
> An **Entity-Relationship (ER) Diagram** is a graphical representation of entities and their relationships in a database. It was proposed by **Peter Chen in 1976**. It uses rectangles for entities, ellipses for attributes, diamonds for relationships, and lines for links.

---

### 2. Intuition
Think of a **university database**:
- **Students** exist → they are *Entities*
- Each student has a **name, roll number, age** → these are *Attributes*
- Students **enroll in** courses → that's a *Relationship*

ER Diagram is just a **blueprint** of your database before you build it.

---

### 3. ER Diagram Components

```
┌─────────────────────────────────────────────────────────────┐
│                    ER DIAGRAM SYMBOLS                       │
├──────────────────────┬──────────────────────────────────────┤
│ SYMBOL               │ MEANING                              │
├──────────────────────┼──────────────────────────────────────┤
│ Rectangle  □         │ Entity (Strong)                      │
│ Double Rect ═══      │ Weak Entity                          │
│ Ellipse    ○         │ Attribute                            │
│ Double Oval ══○      │ Multivalued Attribute                │
│ Dashed Oval --○      │ Derived Attribute                    │
│ Underlined  <u>A</u> │ Key Attribute (Primary Key)         │
│ Diamond    ◇         │ Relationship (Strong)                │
│ Double ◈             │ Identifying Relationship (Weak)      │
│ Line       ──        │ Link between entity and attribute    │
│ Double Line ══       │ Total Participation                  │
│ Single Line ─        │ Partial Participation                │
└──────────────────────┴──────────────────────────────────────┘
```

---

### 4. Types of Attributes

```
ATTRIBUTES
├── Simple Attribute       → Cannot be divided further. e.g., Age
├── Composite Attribute   → Can be divided. e.g., Name = {FName, LName}
├── Single-Valued Attr    → One value per entity. e.g., DOB
├── Multivalued Attribute  → Multiple values. e.g., Phone_Numbers
├── Derived Attribute     → Calculated from another. e.g., Age from DOB
└── Key Attribute         → Uniquely identifies entity. e.g., Roll_No
```

**Text Diagram for Student Entity:**

```
        ○ Roll_No (underlined = key)
        |
○Name ──[STUDENT]── ○ Age (derived → dashed oval)
        |
        ○══ Phone (double oval = multivalued)
        |
        ○ Address (composite: {Street, City, PIN})
```

---

### 5. Complete ER Example

**Scenario:** University has Students, Courses, and Professors.

```
                    ○ SID
                    |
   ○ Sname ────[STUDENT]══════<ENROLLS>──────[COURSE]──── ○ CID
                    |          M         N    |
                    ○ Age                     ○ CName
                                              |
                           [TEACHES]──────[PROFESSOR]──── ○ PID
                             1        N       |
                                              ○ PName
```

---

### 6. PYQ Style Answer

**Q: Draw an ER diagram for a Hospital Management System.**

**Answer:**
```
Entities: PATIENT, DOCTOR, WARD
Relationships: PATIENT is-treated-by DOCTOR (M:N)
               PATIENT is-admitted-in WARD (M:1)

        ○ PID                    ○ DID
        |                        |
  [PATIENT]══<TREATED_BY>══[DOCTOR]
        |      M          N      |
        ○ PName                  ○ DName
        ○ Age                    ○ Specialization

        ○ WardNo
        |
  [WARD]──<ADMITTED_IN>──[PATIENT]
              1               M
```

---

### 7. Common Mistakes
- ❌ Using rectangle for weak entity (should be double rectangle)
- ❌ Forgetting to underline key attribute
- ❌ Using single line for total participation (should be double line)
- ❌ Drawing derived attribute as normal ellipse (should be dashed)

### 8. Memory Trick
> **"RACED"** = Rectangle, Attribute-ellipse, Composite-subdivision, Entity-key underlined, Diamond-relationship

### 9. Expected Marks
| Question Type | Marks |
|--------------|-------|
| Define ER Diagram | 2 marks |
| List components with symbols | 3 marks |
| Draw complete ER diagram | 5 marks |

---

## 📌 TOPIC 2 : CARDINALITY CONSTRAINTS

### 1. Exam Definition
> **Cardinality Ratio** specifies the maximum number of relationship instances that an entity can participate in. The four types are: **1:1, 1:N, N:1, and M:N**.

---

### 2. Intuition
Cardinality = **"How many of A can relate to how many of B?"**

---

### 3. Diagrams

**1:1 (One-to-One)**
```
[EMPLOYEE] ──1──<MANAGES>──1──[DEPARTMENT]
(Each employee manages at most one department)
```

**1:N (One-to-Many)**
```
[DEPARTMENT] ──1──<HAS>──N──[EMPLOYEE]
(One department has many employees)
```

**M:N (Many-to-Many)**
```
[STUDENT] ──M──<ENROLLS>──N──[COURSE]
(Many students enroll in many courses)
```

---

### 4. Conversion to Tables

| Cardinality | Table Strategy |
|-------------|---------------|
| **1:1** | Merge both entities OR add FK in either table |
| **1:N** | Add FK of "1-side" into "N-side" table |
| **M:N** | Create a **new junction/bridge table** with FKs of both |

**Example: STUDENT (M) — ENROLLS — COURSE (N)**
```sql
-- New junction table created:
ENROLLS(SID, CID, EnrollDate)
-- SID references STUDENT, CID references COURSE
-- PK = (SID, CID)
```

---

### 5. PYQ Answer
**Q: Explain cardinality constraints with examples.**

> Cardinality constraints define the maximum number of times an entity instance can participate in a relationship. 
> - **1:1** → One employee manages one department.
> - **1:N** → One department has many employees.
> - **M:N** → Many students enroll in many courses.
> Cardinality is shown in ER diagram by placing **1, M, or N** near the relationship lines.

### 6. Memory Trick
> **"1:1 merge, 1:N foreign key in N, M:N new table"**

### 7. Expected Marks: 3–5 marker

---

## 📌 TOPIC 3 : PARTICIPATION CONSTRAINTS

### 1. Exam Definition
> **Participation Constraint** specifies whether the existence of an entity depends on its relationship with another entity. It has two types:
> - **Total Participation**: Every entity must participate in the relationship (shown by **double line**)
> - **Partial Participation**: An entity MAY participate in the relationship (shown by **single line**)

---

### 2. Intuition
- **Total Participation** = MANDATORY (every row must have a match)
- **Partial Participation** = OPTIONAL (some rows may not have a match)

---

### 3. Diagram

```
EMPLOYEE must work for DEPARTMENT (Total from EMPLOYEE side)
DEPARTMENT may not have employees yet (Partial from DEPARTMENT side)

[EMPLOYEE]══════<WORKS_FOR>──────[DEPARTMENT]
    Total                  Partial
(double line)           (single line)

══ = Total Participation (double line)
── = Partial Participation (single line)
```

---

### 4. PYQ Style Answer

**Q: Differentiate between Total and Partial Participation.**

| Feature | Total Participation | Partial Participation |
|---------|--------------------|-----------------------|
| Meaning | Every entity MUST participate | Entity MAY or MAY NOT participate |
| Symbol | Double line (══) | Single line (──) |
| Constraint Type | Mandatory | Optional |
| Also called | Existence dependency | — |
| Example | Every EMPLOYEE must work in a DEPT | Every DEPT may not have a MANAGER |
| SQL equivalent | NOT NULL foreign key | NULL allowed foreign key |

---

### 5. Common Mistakes
- ❌ Confusing total participation with 1:1 cardinality
- ❌ Drawing double line on wrong side

### 6. Memory Trick
> **"Total = Two lines = Totally mandatory"**

### 7. Expected Marks: 2–3 marker

---

## 📌 TOPIC 4 : WEAK ENTITY

### 1. Exam Definition
> A **Weak Entity** is an entity that does not have a primary key of its own and depends on a **strong (owner) entity** for its existence. It is identified by a **partial key (discriminator)** combined with the primary key of its owner entity. The relationship connecting them is called an **Identifying Relationship**.

---

### 2. Intuition
- **Bank Account** → Strong Entity (has Account_No)
- **Transaction** → Weak Entity (has Transaction_Slip_No, but it means nothing without knowing WHICH account)
- Transaction cannot exist without Account → **Existence Dependent**

---

### 3. Diagram

```
        ○ Account_No (key)          ○~~TxnSlip~~ (partial key - dashed underline)
        |                            |
  [ACCOUNT]══════<◈MAKES>════[TRANSACTION]
   (Strong)    (double diamond)   (double rect)
               Identifying Rel.   (Weak Entity)
               
Legend:
[  ] = Strong Entity (single rect)
[══] = Weak Entity (double rect)
◇   = Regular relationship
◈   = Identifying relationship (double diamond)
~~~  = Partial key (dashed underline)
```

---

### 4. 2-Marker Answer

**Q: What is a Weak Entity?**

> A Weak Entity is an entity that lacks a primary key and depends on an owner (strong) entity for identification. It is represented by a **double rectangle** in ER diagrams. It uses a **partial key (discriminator)** shown with a dashed underline. Example: DEPENDENT entity depends on EMPLOYEE entity.

---

### 5. 5-Marker Answer

**Q: Explain Weak Entity with diagram and example.**

> **Weak Entity** is an entity that:
> 1. Does not have a primary key of its own
> 2. Is existence-dependent on a strong entity called the **Owner Entity**
> 3. Is identified using a **Partial Key** (discriminator) combined with the owner's PK
> 4. Is connected to the owner via an **Identifying Relationship** (double diamond)
>
> **Example:** In a company database:
> - EMPLOYEE (Strong Entity) → PK = Emp_ID
> - DEPENDENT (Weak Entity) → Partial Key = Dep_Name (not unique alone)
>   - Full identity = Emp_ID + Dep_Name
>
> **ER Diagram:**
> ```
> ○ Emp_ID          ○~~Dep_Name~~   ○ Relationship
>     |                  |              |
> [EMPLOYEE]════<◈HAS_DEPENDENT>══[DEPENDENT]
> ```
>
> **Mapping to Tables:**
> - EMPLOYEE(Emp_ID, Emp_Name, Age)
> - DEPENDENT(**Emp_ID**, **Dep_Name**, DOB, Relationship)
>   - PK = (Emp_ID, Dep_Name)
>   - Emp_ID is FK referencing EMPLOYEE

---

### 6. Common Mistakes
- ❌ Forgetting double rectangle for weak entity
- ❌ Using single diamond instead of double diamond for identifying relationship
- ❌ Not combining partial key with owner PK when mapping to tables

### 7. Memory Trick
> **"Weak needs OWNER — Double rect, double diamond, dashed key"**

### 8. Expected Marks: 2 or 5 marker (very high probability!)

---

## 📌 TOPIC 5 : RECURSIVE RELATIONSHIP

### 1. Exam Definition
> A **Recursive Relationship** (also called **Unary Relationship**) is a relationship where an entity is related to **itself**. It occurs when instances of the same entity type are associated with each other.

---

### 2. Intuition
- An **EMPLOYEE** can **supervise** other **EMPLOYEES**
- One person is both the supervisor AND supervised → same entity, different roles

---

### 3. Diagram

```
           ○ Emp_ID
           |
    ┌──────┤
    │  [EMPLOYEE]──────<SUPERVISES>
    │      |                |
    └──────┘           (recursive)
    
More detailed:
                    Supervisor
                   /
[EMPLOYEE]──<SUPERVISES>──[EMPLOYEE]
                   \
                    Supervisee

Role Names on both ends:
[EMPLOYEE]──────────<SUPERVISES>
     │  (supervisor)         (supervisee)  │
     └────────────────────────────────────┘
```

**Cardinality:** 1:N (one supervisor has many supervisees)

---

### 4. Mapping to Table

```sql
-- Single entity table with self-referential FK
EMPLOYEE(Emp_ID, Emp_Name, Supervisor_ID)
-- Supervisor_ID is FK referencing Emp_ID in same table
-- Supervisor_ID can be NULL (if no supervisor)
```

| Emp_ID | Emp_Name | Supervisor_ID |
|--------|----------|---------------|
| E1 | Alice (CEO) | NULL |
| E2 | Bob | E1 |
| E3 | Carol | E1 |
| E4 | Dave | E2 |

---

### 5. PYQ Style Answer

**Q: What is a Recursive Relationship? Draw an ER diagram for "Employee supervises Employee".**

> A **Recursive Relationship** is a relationship type where an entity participates in a relationship with **itself**. It is also called a **Unary Relationship**.
>
> **Example:** EMPLOYEE supervises EMPLOYEE
> - Role 1: Supervisor (the "1" side)
> - Role 2: Supervisee (the "N" side)
> - Cardinality: 1:N (one employee supervises many)
>
> ER Diagram: [as shown above]
>
> **Table:**
> EMPLOYEE(Emp_ID PK, Emp_Name, Supervisor_ID FK → Emp_ID)

---

### 6. Common Mistakes
- ❌ Forgetting to label role names on both ends
- ❌ Not knowing that it maps to a self-referential FK

### 7. Memory Trick
> **"RECURSIVE = Same box, loop back, self-reference FK"**

### 8. Expected Marks: 3–5 marker

---

## 📌 TOPIC 6 : GENERALIZATION vs SPECIALIZATION

### 1. Comparison Table (Exam Gold!)

| Feature | Generalization | Specialization |
|---------|---------------|----------------|
| Direction | Bottom-Up | Top-Down |
| Process | Combine subclasses → superclass | Divide superclass → subclasses |
| Starting point | Lower-level entities | Higher-level entity |
| Example | CAR + TRUCK → VEHICLE | VEHICLE → CAR, TRUCK |
| Concept | Abstraction (finding common) | Refinement (finding specific) |
| ER notation | Uses ISA triangle | Uses ISA triangle |

---

### 2. Diagram

```
        [VEHICLE]          ← Superclass
            |
          <ISA>            ← ISA triangle
         /     \
      [CAR]   [TRUCK]      ← Subclasses

Generalization: CAR + TRUCK → VEHICLE (bottom-up)
Specialization: VEHICLE → CAR + TRUCK (top-down)
```

---

### 3. PYQ Answer

**Q: Differentiate between Generalization and Specialization.**

> **Specialization** is a **top-down** design process where a higher-level entity (superclass) is divided into lower-level entities (subclasses) based on distinguishing attributes.
> Example: PERSON → STUDENT, EMPLOYEE
>
> **Generalization** is a **bottom-up** process where common attributes of subclasses are combined to form a superclass.
> Example: STUDENT + EMPLOYEE → PERSON
>
> Both use the **ISA hierarchy** in ER diagrams.

### 4. Memory Trick
> **"Generalization = GENERAL goes UP (bottom-up), Specialization = SPECIAL goes DOWN (top-down)"**

### 5. Expected Marks: 3 marker (medium probability)

---

# ═══════════════════════════════════
# SECTION B : RELATIONAL MODEL
# ═══════════════════════════════════

---

## 📌 TOPIC 7 : INTEGRITY CONSTRAINTS

### 1. Exam Definition
> **Integrity Constraints** are rules that ensure accuracy, consistency, and validity of data in a relational database. There are four main types: Domain, Key, Entity Integrity, and Referential Integrity.

---

### 2. All Four Constraints

#### 2.1 Domain Constraint
> Each attribute value must belong to the **defined domain (data type and range)**.

```sql
-- Age must be between 0 and 150
Age INT CHECK (Age >= 0 AND Age <= 150)

-- Gender must be 'M' or 'F'
Gender CHAR(1) CHECK (Gender IN ('M', 'F'))
```

#### 2.2 Key Constraint
> Every relation must have a **primary key** — unique and not null. No two tuples can have the same PK value.

```sql
CREATE TABLE STUDENT (
    SID INT PRIMARY KEY,  -- Key Constraint
    SName VARCHAR(50)
);
```

#### 2.3 Entity Integrity Constraint
> **Primary Key** of a table must be **NOT NULL**. No primary key attribute can have a NULL value.

```sql
-- SID cannot be NULL
SID INT NOT NULL PRIMARY KEY
```

#### 2.4 Referential Integrity Constraint
> A **Foreign Key** in a table must either match an existing **Primary Key** in the referenced table, or be **NULL**. No dangling references allowed.

```sql
CREATE TABLE ENROLLMENT (
    SID INT,
    CID INT,
    FOREIGN KEY (SID) REFERENCES STUDENT(SID),  -- Referential Integrity
    FOREIGN KEY (CID) REFERENCES COURSE(CID)
);
```

---

### 3. 5-Marker Answer

**Q: Explain integrity constraints in RDBMS with examples.**

> Integrity constraints are rules that maintain data accuracy and consistency:
>
> 1. **Domain Constraint**: Values must belong to a defined domain. E.g., age must be numeric and positive.
>
> 2. **Key Constraint**: Primary key must be unique. No two students can have the same Roll No.
>
> 3. **Entity Integrity**: Primary key cannot be NULL. Every student must have a Roll No.
>
> 4. **Referential Integrity**: Foreign key value must exist in the referenced relation. A student cannot enroll in a course that doesn't exist.
>
> These constraints prevent insert/update/delete anomalies.

### 4. Common Mistakes
- ❌ Confusing Entity Integrity (PK not null) with Key Constraint (PK unique)
- ❌ Saying foreign key cannot be null (it CAN be null)

### 5. Memory Trick
> **"DKER"** = Domain, Key, Entity Integrity, Referential Integrity

### 6. Expected Marks: 5 marker

---

## 📌 TOPIC 8 : DDL COMMANDS

### 1. Exam Definition
> **DDL (Data Definition Language)** commands define the structure of the database. They deal with schema, not data. Changes are **auto-committed**.

---

### 2. All DDL Commands

#### CREATE
```sql
CREATE TABLE STUDENT (
    SID     INT          PRIMARY KEY,
    SName   VARCHAR(50)  NOT NULL,
    Age     INT          CHECK (Age > 0),
    Dept    VARCHAR(30)  DEFAULT 'CSE'
);
```

#### ALTER
```sql
-- Add a new column
ALTER TABLE STUDENT ADD Email VARCHAR(100);

-- Modify column data type
ALTER TABLE STUDENT MODIFY Age SMALLINT;

-- Drop a column
ALTER TABLE STUDENT DROP COLUMN Email;

-- Rename column
ALTER TABLE STUDENT RENAME COLUMN SName TO StudentName;
```

#### DROP
```sql
-- Remove entire table (structure + data)
DROP TABLE STUDENT;
```

#### TRUNCATE
```sql
-- Remove all data, keep structure
TRUNCATE TABLE STUDENT;
```

---

### 3. DDL vs DML Quick Comparison

| Command | Type | Deletes Structure? | Rollback? |
|---------|------|-------------------|-----------|
| DROP | DDL | Yes | No |
| TRUNCATE | DDL | No (only data) | No |
| DELETE | DML | No | Yes |

### 4. Memory Trick
> **"CAD-T"** = CREATE, ALTER, DROP, TRUNCATE

### 5. Expected Marks: 3–5 marker

---

## 📌 TOPIC 9 : DML COMMANDS

### 1. Exam Definition
> **DML (Data Manipulation Language)** commands are used to manipulate data within database tables. They are **NOT auto-committed** and can be rolled back.

---

### 2. All DML Commands

#### INSERT
```sql
-- Insert single row
INSERT INTO STUDENT (SID, SName, Age, Dept)
VALUES (101, 'Alice', 20, 'CSE');

-- Insert multiple rows
INSERT INTO STUDENT VALUES
(102, 'Bob', 21, 'ECE'),
(103, 'Carol', 19, 'MECH');
```

#### SELECT
```sql
-- Select all
SELECT * FROM STUDENT;

-- Select specific columns
SELECT SName, Age FROM STUDENT WHERE Dept = 'CSE';
```

#### UPDATE
```sql
-- Update specific rows
UPDATE STUDENT SET Age = 22 WHERE SID = 101;

-- Update multiple columns
UPDATE STUDENT SET Age = 22, Dept = 'IT' WHERE SID = 101;
```

#### DELETE
```sql
-- Delete specific rows
DELETE FROM STUDENT WHERE SID = 101;

-- Delete all rows (but structure remains)
DELETE FROM STUDENT;
```

### 3. Memory Trick
> **"SIUD"** = SELECT, INSERT, UPDATE, DELETE

### 4. Expected Marks: 3 marker

---

## 📌 TOPIC 10 : SQL QUERIES (PRACTICE SET)

### Setup: STUDENT Table

```sql
CREATE TABLE STUDENT (
    SID     INT PRIMARY KEY,
    SName   VARCHAR(50),
    Age     INT,
    Dept    VARCHAR(30),
    Marks   FLOAT,
    City    VARCHAR(30)
);

INSERT INTO STUDENT VALUES
(1, 'Alice',   20, 'CSE',  88.5, 'Delhi'),
(2, 'Bob',     21, 'ECE',  72.0, 'Mumbai'),
(3, 'Carol',   19, 'CSE',  91.0, 'Delhi'),
(4, 'Dave',    22, 'MECH', 65.0, 'Chennai'),
(5, 'Eve',     20, 'ECE',  79.5, 'Mumbai'),
(6, 'Frank',   21, 'CSE',  85.0, 'Delhi'),
(7, 'Grace',   22, 'IT',   93.0, 'Bangalore');
```

---

### 10 Exam-Ready Queries

**Q1: Get all CSE students**
```sql
SELECT * FROM STUDENT WHERE Dept = 'CSE';
```

**Q2: Get students with Marks > 80, sorted by Marks descending**
```sql
SELECT SName, Marks FROM STUDENT
WHERE Marks > 80
ORDER BY Marks DESC;
```

**Q3: Count students in each department**
```sql
SELECT Dept, COUNT(*) AS StudentCount
FROM STUDENT
GROUP BY Dept;
```

**Q4: Find average marks per department**
```sql
SELECT Dept, AVG(Marks) AS AvgMarks
FROM STUDENT
GROUP BY Dept;
```

**Q5: Find maximum and minimum marks**
```sql
SELECT MAX(Marks) AS HighestMarks, MIN(Marks) AS LowestMarks
FROM STUDENT;
```

**Q6: Get departments with more than 2 students**
```sql
SELECT Dept, COUNT(*) AS Count
FROM STUDENT
GROUP BY Dept
HAVING COUNT(*) > 2;
```

**Q7: Get students from Delhi OR Mumbai**
```sql
SELECT SName, City FROM STUDENT
WHERE City IN ('Delhi', 'Mumbai');
```

**Q8: Get students whose name starts with 'A'**
```sql
SELECT * FROM STUDENT WHERE SName LIKE 'A%';
```

**Q9: Get 2nd highest marks (using subquery)**
```sql
SELECT MAX(Marks) FROM STUDENT
WHERE Marks < (SELECT MAX(Marks) FROM STUDENT);
```

**Q10: Get students ordered by department, then by marks**
```sql
SELECT SName, Dept, Marks FROM STUDENT
ORDER BY Dept ASC, Marks DESC;
```

---

# ═══════════════════════════════════
# SECTION C : RELATIONAL ALGEBRA
# ═══════════════════════════════════

> **Relational Algebra** is a procedural query language that operates on relations (tables) and returns relations as results.

---

### Sample Relations

**STUDENT**
| SID | SName | Age | Dept |
|-----|-------|-----|------|
| 1 | Alice | 20 | CSE |
| 2 | Bob | 21 | ECE |
| 3 | Carol | 19 | CSE |
| 4 | Dave | 22 | MECH |

**COURSE**
| CID | CName | Dept |
|-----|-------|------|
| C1 | DBMS | CSE |
| C2 | OS | CSE |
| C3 | Circuits | ECE |

**ENROLLMENT**
| SID | CID | Grade |
|-----|-----|-------|
| 1 | C1 | A |
| 1 | C2 | B |
| 2 | C3 | A |
| 3 | C1 | A |

---

## Operation 1: SELECTION (σ)

**Definition:** Selects rows (tuples) satisfying a condition.

**Symbol:** σ (sigma)

**Syntax:** σ_condition(Relation)

```
σ_Dept='CSE'(STUDENT)
→ Returns: Alice, Carol (both CSE students)

Result:
| SID | SName | Age | Dept |
|-----|-------|-----|------|
| 1   | Alice | 20  | CSE  |
| 3   | Carol | 19  | CSE  |
```

---

## Operation 2: PROJECTION (π)

**Definition:** Selects specific columns from a relation.

**Symbol:** π (pi)

**Syntax:** π_attr1,attr2(Relation)

```
π_SName,Dept(STUDENT)
→ Returns only SName and Dept columns

Result:
| SName | Dept |
|-------|------|
| Alice | CSE  |
| Bob   | ECE  |
| Carol | CSE  |
| Dave  | MECH |
```

---

## Operation 3: UNION (∪)

**Definition:** Returns all tuples from both relations (no duplicates). Relations must be **union compatible** (same attributes).

**Symbol:** ∪

**Syntax:** R ∪ S

```
Suppose R = {Students in CSE}, S = {Students in ECE}
R ∪ S = All students in CSE or ECE (no duplicates)
```

**Union Compatible** = Same number of attributes, compatible domains.

---

## Operation 4: SET DIFFERENCE (−)

**Definition:** Returns tuples in R but NOT in S.

**Symbol:** −

**Syntax:** R − S

```
R − S = Tuples in R that are not in S

Students enrolled in C1 but NOT in C2:
π_SID(σ_CID='C1'(ENROLLMENT)) − π_SID(σ_CID='C2'(ENROLLMENT))
```

---

## Operation 5: CARTESIAN PRODUCT (×)

**Definition:** Returns all possible combinations of tuples from two relations.

**Symbol:** ×

**Syntax:** R × S

```
If R has 4 tuples and S has 3 tuples
R × S has 4 × 3 = 12 tuples

STUDENT × COURSE = Every student paired with every course
(not very useful alone, used before joins)
```

---

## Operation 6: NATURAL JOIN (⋈)

**Definition:** Joins two relations on their common attributes (equal values), removes duplicate columns.

**Symbol:** ⋈

**Syntax:** R ⋈ S

```
STUDENT ⋈ ENROLLMENT
→ Joins on SID (common attribute)

Result:
| SID | SName | Age | Dept | CID | Grade |
|-----|-------|-----|------|-----|-------|
| 1   | Alice | 20  | CSE  | C1  | A     |
| 1   | Alice | 20  | CSE  | C2  | B     |
| 2   | Bob   | 21  | ECE  | C3  | A     |
| 3   | Carol | 19  | CSE  | C1  | A     |
```

---

## Operation 7: THETA JOIN (θ-JOIN)

**Definition:** Joins two relations using a condition (theta condition). The condition can use any comparison operator (=, <, >, ≤, ≥, ≠).

**Symbol:** ⋈_θ

**Syntax:** R ⋈_(condition) S

```
STUDENT ⋈_(STUDENT.Dept = COURSE.Dept) COURSE
→ Join student with courses from the same department

If condition uses = only → called EQUI-JOIN
If equi-join removes duplicate → called NATURAL JOIN
```

---

## Operation 8: OUTER JOIN

**Definition:** Returns all tuples from one or both relations, even if no matching tuple exists in the other. Missing values are filled with NULL.

| Type | Returns |
|------|---------|
| **Left Outer Join** (⟕) | All from LEFT + matching from RIGHT |
| **Right Outer Join** (⟖) | All from RIGHT + matching from LEFT |
| **Full Outer Join** (⟗) | All from BOTH relations |

```
STUDENT ⟕ ENROLLMENT
→ All students, even if not enrolled in any course
→ Dave (not enrolled) → appears with NULL for CID, Grade
```

---

### 10 PYQ-Level Relational Algebra Problems

**Q1:** Find names of all CSE students.
```
π_SName(σ_Dept='CSE'(STUDENT))
Answer: {Alice, Carol}
```

**Q2:** Find SIDs of students scoring grade 'A'.
```
π_SID(σ_Grade='A'(ENROLLMENT))
Answer: {1, 2, 3}
```

**Q3:** Find names of students enrolled in course C1.
```
π_SName(σ_CID='C1'(STUDENT ⋈ ENROLLMENT))
Answer: {Alice, Carol}
```

**Q4:** Find students who are NOT enrolled in any course.
```
π_SID(STUDENT) − π_SID(ENROLLMENT)
Answer: {4} (Dave)
```

**Q5:** Find students older than 20.
```
σ_Age>20(STUDENT)
Answer: Bob (21), Dave (22)
```

**Q6:** Find all courses taken by Alice (SID=1).
```
π_CName(σ_SID=1(ENROLLMENT ⋈ COURSE))
Answer: {DBMS, OS}
```

**Q7:** Find departments with at least one student.
```
π_Dept(STUDENT)
Answer: {CSE, ECE, MECH}
```

**Q8:** Find students enrolled in both C1 and C2.
```
π_SID(σ_CID='C1'(ENROLLMENT)) ∩ π_SID(σ_CID='C2'(ENROLLMENT))
Answer: {1} (Alice)
```

**Q9:** Find names of students who got grade 'A' in DBMS.
```
π_SName(σ_Grade='A' ∧ CName='DBMS'(STUDENT ⋈ ENROLLMENT ⋈ COURSE))
Answer: {Alice, Carol}
```

**Q10:** Find all student-course pairs where student's department matches course's department.
```
STUDENT ⋈_(STUDENT.Dept = COURSE.Dept) COURSE
Answer: Alice-DBMS, Alice-OS, Carol-DBMS, Carol-OS, Bob-Circuits
```

---

# ═══════════════════════════════════
# SECTION D : ER → RELATIONAL MAPPING
# ═══════════════════════════════════

> **MOST IMPORTANT SECTION** — Appears in almost every exam!

---

## Rule 1: Strong Entity Mapping

**Rule:** Each strong entity becomes a table. Its attributes become columns. Key attribute becomes PK.

```
ER: [STUDENT] with attributes {SID, SName, Age, Dept}
         ↓
Table: STUDENT(SID, SName, Age, Dept)
       PK = SID
```

```sql
CREATE TABLE STUDENT (
    SID   INT PRIMARY KEY,
    SName VARCHAR(50),
    Age   INT,
    Dept  VARCHAR(30)
);
```

---

## Rule 2: Weak Entity Mapping

**Rule:** Weak entity table includes: its own partial key + PK of owner entity. PK = (Partial Key + Owner's PK). Add FK referencing owner.

```
ER: [EMPLOYEE] ◈── [DEPENDENT]
    PK=EmpID       Partial Key = DepName
         ↓
Tables:
EMPLOYEE(EmpID, EmpName, Age)
DEPENDENT(EmpID, DepName, Relationship, DOB)
-- PK = (EmpID, DepName)
-- EmpID is FK referencing EMPLOYEE
```

```sql
CREATE TABLE DEPENDENT (
    EmpID        INT,
    DepName      VARCHAR(50),
    Relationship VARCHAR(20),
    DOB          DATE,
    PRIMARY KEY (EmpID, DepName),
    FOREIGN KEY (EmpID) REFERENCES EMPLOYEE(EmpID)
);
```

---

## Rule 3: 1:1 Relationship Mapping

**Rule:** Two approaches:
- **Option A:** Add FK of one entity into the other (prefer total participation side)
- **Option B:** Merge into a single table (if same entity)

```
ER: [EMPLOYEE] ──1──<MANAGES>──1──[DEPARTMENT]
     PK=EmpID                      PK=DeptID
     (Total: every emp manages dept)

Option A: Add DeptID in EMPLOYEE table
EMPLOYEE(EmpID, EmpName, DeptID)
-- DeptID FK references DEPARTMENT

Option B (if total on both sides): Merge tables
EMPLOYEE_DEPT(EmpID, EmpName, DeptID, DeptName)
```

---

## Rule 4: 1:N Relationship Mapping

**Rule:** Add the PK of the "1-side" entity as a FK in the "N-side" table.

```
ER: [DEPARTMENT] ──1──<HAS>──N──[EMPLOYEE]
     PK=DeptID                   PK=EmpID

→ Add DeptID (FK) into EMPLOYEE table

DEPARTMENT(DeptID, DeptName, Location)
EMPLOYEE(EmpID, EmpName, Age, DeptID)
-- DeptID FK → DEPARTMENT.DeptID
```

```sql
CREATE TABLE EMPLOYEE (
    EmpID  INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Age    INT,
    DeptID INT,
    FOREIGN KEY (DeptID) REFERENCES DEPARTMENT(DeptID)
);
```

---

## Rule 5: M:N Relationship Mapping

**Rule:** Create a **new table** for the relationship. Include PKs of both entities as FKs. PK of new table = combination of both FKs.

```
ER: [STUDENT] ──M──<ENROLLS>──N──[COURSE]
     PK=SID    (Grade attr)       PK=CID

→ Create ENROLLS table

STUDENT(SID, SName, ...)
COURSE(CID, CName, ...)
ENROLLS(SID, CID, Grade)
-- PK = (SID, CID)
-- SID FK → STUDENT, CID FK → COURSE
```

```sql
CREATE TABLE ENROLLS (
    SID   INT,
    CID   VARCHAR(5),
    Grade CHAR(1),
    PRIMARY KEY (SID, CID),
    FOREIGN KEY (SID) REFERENCES STUDENT(SID),
    FOREIGN KEY (CID) REFERENCES COURSE(CID)
);
```

---

## Mapping Summary Table

| ER Component | Mapping Rule |
|-------------|-------------|
| Strong Entity | → One table, PK = Key Attribute |
| Weak Entity | → Table with Partial Key + Owner PK as composite PK |
| 1:1 Relationship | → FK in one table (prefer total participation side) |
| 1:N Relationship | → FK of 1-side in N-side table |
| M:N Relationship | → New junction table with composite PK |
| Multivalued Attribute | → New table (Entity PK + Attribute value) |
| Composite Attribute | → Include individual components, not composite itself |
| Derived Attribute | → Usually NOT stored in table |

---

## Complete PYQ Style Question

**Q: Convert the following ER diagram to relational tables:**

```
Hospital ER:
- PATIENT (PID, PName, Age, Disease)
- DOCTOR (DID, DName, Specialization)
- WARD (WID, WName, Capacity)
- PATIENT treats with DOCTOR (M:N, with Date attribute)
- PATIENT admitted in WARD (M:1)
```

**Solution:**

```
PATIENT(PID, PName, Age, Disease, WID)
-- WID FK → WARD (for M:1 relationship, add FK in PATIENT)

DOCTOR(DID, DName, Specialization)

WARD(WID, WName, Capacity)

TREATS(PID, DID, Date)
-- PK = (PID, DID)
-- PID FK → PATIENT, DID FK → DOCTOR
-- (New table for M:N relationship)
```

---

# ═══════════════════════════════════
# SECTION E : FUNCTIONAL DEPENDENCY
# ═══════════════════════════════════

---

### 1. Exam Definition
> A **Functional Dependency (FD)** X → Y means: for every tuple in the relation, if two tuples have the same value of X, they must have the same value of Y. X is called the **determinant** and Y is the **dependent**.

---

### 2. Intuition
- If you know **Roll Number**, you can determine **Student Name** → RollNo → SName
- If you know **Course ID**, you can determine **Course Name** → CID → CName
- Roll Number "determines" Name

---

### 3. Types of Functional Dependencies

#### Trivial FD
> X → Y is **trivial** if Y ⊆ X (Y is a subset of X)
```
{SID, SName} → SID   (trivial, because SID is already in LHS)
SID → SID             (trivial)
```

#### Non-Trivial FD
> X → Y is **non-trivial** if Y ⊄ X
```
SID → SName           (non-trivial: SName not a subset of SID)
```

#### Fully Functional Dependency
> X → Y is **fully functional** if removing ANY attribute from X makes the FD invalid. (Y depends on the WHOLE of X, not a part of it.)
```
(SID, CID) → Grade    (fully functional: neither SID alone nor CID alone determines Grade)
```

#### Partial Dependency
> X → Y is a **partial dependency** if Y can be determined by a PROPER SUBSET of X.
```
(SID, CID) → SName    (partial: SID alone → SName, so SName partially depends on composite key)
```
⚠️ **Partial dependency causes 2NF violation!**

#### Transitive Dependency
> X → Y → Z means Z **transitively depends** on X (via Y), where X is not a proper subset of Y.
```
SID → DeptID → DeptName
(SName transitively depends on SID through DeptID)
```
⚠️ **Transitive dependency causes 3NF violation!**

---

### 4. Inference Rules (Armstrong's Axioms)

| Rule | Statement |
|------|-----------|
| **Reflexivity** | If Y ⊆ X, then X → Y |
| **Augmentation** | If X → Y, then XZ → YZ |
| **Transitivity** | If X → Y and Y → Z, then X → Z |

---

### 5. Practice Problems on FD

Given: STUDENT_COURSE(SID, CID, SName, CName, Faculty, Grade)

**Identify FDs:**
- SID → SName
- CID → CName
- CID → Faculty
- (SID, CID) → Grade

**Q1:** Is (SID, CID) → SName a full or partial FD?
> **Partial** — because SID alone → SName

**Q2:** Is (SID, CID) → Grade a full or partial FD?
> **Fully Functional** — neither SID nor CID alone determines Grade

**Q3:** If SID → DeptID and DeptID → HOD, is HOD transitively dependent on SID?
> **Yes** — SID → DeptID → HOD (transitive dependency)

**Q4:** Is {SID, CID} → SID a trivial or non-trivial FD?
> **Trivial** — SID ⊆ {SID, CID}

**Q5:** From {A → B, B → C}, can we derive A → C?
> **Yes** — by transitivity axiom

**Q6:** Given A → B, is AB → B trivial?
> **Yes** — B ⊆ AB

**Q7:** If FDs are: EmpID → Name, EmpID → DeptID, DeptID → DeptName. Find all FDs derivable from EmpID.
> EmpID → Name, EmpID → DeptID, EmpID → DeptName (via transitivity)

**Q8:** R(A,B,C,D) with FDs: A→B, B→C, A→D. What is the closure of A (A+)?
> A+ = {A, B, C, D} — A determines everything → A is a candidate key

**Q9:** Is A→BC same as A→B and A→C?
> **Yes** — Union rule: X→Y and X→Z implies X→YZ

**Q10:** Given (SID,CID)→Grade, (SID,CID)→SName, and SID→SName. Is (SID,CID)→SName partial or full?
> **Partial** — SName can be determined by SID alone

---

### 15 More FD Practice Questions

**Q11:** R(P,Q,R,S) FDs: P→Q, Q→R, R→S. Find P+.
> P+ = {P, Q, R, S}

**Q12:** Is PQ→R a partial dependency if P→R exists?
> Yes, partial. R depends on P alone (proper subset of PQ).

**Q13:** Can a prime attribute (part of candidate key) have partial dependency?
> By definition, partial dependency is from a NON-prime attribute on a proper subset of candidate key. Prime attributes can't have partial deps (by definition).

**Q14:** EMPLOYEE(EmpID, ProjID, Hours, EmpName, ProjName). Key=(EmpID, ProjID). FDs: EmpID→EmpName, ProjID→ProjName, (EmpID,ProjID)→Hours. Which are partial dependencies?
> EmpID→EmpName (partial), ProjID→ProjName (partial). Hours is fully dependent.

**Q15:** What is a superkey?
> A set of attributes that uniquely identifies every tuple. If X+ = all attributes, X is a superkey.

---

# ═══════════════════════════════════
# SECTION F : NORMALIZATION
# ═══════════════════════════════════

---

### Why Normalize?

Consider this unnormalized table:

**STUDENT_COURSE (SID, SName, CID, CName, Faculty, Grade)**

| SID | SName | CID | CName | Faculty | Grade |
|-----|-------|-----|-------|---------|-------|
| 1 | Alice | C1 | DBMS | Dr. Roy | A |
| 1 | Alice | C2 | OS | Dr. Sen | B |
| 2 | Bob | C1 | DBMS | Dr. Roy | B |

**Problems:**

| Anomaly | Example |
|---------|---------|
| **Redundancy** | "Alice" and "DBMS" stored multiple times |
| **Update Anomaly** | Change DBMS faculty → must update multiple rows. Risk of inconsistency. |
| **Insertion Anomaly** | Can't add a new course without a student enrolled |
| **Deletion Anomaly** | Delete Bob → lose information about C1/DBMS |

---

## FIRST NORMAL FORM (1NF)

### 1. Exam Definition
> A relation is in **1NF** if:
> 1. All attribute values are **atomic** (indivisible)
> 2. Each cell contains only a **single value**
> 3. All rows are **unique** (has a primary key)
> 4. No **repeating groups** or multi-valued attributes

---

### 2. 1NF Violation Example

**NOT in 1NF (multivalued attribute):**

| SID | SName | Phone |
|-----|-------|-------|
| 1 | Alice | 9876, 5432 |
| 2 | Bob | 1234 |

Alice has two phone numbers in one cell → **violates atomicity**

---

### 3. Convert to 1NF

**Method 1: Separate rows**

| SID | SName | Phone |
|-----|-------|-------|
| 1 | Alice | 9876 |
| 1 | Alice | 5432 |
| 2 | Bob | 1234 |

Now PK = (SID, Phone)

**Method 2: Separate table**

| SID | SName |
|-----|-------|
| 1 | Alice |
| 2 | Bob |

| SID | Phone |
|-----|-------|
| 1 | 9876 |
| 1 | 5432 |
| 2 | 1234 |

---

### 4. Another 1NF Example

**NOT in 1NF:**
| OrderID | Items |
|---------|-------|
| O1 | Pen, Book, Eraser |

**In 1NF:**
| OrderID | Item |
|---------|------|
| O1 | Pen |
| O1 | Book |
| O1 | Eraser |

---

### 5. PYQ Answer

**Q: What is 1NF? Convert the following table to 1NF:**

> **1NF Definition:** A relation is in First Normal Form if every attribute contains only atomic (indivisible) values with no repeating groups.
>
> **Conversion:** Separate multi-valued attributes into individual rows, ensure each cell has a single value.

### 6. Memory Trick
> **"1NF = ONE value per cell"**

### 7. Expected Marks: 3–5 marker

---

## SECOND NORMAL FORM (2NF)

### 1. Exam Definition
> A relation is in **2NF** if:
> 1. It is in **1NF**
> 2. Every **non-prime attribute** is **fully functionally dependent** on the **entire primary key** (no partial dependencies)

**Non-prime attribute** = Attribute NOT part of any candidate key

---

### 2. 2NF Violation Example

**Relation:** ENROLLMENT(SID, CID, SName, CName, Grade)
**Primary Key:** (SID, CID)
**FDs:**
- SID → SName ← **PARTIAL** dependency!
- CID → CName ← **PARTIAL** dependency!
- (SID, CID) → Grade ← Fully functional ✓

SName depends on only SID (part of PK) → **partial dependency → 2NF violation!**

---

### 3. Convert to 2NF: Step-by-Step

**Step 1:** Identify partial dependencies
```
SID → SName        (partial)
CID → CName        (partial)
(SID, CID) → Grade (full) ✓
```

**Step 2:** Create separate tables for each partial dependency
- Take the partial determinant as PK of new table
- Remove the dependent from original table

**Step 3:** Result

```
STUDENT(SID, SName)         ← PK = SID
COURSE(CID, CName)          ← PK = CID
ENROLLMENT(SID, CID, Grade) ← PK = (SID, CID)
```

No more partial dependencies → **In 2NF!**

---

### 4. PYQ Solved: STUDENT Relation

**Q: Normalize STUDENT(SID, SNAME, COURSEID, COURSENAME, FACULTY) to 2NF.**

**Given FDs:**
- SID → SNAME
- COURSEID → COURSENAME, FACULTY

**Step 1: Identify PK**
Candidate Key = (SID, COURSEID) [needed to uniquely identify each enrollment]

**Step 2: Identify Partial Dependencies**
- SID → SNAME → **PARTIAL** (SID is only part of composite PK)
- COURSEID → COURSENAME → **PARTIAL**
- COURSEID → FACULTY → **PARTIAL**

**Step 3: Decompose**

```
STUDENT(SID, SNAME)
-- PK = SID

COURSE(COURSEID, COURSENAME, FACULTY)
-- PK = COURSEID

STUDENT_COURSE(SID, COURSEID)
-- PK = (SID, COURSEID)
-- FK: SID → STUDENT, COURSEID → COURSE
```

**Verification: Check 2NF**
- STUDENT: Only SID as PK → single attribute PK → can't have partial dep → ✓ 2NF
- COURSE: Only COURSEID as PK → ✓ 2NF
- STUDENT_COURSE: Only (SID,COURSEID) as PK, no other attributes → ✓ 2NF

---

### 5. Quick Reference: Normal Forms

| NF | Condition |
|----|-----------|
| **1NF** | Atomic values, no repeating groups |
| **2NF** | 1NF + No Partial Dependencies |
| **3NF** | 2NF + No Transitive Dependencies |
| **BCNF** | For every FD X→Y, X must be a superkey |

---

### 6. Memory Trick
> **"2NF = Full dependency on FULL key"**
> **"Partial = BAD in 2NF"**

### 7. Expected Marks: 5 marker (VERY HIGH PROBABILITY!)

---

# ═══════════════════════════════════
# SECTION G : ULTIMATE 5-PAGE REVISION SHEET
# ═══════════════════════════════════

---

## PAGE 1: ER DIAGRAM QUICK REFERENCE

```
SYMBOLS:
□  = Strong Entity
══ = Weak Entity (double rect)
○  = Attribute
──○ = Simple Attribute
○══ = Multivalued Attribute (double oval)
--○ = Derived Attribute (dashed oval)
○_ = Key Attribute (underlined)
○~~= Partial Key (dashed underline)
◇  = Relationship
◈  = Identifying Relationship (double diamond)
── = Partial Participation
══ = Total Participation (double line)

CARDINALITY:
1:1 ── [E1] ──1──◇──1──[E2] → FK in either
1:N ── [E1] ──1──◇──N──[E2] → FK in N side
M:N ── [E1] ──M──◇──N──[E2] → New table

WEAK ENTITY RULE:
Table PK = (Partial Key + Owner's PK)

RECURSIVE RELATIONSHIP:
[EMPLOYEE]──<SUPERVISES>── (self)
Maps to: EmpID, Name, Supervisor_ID (FK → EmpID)
```

---

## PAGE 2: RELATIONAL ALGEBRA CHEAT SHEET

```
OPERATION    SYMBOL    USE
─────────────────────────────────────────────
Selection    σ         Filter ROWS
Projection   π         Select COLUMNS
Union        ∪         All tuples from R or S
Difference   −         Tuples in R not in S
Intersection ∩         Tuples in both R and S
Cartesian    ×         All combinations
Natural Join ⋈         Join on common attributes
Theta Join   ⋈_θ       Join with any condition
Left Outer   ⟕         All of left + matching right
Right Outer  ⟖         All of right + matching left
Full Outer   ⟗         All from both sides

KEY EXPRESSIONS:
σ_cond(R)            = SELECT rows where condition
π_a,b(R)             = SELECT columns a,b
R ⋈ S                = JOIN on common attr
σ_A=x(π_a,b(R))     = Nested operations (innermost first)
```

---

## PAGE 3: NORMALIZATION QUICK GUIDE

```
FUNCTIONAL DEPENDENCY (FD): X → Y
"X determines Y"

TYPES:
Trivial FD    : Y ⊆ X         (A → A)
Non-Trivial   : Y ⊄ X         (SID → SName)
Partial FD    : Subset of PK → non-prime attr
Transitive FD : X → Y → Z (via non-key Y)

NORMALIZATION STEPS:
1NF: All values atomic, no repeating groups
     → Separate multi-valued into rows/table

2NF: In 1NF + No Partial Dependencies
     → Move partial deps to separate table
     → Each non-prime attr fully depends on full PK

ANOMALIES (reason to normalize):
Update Anomaly  → Change data in multiple places
Insert Anomaly  → Can't insert without unrelated data
Delete Anomaly  → Delete loses other information

PYQ Decomposition:
GIVEN: R(A, B, C, D) with PK=(A,B), FDs: A→C, B→D, AB→...
Step 1: Find partial deps (A→C, B→D are partial)
Step 2: Create R1(A,C), R2(B,D), R3(A,B,...fully dependent attrs)
```

---

## PAGE 4: SQL COMMANDS QUICK REFERENCE

```sql
-- DDL (Auto-committed, can't rollback)
CREATE TABLE T (col1 TYPE constraint, col2 TYPE ...);
ALTER TABLE T ADD col TYPE;
ALTER TABLE T MODIFY col TYPE;
ALTER TABLE T DROP COLUMN col;
DROP TABLE T;          -- deletes structure + data
TRUNCATE TABLE T;      -- deletes all data, keeps structure

-- DML (Can rollback)
INSERT INTO T (col1,col2) VALUES (v1, v2);
UPDATE T SET col=val WHERE condition;
DELETE FROM T WHERE condition;
SELECT col FROM T WHERE cond GROUP BY g HAVING h ORDER BY o;

-- CONSTRAINTS
PRIMARY KEY       → Unique + Not Null
FOREIGN KEY       → References PK of another table
UNIQUE            → No duplicates (can be null)
NOT NULL          → Cannot be null
CHECK             → Conditional constraint
DEFAULT           → Default value if none given

-- AGGREGATE FUNCTIONS
COUNT(*), SUM(col), AVG(col), MAX(col), MIN(col)

-- CLAUSES ORDER (must follow this order!):
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
```

---

## PAGE 5: KEY DEFINITIONS & INTEGRITY CONSTRAINTS

```
ENTITY: Real-world object with independent existence
ATTRIBUTE: Property of an entity
WEAK ENTITY: No PK of own, depends on strong entity
PARTIAL KEY: Attribute that identifies weak entity within owner
RECURSIVE: Entity related to itself (unary relationship)
GENERALIZATION: Bottom-up (subclasses → superclass)
SPECIALIZATION: Top-down (superclass → subclasses)

INTEGRITY CONSTRAINTS:
Domain     → Values in correct domain/range
Key        → PK must be unique
Entity     → PK cannot be NULL
Referential → FK must match existing PK or be NULL

MAPPING RULES:
Strong Entity → Table (PK = key attribute)
Weak Entity  → Table (PK = owner PK + partial key)
1:1 Rel      → FK in total participation side
1:N Rel      → FK on N-side
M:N Rel      → New junction table (PK = both FKs)
Multivalued  → New table (entity PK + attribute)
Derived Attr → NOT stored (calculated when needed)

RELATIONAL ALGEBRA PRIORITY:
1. Innermost operation first
2. σ before ×  (reduces size)
3. π to reduce columns
4. Then join/union
```

---

# ═══════════════════════════════════
# SECTION H : FINAL EXAM PREP
# ═══════════════════════════════════

---

## 🎯 PREDICTED QUESTIONS FOR TOMORROW

### VERY HIGH PROBABILITY (attempt all)
1. Draw an ER diagram for [Library / Hospital / University / Banking System]
2. Explain Weak Entity with diagram and example
3. What is Recursive Relationship? Draw ER for "Employee supervises Employee"
4. Explain Participation Constraints (Total and Partial)
5. Normalize STUDENT(SID, SName, CID, CName, Faculty) to 2NF
6. Explain Functional Dependency with types (Partial, Transitive)
7. Map M:N ER relationship to relational tables
8. Write relational algebra for given queries
9. Explain integrity constraints (all 4) with SQL examples
10. Convert given ER diagram to relational schema

### MEDIUM PROBABILITY
11. Generalization vs Specialization comparison
12. DDL + DML commands with examples
13. SQL queries with GROUP BY, HAVING, ORDER BY

---

## 📊 TOP 10 MOST IMPORTANT DEFINITIONS

| # | Term | One-Line Definition |
|---|------|---------------------|
| 1 | Weak Entity | Entity with no PK of own, depends on strong entity |
| 2 | Partial Key | Discriminator that identifies weak entity within owner |
| 3 | Functional Dependency | X→Y: same X values always give same Y values |
| 4 | Partial Dependency | Non-prime attr depends on PART of composite PK |
| 5 | Transitive Dependency | X→Y→Z where Y is non-prime (Z depends on X via Y) |
| 6 | 1NF | All attribute values are atomic (single-valued) |
| 7 | 2NF | 1NF + No partial dependencies on composite PK |
| 8 | Referential Integrity | FK must match existing PK or be NULL |
| 9 | Total Participation | Every entity MUST participate in relationship |
| 10 | Recursive Relationship | An entity type related to itself (unary) |

---

## 📐 TOP 10 MOST IMPORTANT DIAGRAMS

### 1. ER Diagram Components
```
○ (attr)  □ (entity)  ◇ (relation)
○══(multival)  --○(derived)  ○_(key)
══(total part)  ──(partial part)
```

### 2. Weak Entity
```
[EMPLOYEE]════<◈HAS>══[DEPENDENT]
              Identifying  (double rect)
```

### 3. Recursive Relationship
```
[EMPLOYEE]──<SUPERVISES>──(same EMPLOYEE)
     └──────── self-loop ────────┘
```

### 4. 1:N Mapping
```
[DEPT] ──1──<HAS>──N──[EMPLOYEE]
→ Add DeptID (FK) into EMPLOYEE table
```

### 5. M:N Mapping
```
[STUDENT] ──M──<ENROLLS>──N──[COURSE]
→ New table: ENROLLS(SID, CID, Grade)
```

### 6. Participation Constraints
```
[EMP]════<WORKS_FOR>──[DEPT]
  Total                 Partial
```

### 7. Generalization/Specialization
```
     [PERSON]          ← Superclass
         |
       <ISA>
      /     \
[STUDENT] [EMPLOYEE]   ← Subclasses
```

### 8. Normalization (1NF Violation)
```
BEFORE: | Phone: 9876, 5432 |  ← NOT atomic
AFTER:  | Phone: 9876 |        ← Atomic (1NF)
        | Phone: 5432 |
```

### 9. 2NF Decomposition
```
BEFORE: ENROLL(SID, CID, SName, CName, Grade)
        SID → SName (PARTIAL!)
        CID → CName (PARTIAL!)

AFTER:  STUDENT(SID, SName)
        COURSE(CID, CName)
        ENROLL(SID, CID, Grade) ← Only full FDs
```

### 10. Relational Algebra Pipeline
```
σ_cond → π_attrs → ⋈ (join) → final result
Filter rows → Select columns → Join tables
```

---

## 🧮 TOP 10 MOST IMPORTANT SQL QUERIES

```sql
-- Q1: Basic select with condition
SELECT * FROM STUDENT WHERE Dept = 'CSE';

-- Q2: Order by marks descending
SELECT SName, Marks FROM STUDENT ORDER BY Marks DESC;

-- Q3: Count per group
SELECT Dept, COUNT(*) FROM STUDENT GROUP BY Dept;

-- Q4: Average per group
SELECT Dept, AVG(Marks) FROM STUDENT GROUP BY Dept;

-- Q5: Filter groups with HAVING
SELECT Dept, COUNT(*) FROM STUDENT GROUP BY Dept HAVING COUNT(*) > 2;

-- Q6: Maximum and minimum
SELECT MAX(Marks) AS Max, MIN(Marks) AS Min FROM STUDENT;

-- Q7: LIKE pattern
SELECT * FROM STUDENT WHERE SName LIKE 'A%';

-- Q8: IN clause
SELECT * FROM STUDENT WHERE City IN ('Delhi', 'Mumbai');

-- Q9: Create table with constraints
CREATE TABLE STUDENT (
  SID INT PRIMARY KEY,
  SName VARCHAR(50) NOT NULL,
  Age INT CHECK(Age > 0)
);

-- Q10: Foreign key reference
CREATE TABLE ENROLLMENT (
  SID INT, CID INT,
  PRIMARY KEY(SID, CID),
  FOREIGN KEY(SID) REFERENCES STUDENT(SID)
);
```

---

## ∑ TOP 10 MOST IMPORTANT RELATIONAL ALGEBRA EXPRESSIONS

```
1. Select CSE students:
   σ_Dept='CSE'(STUDENT)

2. Get only names and departments:
   π_SName,Dept(STUDENT)

3. CSE students' names (combined):
   π_SName(σ_Dept='CSE'(STUDENT))

4. Students enrolled in course C1:
   π_SName(σ_CID='C1'(STUDENT ⋈ ENROLLMENT))

5. Students NOT enrolled in any course:
   π_SID(STUDENT) − π_SID(ENROLLMENT)

6. Students enrolled in both C1 and C2:
   π_SID(σ_CID='C1'(ENROLLMENT)) ∩ π_SID(σ_CID='C2'(ENROLLMENT))

7. Natural join of STUDENT and ENROLLMENT:
   STUDENT ⋈ ENROLLMENT

8. Theta join (students and courses, same dept):
   STUDENT ⋈_(STUDENT.Dept=COURSE.Dept) COURSE

9. All students with their courses (left outer join):
   STUDENT ⟕ ENROLLMENT

10. Students who got 'A' grade in DBMS:
    π_SName(σ_Grade='A' ∧ CName='DBMS'(STUDENT ⋈ ENROLLMENT ⋈ COURSE))
```

---

## 📝 25-MARK MOCK TEST

**Total: 25 Marks | Time: 1.5 Hours**

---

**Q1. (5 marks)** Draw a complete ER diagram for a **Library Management System** with the following requirements:
- Library has Books and Members
- Members borrow Books (M:N relationship, with BorrowDate and ReturnDate)
- Each Book has ISBN, Title, Author
- Book has many Copies (Weak Entity — CopyID as partial key)
- Each Member has MemberID, Name, PhoneNumbers (multivalued)

---

**Q2. (5 marks)** Consider the following relation:

```
ORDERITEM(OrderID, ProductID, CustomerID, CustomerName, ProductName, Quantity, Price)

FDs:
OrderID → CustomerID
CustomerID → CustomerName
ProductID → ProductName, Price
(OrderID, ProductID) → Quantity
```

a) Identify the primary key.
b) Identify all partial dependencies.
c) Normalize to 2NF showing all decomposed tables.

---

**Q3. (5 marks)** Explain with examples:
a) Weak Entity and Identifying Relationship (with ER diagram)
b) Total vs Partial Participation
c) Map the Weak Entity relationship to relational tables

---

**Q4. (5 marks)** Given relations:

```
EMPLOYEE(EmpID, EmpName, DeptID, Salary)
DEPARTMENT(DeptID, DeptName, Location)
```

Write relational algebra for:
a) Find names of employees in 'IT' department
b) Find employees with salary > 50000
c) Find all employees and their department names
d) Find employees NOT in any department
e) Find department names where at least one employee works

---

**Q5. (5 marks)** Answer the following:
a) Define Functional Dependency. Give example.
b) What is the difference between Trivial and Non-Trivial FD?
c) Explain Partial Dependency with example.
d) What is Transitive Dependency?
e) What anomalies does normalization solve? Give one example of each.

---

## ✅ COMPLETE SOLUTIONS TO MOCK TEST

---

### Q1 Solution (Library ER Diagram)

```
LIBRARY ER DIAGRAM:

○ MemberID (key)              ○~~CopyID~~ (partial key)
|                              |
○ MName                       ○ Condition
|
○══ PhoneNumbers              [BOOKCOPY]══════<◈IS_COPY_OF>═══[BOOK]
|                                                              |
[MEMBER]══════════<BORROWS>══════════════════════             ○ ISBN (key)
                      |         M          N                  |
              ○ BorrowDate                                    ○ Title
              ○ ReturnDate                                    |
                                                              ○ Author
```

**Tables:**
```
MEMBER(MemberID, MName)
MEMBER_PHONE(MemberID, PhoneNo)   ← Multivalued attribute
BOOK(ISBN, Title, Author)
BOOKCOPY(ISBN, CopyID, Condition) ← PK = (ISBN, CopyID)
BORROWS(MemberID, CopyID, ISBN, BorrowDate, ReturnDate)
```

---

### Q2 Solution (2NF Normalization)

**Primary Key:** (OrderID, ProductID)

**Partial Dependencies:**
- OrderID → CustomerID (partial)
- CustomerID → CustomerName (transitive via CustomerID, also partial via OrderID)
- ProductID → ProductName (partial)
- ProductID → Price (partial)
- (OrderID, ProductID) → Quantity ✓ fully functional

**Decomposed 2NF Tables:**

```
CUSTOMER(CustomerID, CustomerName)
-- PK = CustomerID

ORDER(OrderID, CustomerID)
-- PK = OrderID
-- FK: CustomerID → CUSTOMER

PRODUCT(ProductID, ProductName, Price)
-- PK = ProductID

ORDERITEM(OrderID, ProductID, Quantity)
-- PK = (OrderID, ProductID)
-- FK: OrderID → ORDER, ProductID → PRODUCT
```

---

### Q3 Solution (Weak Entity + Participation)

**a) Weak Entity Example: DEPENDENT of EMPLOYEE**
```
Weak Entity: DEPENDENT
Owner Entity: EMPLOYEE
Partial Key: Dep_Name
Identifying Relationship: HAS_DEPENDENT

ER Diagram:
○ EmpID           ○~~DepName~~    ○ Relationship
    |                  |              |
[EMPLOYEE]══<◈HAS_DEPENDENT>══[DEPENDENT]

Features:
- Double rectangle for DEPENDENT
- Double diamond for HAS_DEPENDENT
- Dashed underline for DepName
```

**b) Total vs Partial Participation:**
```
[EMPLOYEE]════<WORKS_IN>──[DEPARTMENT]
    Total                   Partial

Total: Every employee MUST work in a department
Partial: Department may exist without employees (e.g., new dept)
```

**c) Table Mapping:**
```
EMPLOYEE(EmpID, EmpName, Age, DeptID)
-- DeptID FK → DEPARTMENT (for WORKS_IN relationship)

DEPARTMENT(DeptID, DeptName, Location)

DEPENDENT(EmpID, DepName, Relationship, DOB)
-- PK = (EmpID, DepName)
-- EmpID FK → EMPLOYEE (ON DELETE CASCADE)
```

---

### Q4 Solution (Relational Algebra)

**a) Employees in IT department:**
```
π_EmpName(σ_DeptName='IT'(EMPLOYEE ⋈ DEPARTMENT))
```

**b) Employees with salary > 50000:**
```
σ_Salary>50000(EMPLOYEE)
```

**c) Employees with department names:**
```
π_EmpName,DeptName(EMPLOYEE ⋈ DEPARTMENT)
```

**d) Employees NOT in any department:**
```
π_EmpID(EMPLOYEE) − π_EmpID(σ_DeptID IS NOT NULL(EMPLOYEE))
-- OR: Employees where DeptID is NULL
σ_DeptID=NULL(EMPLOYEE)
```

**e) Department names with at least one employee:**
```
π_DeptName(DEPARTMENT ⋈ EMPLOYEE)
```

---

### Q5 Solution (FD Concepts)

**a) Functional Dependency:**
> X → Y means: if two tuples have same X, they have same Y.
> Example: SID → SName (if two students have same ID, they have same name)

**b) Trivial vs Non-Trivial:**
> Trivial: Y ⊆ X. Example: {SID, SName} → SID
> Non-Trivial: Y ⊄ X. Example: SID → SName (SName not in {SID})

**c) Partial Dependency:**
> Non-prime attribute depends on PART of composite PK.
> Example: PK=(SID, CID), FD: SID→SName. SName depends only on SID (part of PK) → Partial!

**d) Transitive Dependency:**
> X → Y → Z where Y is not a candidate key.
> Example: EmpID → DeptID → DeptName. DeptName transitively depends on EmpID via DeptID.

**e) Anomalies solved:**
> - **Update Anomaly**: Change Dr. Roy to Dr. Kumar → must update all rows with Dr. Roy.
> - **Insertion Anomaly**: Can't add Course without a Student to enroll.
> - **Deletion Anomaly**: Delete last student in CS101 → lose all CS101 course info.

---

## 🎓 EXPECTED SCORE ANALYSIS

| Question | Topic | Marks | Difficulty | Your Expected Score |
|----------|-------|-------|------------|---------------------|
| Q1 | ER Diagram | 5 | Medium | 4/5 |
| Q2 | 2NF Normalization | 5 | Medium-High | 4/5 |
| Q3 | Weak Entity | 5 | Medium | 4/5 |
| Q4 | Relational Algebra | 5 | Medium | 4/5 |
| Q5 | FD + Anomalies | 5 | Easy-Medium | 5/5 |
| **TOTAL** | | **25** | | **21/25** |

---

## ⚡ LAST 30-MINUTE REVISION CHECKLIST

```
□ ER Diagram Symbols (7 symbols)
□ Cardinality Mapping Rules (1:1, 1:N, M:N)
□ Weak Entity (double rect + double diamond + partial key)
□ Recursive Relationship (self-referential FK)
□ Total vs Partial Participation (double/single line)
□ Integrity Constraints (DKER)
□ DDL: CREATE, ALTER, DROP, TRUNCATE
□ DML: SELECT, INSERT, UPDATE, DELETE
□ Relational Algebra: σ, π, ∪, −, ×, ⋈
□ FD Types: Trivial, Non-trivial, Partial, Transitive
□ 1NF: Atomic values, no repeating groups
□ 2NF: No partial dependencies
□ Mapping Rules: Strong → Table, Weak → Composite PK, M:N → Junction
```

---

> **ALL THE BEST FOR YOUR EXAM! 🎯**
> 
> **Target: 20+/25 | Strategy: Attempt full questions, show all steps, draw neat diagrams**
> 
> Remember: Even partial credit counts — write whatever you know!

---

*Guide Created: Database Modelling Midsem Crash Prep*
*Coverage: Module I + Module III (1NF, 2NF)*
*Estimated Prep Time: 3-4 hours | Revision Time: 30 minutes*
