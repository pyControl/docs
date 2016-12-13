# pyControlGUI Test Cases

## Session

Below, we describe test cases for: 

* ???
* ???

### Resume table

| Test name | Date | Result | Comments |
|---|---|---|---|
| 1. Create, modify and save project | --- | --- | ---
| 1.1 Create project
| 1.2 Add experiments
| 1.3 Add subjects
| 1.4 Add and import task
| 1.5 Add experimental setup
| 1.6 Quit project

### 1. Create, modify and save project

**Scenario type:** Success

**Preconditions:** 

* Create a folder in your desktop called "test\_case\_project"

#### 1.1 Create project

1. Start application
2. Select ***File > New project***
3. Insert project name: ***My project***
4. Select project location: ***Desktop\test\_case\_project***

**What to expect:**

* Created folder structure with settings file:

```
My project
   | data
   | frameworks
   | tasks
   | settings.json
```

