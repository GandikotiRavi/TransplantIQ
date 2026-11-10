# TransplantIQ – Agentic AI-Powered Organ Transplant Coordination System

**Smarter Organ Coordination. Explainable AI. Human-Led Decisions.**

TransplantIQ is an Agentic AI-powered Organ Transplant Coordination and Clinical Decision Support System designed to support the organ transplantation process through intelligent clinical matching, logistics coordination, ethical evaluation, and human-supervised decision-making.

The platform combines multiple specialized AI agents with IBM Db2 to organize donor and recipient information, evaluate compatibility factors, estimate transportation feasibility, and generate explainable recommendations for authorized medical professionals.

**Important:** TransplantIQ is a clinical decision-support prototype. It does not independently allocate organs, authorize transplantation, or replace qualified medical professionals or official organ-allocation authorities.

---

## 1. Project Overview

Organ transplantation requires coordination between hospitals, transplant teams, donors, recipients, and transportation services. Delays in communication, fragmented information, clinical compatibility requirements, and transportation constraints can make coordination challenging.

TransplantIQ addresses these challenges through a centralized intelligent coordination platform.

It uses a multi-agent architecture in which specialized AI agents perform different responsibilities and share their findings through a central supervisor agent.

IBM Db2 acts as the enterprise data layer, supporting structured information storage, historical records, spatial data, and workflow auditing.

### Main Objectives

- Improve the organization of donor and recipient information.
- Support clinical compatibility assessment.
- Assist with organ transportation and logistics planning.
- Consider configured ethical and allocation criteria.
- Maintain traceable workflow and decision records.
- Provide explainable recommendations to authorized clinicians.
- Keep final medical and operational decisions under human control.

---

## 2. Problem Statement

The organ transplantation process involves several interconnected activities:

1. Collecting donor and recipient medical information.
2. Evaluating blood group and tissue compatibility.
3. Identifying suitable transplant centers.
4. Considering organ preservation and transportation time.
5. Reviewing ethical and allocation criteria.
6. Coordinating communication between medical teams.
7. Maintaining records of decisions and activities.

When these activities are managed through disconnected systems or manual coordination, it can become difficult to maintain a consistent overview of the transplant process.

TransplantIQ proposes an integrated platform to assist with these activities using Agentic AI and IBM Db2.

---

## 3. Proposed Solution

TransplantIQ introduces a multi-agent AI system where each agent handles a specialized responsibility.

The Supervisor Agent coordinates the execution of the agents and combines their findings into a recommendation.

The platform uses IBM Db2 to store and retrieve relevant information and maintain historical workflow records.

The generated recommendation is submitted to an authorized medical professional for review. Only an authorized human decision can move the request to the next permitted operational stage.

### Key Features

- Multi-agent AI coordination.
- Donor and recipient information management.
- ABO and HLA compatibility assessment support.
- Organ-specific clinical factor evaluation.
- Hospital location and distance analysis.
- Transportation and Cold Ischemia Time (CIT) monitoring.
- Configurable ethical-rule evaluation.
- Human-in-the-Loop approval workflow.
- IBM Db2 database integration.
- Historical data and audit tracking.
- Interactive dashboard and geographical visualization.

---

## 4. System Architecture

The following architecture represents the proposed overall system organization.

```text
                    TRANSPLANTIQ SYSTEM ARCHITECTURE

┌───────────────────────────────────────────────────────────────┐
│                         USER LAYER                            │
│                                                               │
│    Authorized Clinicians | Surgeons | Hospital Coordinators   │
└──────────────────────────────┬────────────────────────────────┘
                               │
                               ▼
┌───────────────────────────────────────────────────────────────┐
│                       FRONTEND LAYER                          │
│                                                               │
│                 Hospital Coordination Dashboard               │
│                                                               │
│  ┌────────────────┐  ┌────────────────┐  ┌─────────────────┐  │
│  │ Donor & Patient│  │ GIS Hospital   │  │ CIT Countdown   │  │
│  │ Information    │  │ Map            │  │ Monitoring      │  │
│  └────────────────┘  └────────────────┘  └─────────────────┘  │
│                                                               │
│                 Agent Execution & Approval Panel              │
└──────────────────────────────┬────────────────────────────────┘
                               │
                         REST API / WebSocket
                               │
                               ▼
┌───────────────────────────────────────────────────────────────┐
│                       BACKEND LAYER                           │
│                                                               │
│                     FastAPI Backend Engine                    │
│                                                               │
│       Authentication | Request Validation | API Routing      │
│                                                               │
│                Agent Execution & Orchestration                │
└──────────────────────────────┬────────────────────────────────┘
                               │
                               ▼
┌───────────────────────────────────────────────────────────────┐
│                     MULTI-AGENT AI LAYER                      │
│                                                               │
│                  ┌─────────────────────┐                      │
│                  │ 1. SUPERVISOR AGENT │                      │
│                  └──────────┬──────────┘                      │
│                             │                                 │
│          ┌──────────────────┼──────────────────┐              │
│          ▼                  ▼                  ▼              │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐      │
│  │ 2. PATIENT   │   │ 3. CLINICAL  │   │ 4. LOGISTICS │      │
│  │ CLINICAL     │   │ MATCHING     │   │ AGENT        │      │
│  │ AGENT        │   │ AGENT        │   │              │      │
│  └──────────────┘   └──────────────┘   └──────────────┘      │
│                                                               │
│          ┌──────────────────────┐                              │
│          ▼                     ▼                              │
│  ┌──────────────┐     ┌──────────────────┐                    │
│  │ 5. BIOETHICS │     │ 6. COORDINATION  │                    │
│  │ AGENT        │     │ AGENT (HITL)     │                    │
│  └──────────────┘     └──────────────────┘                    │
└──────────────────────────────┬────────────────────────────────┘
                               │
                               ▼
┌───────────────────────────────────────────────────────────────┐
│                       IBM Db2 DATA LAYER                      │
│                                                               │
│  ┌─────────────────┐  ┌─────────────────┐                    │
│  │ Donor Records   │  │ Recipient Data  │                    │
│  └─────────────────┘  └─────────────────┘                    │
│                                                               │
│  ┌─────────────────┐  ┌─────────────────┐                    │
│  │ Hospital & GIS  │  │ Matching Results│                    │
│  │ Information     │  │                 │                    │
│  └─────────────────┘  └─────────────────┘                    │
│                                                               │
│  ┌─────────────────┐  ┌─────────────────┐                    │
│  │ Temporal Tables │  │ Workflow &      │                    │
│  │                 │  │ Audit Logs      │                    │
│  └─────────────────┘  └─────────────────┘                    │
└──────────────────────────────┬────────────────────────────────┘
                               │
                               ▼
┌───────────────────────────────────────────────────────────────┐
│                    HUMAN GOVERNANCE LAYER                     │
│                                                               │
│                  Authorized Clinical Review                   │
│                              │                                │
│                              ▼                                │
│                      Approval Decision                        │
│                              │                                │
│                   ┌──────────┴──────────┐                     │
│                   ▼                     ▼                     │
│                APPROVED              REJECTED                 │
│                   │                     │                     │
│                   ▼                     ▼                     │
│          Authorized Next Step    Revision / Review            │
└───────────────────────────────────────────────────────────────┘
```

---

## 5. Multi-Agent AI Architecture

TransplantIQ uses six specialized agents to divide the organ coordination process into manageable tasks.

### 1. Supervisor Agent

The Supervisor Agent acts as the central coordinator of the multi-agent system.

Responsibilities:

- Receives the initial transplant request.
- Understands the requested operation.
- Determines which specialized agents are required.
- Coordinates agent execution.
- Collects and combines agent outputs.
- Prepares the overall recommendation.

### 2. Patient Clinical Agent

This agent handles donor and recipient information.

Responsibilities:

- Retrieves relevant donor information.
- Retrieves recipient clinical information.
- Organizes patient-related data for evaluation.
- Applies configured privacy and data-minimization procedures.
- Provides relevant information to the matching agent.

### 3. Clinical Matching Agent

This agent evaluates compatibility-related information.

Responsibilities:

- Checks ABO blood group compatibility.
- Evaluates HLA information.
- Considers organ-specific clinical factors.
- Reviews available donor and recipient information.
- Produces an explainable compatibility assessment.

Potential evaluation factors include:

- ABO blood group.
- HLA loci: A, B, C, DRB1 and DQB1.
- Organ-specific urgency indicators.
- MELD-related factors for liver transplantation.
- KDPI-related factors for kidney donor assessment.
- Relevant anthropometric and clinical information.

The factors and their interpretation must be configured according to validated clinical protocols. A compatibility score generated by the system is not a medical allocation decision.

### 4. Logistics Agent

The Logistics Agent evaluates transportation-related information.

Responsibilities:

- Identifies relevant transplant center locations.
- Evaluates geographical distance.
- Assists with transportation planning.
- Estimates potential transportation duration.
- Monitors the available preservation-time window.
- Presents logistics information for clinical review.

Potential transportation options:

- Ambulance.
- Helicopter.
- Medical transport aircraft.

### 5. Bioethics Agent

The Bioethics Agent checks configured ethical and allocation-related rules.

Responsibilities:

- Reviews applicable configured criteria.
- Identifies potential rule conflicts.
- Checks whether required information is available.
- Explains ethical considerations.
- Reports issues requiring human review.

The system must not claim official NOTTO or UNOS certification or complete policy compliance without formal validation.

### 6. Coordination Agent

The Coordination Agent manages the final review stage.

Responsibilities:

- Collects outputs from other agents.
- Prepares a consolidated recommendation.
- Creates a pending review request.
- Presents relevant evidence to the clinician.
- Records the approval, rejection, or request for additional information.
- Updates the workflow status.

This agent enforces the Human-in-the-Loop principle. It does not independently authorize organ allocation or dispatch.

---

## 6. End-to-End System Workflow

The following diagram explains how a transplant request moves through the system.

```text
                    TRANSPLANTIQ WORKFLOW
                             │
                             ▼
              ┌──────────────────────────┐
              │ 1. REQUEST INITIATION    │
              │                          │
              │ Clinician submits organ  │
              │ transplant request      │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ 2. SUPERVISOR AGENT      │
              │                          │
              │ Understands request and  │
              │ plans agent execution    │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ 3. PATIENT CLINICAL AGENT│
              │                          │
              │ Retrieves donor and      │
              │ recipient information   │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ 4. CLINICAL MATCHING     │
              │                          │
              │ ABO Compatibility        │
              │ HLA Matching             │
              │ Organ-Specific Factors   │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ 5. LOGISTICS AGENT       │
              │                          │
              │ Geographic Distance     │
              │ Transport Evaluation     │
              │ CIT Monitoring           │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ 6. BIOETHICS AGENT       │
              │                          │
              │ Reviews configured      │
              │ ethical criteria        │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ 7. COORDINATION AGENT    │
              │                          │
              │ Prepares recommendation│
              │ and pending request     │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ 8. CLINICAL REVIEW       │
              │                          │
              │ Authorized clinician     │
              │ examines recommendation │
              └────────────┬─────────────┘
                           │
                           ▼
                   ┌───────────────┐
                   │   DECISION    │
                   └───────┬───────┘
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
       ┌────────────────┐    ┌────────────────┐
       │    APPROVED    │    │    REJECTED    │
       │                │    │                │
       │ Record approved│    │ Record reason  │
       │ action         │    │ or revision    │
       └───────┬────────┘    └───────┬────────┘
               │                    │
               └──────────┬─────────┘
                          ▼
                 ┌────────────────┐
                 │  AUDIT LOGGING │
                 │                │
                 │ Record workflow│
                 │ activity       │
                 └───────┬────────┘
                         │
                         ▼
                    END PROCESS
```

*Note: This is a simplified presentation workflow. The actual supervisor may coordinate multiple agents in parallel or in a different order depending on the request.*

---

## 7. Human-in-the-Loop (HITL) Decision System

Human-in-the-Loop is one of the most important principles of TransplantIQ.

AI agents can analyze information and prepare recommendations, but final clinical and operational decisions must remain with authorized professionals.

### Approval Workflow

```text
             AI AGENTS COMPLETE EVALUATION
                         │
                         ▼
             GENERATE CLINICAL PROPOSAL
                         │
                         ▼
              CREATE PENDING REQUEST
                         │
                         ▼
             AUTHORIZED CLINICIAN REVIEW
                         │
                         ▼
                  APPROVAL DECISION
                         │
              ┌──────────┼───────────┐
              │          │           │
              ▼          ▼           ▼
           APPROVE     REJECT     NEED MORE
                                  INFORMATION
              │          │           │
              ▼          ▼           ▼
          Record      Record      Request
          Approval    Rejection   Revision
              │          │           │
              └──────────┼───────────┘
                         │
                         ▼
                  UPDATE STATUS
                         │
                         ▼
                  CREATE AUDIT LOG
                         │
                         ▼
                    END PROCESS
```

### Benefits

- Prevents autonomous AI allocation decisions.
- Keeps medical professionals responsible for clinical decisions.
- Provides a reviewable recommendation.
- Records approval and rejection activities.
- Supports accountability and traceability.

---

## 8. IBM Db2 Integration

IBM Db2 acts as the enterprise data management layer of TransplantIQ.

It is intended to provide reliable storage, structured data access, historical tracking, and audit support.

### Why IBM Db2?

- Supports structured relational data.
- Provides SQL-based data retrieval.
- Supports temporal data management.
- Provides spatial data capabilities.
- Supports transaction management.
- Offers enterprise-oriented database functionality.

### Db2 Features Used or Proposed

| Feature | Purpose in TransplantIQ |
|---|---|
| Relational Tables | Store donor, recipient and hospital information |
| System-Period Temporal Tables | Maintain historical versions of supported records |
| Spatial Extender | Support hospital location and geographical queries |
| pureScale | Potential high-availability deployment capability |
| SQL Transactions | Maintain consistent database operations |
| SHA-256 Audit Hash | Support integrity verification of audit records |
| Parameterized Queries | Reduce SQL injection risks |

Actual availability of these capabilities depends on the selected Db2 edition, configuration, and implementation.

### Temporal Database Concept

Temporal tables can help retrieve historical information.

For example:

```sql
SELECT *
FROM DONORS
FOR SYSTEM_TIME AS OF CURRENT TIMESTAMP;
```

This is an illustrative query. The table must be created with the appropriate Db2 system-period temporal definition before this query can be used.

### Audit Tracking

The system can record:

- User or agent responsible for an action.
- Type of operation.
- Request identifier.
- Timestamp.
- Previous and updated status.
- Audit integrity information.

A SHA-256 hash can help detect changes to recorded audit data, but a hash alone does not guarantee tamper-proof storage.

---

## 9. Clinical Matching and Compatibility Assessment

Clinical Matching is a central capability of TransplantIQ.

The Clinical Matching Agent evaluates relevant donor and recipient information and generates an assessment for review.

### Evaluation Factors

**ABO Compatibility**

Evaluates blood group compatibility between donor and recipient according to organ-specific clinical rules.

**HLA Compatibility**

Considers human leukocyte antigen information across relevant loci:

- HLA-A
- HLA-B
- HLA-C
- HLA-DRB1
- HLA-DQB1

**Organ-Specific Clinical Factors**

Examples include:

- MELD-related information for liver transplantation.
- KDPI-related information for kidney donor assessment.
- Relevant medical urgency indicators.
- Anthropometric considerations where applicable.

### Matching Process

```text
          DONOR INFORMATION
                 │
                 ▼
          RECIPIENT INFORMATION
                 │
                 ▼
        VALIDATE AVAILABLE DATA
                 │
                 ▼
          ABO COMPATIBILITY
                 │
                 ▼
           HLA ASSESSMENT
                 │
                 ▼
       ORGAN-SPECIFIC EVALUATION
                 │
                 ▼
       GENERATE MATCHING REPORT
                 │
                 ▼
       PRESENT CLINICAL EVIDENCE
                 │
                 ▼
         AUTHORIZED HUMAN REVIEW
```

The system's matching output is a decision-support assessment, not a substitute for laboratory cross-matching, specialist evaluation, or official allocation procedures.

---

## 10. Organ Logistics and Cold Ischemia Time

Organ transportation is a time-sensitive component of transplantation.

The Logistics Agent evaluates the available geographical and transportation information to support coordination between transplant centers.

### Logistics Responsibilities

- Identify donor and recipient hospital locations.
- Estimate geographical distance.
- Compare potential transportation options.
- Estimate transportation duration.
- Display preservation-time information.
- Highlight potential logistics constraints.

### Transportation Options

| Transport Type | Potential Use |
|---|---|
| Ambulance | Ground transportation |
| Helicopter | Rapid regional transportation |
| Medical Jet | Long-distance transportation |

### Cold Ischemia Time (CIT)

Cold Ischemia Time refers to the period an organ remains preserved outside the body under appropriate conditions before transplantation.

Illustrative commonly cited ranges are shown below. These are not universal clinical limits or guaranteed safe windows.

| Organ | Illustrative CIT Range |
|---|---|
| Heart | 4–6 hours |
| Lung | 6–8 hours |
| Liver | 10–12 hours |
| Kidney | 24–36 hours |
| Cornea | Depends on preservation method |

Actual acceptable preservation and transportation windows depend on the organ, preservation technique, clinical circumstances, and applicable medical protocols.

---

## 11. Bioethics and Policy Evaluation

The Bioethics Agent evaluates configured ethical criteria and reports potential concerns.

Its purpose is to support transparent and consistent review rather than independently decide who receives an organ.

### Responsibilities

- Evaluate configured allocation criteria.
- Identify missing or conflicting information.
- Highlight potential policy violations.
- Provide explanations for flagged conditions.
- Escalate uncertain cases to authorized professionals.

The project may use NOTTO and UNOS materials as references when configuring its policy rules. It must not claim official certification, endorsement, or complete compliance without appropriate validation.

---

## 12. Database Design

The following is a conceptual database structure for TransplantIQ. Actual table and column names should be aligned with the implemented Db2 schema.

```text
                    TRANSPLANTIQ DATABASE
                              │
                              ▼
                     ┌─────────────────┐
                     │    HOSPITALS    │
                     │─────────────────│
                     │ hospital_id (PK)│
                     │ hospital_name   │
                     │ location        │
                     │ latitude        │
                     │ longitude       │
                     └────────┬────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
        ┌─────────────────┐       ┌─────────────────┐
        │     DONORS      │       │   RECIPIENTS    │
        │─────────────────│       │─────────────────│
        │ donor_id (PK)   │       │ recipient_id(PK)│
        │ hospital_id(FK) │       │ hospital_id(FK) │
        │ blood_group     │       │ blood_group     │
        │ organ_type      │       │ organ_required  │
        │ availability    │       │ medical_urgency │
        └────────┬────────┘       └────────┬────────┘
                 │                         │
                 ▼                         │
        ┌─────────────────┐                │
        │  ORGAN_DETAILS  │                │
        │─────────────────│                │
        │ organ_id (PK)   │                │
        │ donor_id (FK)   │                │
        │ organ_type      │                │
        │ preservation    │                │
        │ retrieval_time  │                │
        └────────┬────────┘                │
                 │                         │
                 └────────────┬────────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ MATCHING_RESULTS│
                     │─────────────────│
                     │ match_id (PK)   │
                     │ donor_id (FK)   │
                     │ recipient_id(FK)│
                     │ compatibility   │
                     │ assessment      │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ ALLOCATION      │
                     │ REQUESTS        │
                     │─────────────────│
                     │ request_id (PK) │
                     │ match_id (FK)   │
                     │ approval_status │
                     │ clinical_notes  │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │  WORKFLOW_LOG   │
                     │─────────────────│
                     │ log_id (PK)     │
                     │ request_id (FK) │
                     │ action          │
                     │ actor           │
                     │ audit_hash      │
                     │ created_at      │
                     └─────────────────┘
```

### Main Database Entities

| Table | Description |
|---|---|
| HOSPITALS | Stores transplant center information |
| DONORS | Stores donor-related information |
| RECIPIENTS | Stores recipient-related information |
| ORGAN_DETAILS | Stores organ and preservation information |
| MATCHING_RESULTS | Stores compatibility assessment results |
| ALLOCATION_REQUESTS | Stores requests and approval status |
| WORKFLOW_LOG | Stores workflow and audit activities |

---

## 13. Technology Stack

| Component | Technology | Purpose |
|---|---|---|
| Frontend | HTML, CSS, JavaScript | User interface |
| Backend | Python, FastAPI | Application and API layer |
| Agentic AI | Multi-agent architecture | Specialized task execution |
| Database | IBM Db2 | Enterprise data management |
| Database Connector | ibm_db / ibm_db_dbi | Python and Db2 connectivity |
| API Documentation | Swagger / OpenAPI | API exploration and testing |
| GIS | Leaflet | Geographical visualization |
| Data Exchange | JSON | API communication |

*Use this table as a description of the project stack; retain only technologies that are actually present in your implementation.*

---

## 14. Dashboard and User Interface

The TransplantIQ dashboard is intended to provide a centralized view of transplant coordination activities.

### Dashboard Components

**Donor and Recipient Panel**

Displays relevant donor and recipient information.

**Clinical Matching Panel**

Shows compatibility assessment details and supporting clinical factors.

**GIS Map**

Displays participating hospital locations and potential transportation routes.

**CIT Monitoring**

Displays preservation-time information and estimated remaining time when the necessary data is available.

**Agent Execution Panel**

Shows which AI agents have completed their assigned tasks and their outputs.

**Approval Panel**

Allows authorized clinicians to review recommendations and record decisions.

---

## 15. Example Use Cases and Demonstration Scenarios

The following scenarios can be used to demonstrate the proposed system with synthetic data.

### Scenario 1: Pediatric Heart Transplant Coordination

- Enter synthetic donor and recipient details.
- Evaluate relevant compatibility factors.
- Review transportation distance.
- Display the estimated preservation-time window.
- Present the recommendation for clinical review.

### Scenario 2: Multi-Center Kidney Matching

- Retrieve synthetic records from multiple transplant centers.
- Evaluate relevant ABO and HLA information.
- Present potential matching candidates.
- Display the assessment factors for authorized review.

### Scenario 3: Emergency Liver Coordination

- Enter an illustrative emergency request.
- Evaluate configured urgency-related information.
- Review hospital distance and transportation options.
- Display logistics constraints and the recommendation.

### Scenario 4: IBM Db2 Temporal Audit

- Create or update a supported record.
- Retrieve historical information using temporal queries.
- Display the recorded workflow activity.
- Demonstrate how audit information can support traceability.

All demonstration scenarios should use synthetic or properly authorized data, not real patient information.

---

## 16. Human Safety, Privacy and Security

TransplantIQ is designed around responsible AI and human oversight.

### Key Principles

- Human approval for clinical and operational decisions.
- Role-based access to sensitive information.
- Parameterized database queries.
- Secure handling of patient-related information.
- Data minimization and de-identification where applicable.
- Audit logging of important workflow activities.
- Clear explanations for AI-generated recommendations.
- Use of synthetic data during development and demonstrations.

A prototype implementation does not automatically establish compliance with healthcare privacy regulations or clinical safety standards. Formal security, privacy, and clinical validation would be required before real-world deployment.

---

## 17. Project Folder Structure

```text
TransplantIQ/
│
├── backend/
│   ├── main.py
│   ├── agents.py
│   ├── db.py
│   ├── test_suite.py
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── docs/
│   ├── PITCH_DEMO_SCRIPT.md
│   ├── DB2_DEEP_DIVE.md
│   ├── ARCHITECTURE.md
│   └── DB2_CONNECTOR.md
│
├── scripts/
│   ├── verify_project.py
│   └── run_demo.bat
│
└── README.md
```

---

## 18. Installation and Setup

### Prerequisites

Install the following before running the project:

- Python 3.10 or later, compatible with the project's dependencies.
- IBM Db2 instance and database credentials.
- Git.
- A modern web browser.

### Step 1: Clone the Repository

```bash
git clone https://github.com/GandikotiRavi/TransplantIQ.git
cd TransplantIQ
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r backend/requirements.txt
```

### Step 4: Configure Database Connection

Configure the Db2 connection settings required by the application.

Use environment variables for credentials rather than committing passwords or secrets to GitHub.

### Step 5: Verify the Project

```bash
python scripts/verify_project.py
```

### Step 6: Run Tests

```bash
python backend/test_suite.py
```

### Step 7: Start the Backend

```bash
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Step 8: Open API Documentation

Visit:

```text
http://localhost:8000/docs
```

### Step 9: Open the Frontend

Open the frontend file in your browser:

```text
frontend/index.html
```

Alternatively, use the provided demonstration script if it is configured for your environment:

```text
scripts/run_demo.bat
```

---

## 19. Testing and Verification

The project includes a test suite and a verification script.

### Verification

```bash
python scripts/verify_project.py
```

### Test Execution

```bash
python backend/test_suite.py
```

### Suggested Test Areas

- Backend API availability.
- Database connectivity.
- Donor and recipient data retrieval.
- Clinical matching logic.
- Agent execution and response handling.
- Logistics calculations.
- Approval and rejection workflows.
- Audit record creation.
- Error handling and invalid input validation.

Actual test coverage depends on the test cases implemented in the repository.

---

## 20. API Documentation

The FastAPI application can expose interactive API documentation through Swagger UI.

Once the backend is running, open:

```text
http://localhost:8000/docs
```

Swagger UI can be used to inspect available endpoints, review request and response formats, and test supported API operations.

---

## 21. Expected Benefits

TransplantIQ aims to provide the following benefits:

- Centralized transplant coordination information.
- Better visibility into donor and recipient assessment.
- Structured clinical compatibility evaluation.
- Improved logistics planning support.
- Explainable agent-generated recommendations.
- Human-supervised workflow management.
- Historical tracking and audit visibility.
- A foundation for future integration with hospital information systems.

These are intended project benefits and should not be presented as measured clinical outcomes without evaluation.

---

## 22. Future Enhancements

Potential future improvements include:

1. Integration with authorized hospital information systems.
2. Secure clinical data exchange.
3. Advanced clinical decision-support models validated by specialists.
4. More detailed GIS-based transportation analysis.
5. Real-time transportation information integration.
6. Enhanced role-based access and authentication.
7. Advanced Db2 temporal and spatial queries.
8. Improved audit integrity and monitoring.
9. Additional organ-specific assessment modules.
10. Clinical validation and usability evaluation with qualified professionals.

---

## 23. Limitations

- The system is a prototype and is not intended for direct clinical deployment.
- Clinical matching outputs require specialist validation.
- Real-time hospital, donor, and recipient data depend on authorized integrations.
- Transportation estimates depend on the accuracy and availability of location and traffic data.
- Ethical and allocation rules require continuous validation against applicable official policies.
- Db2 capabilities depend on the configured database edition and deployment.
- Human approval remains mandatory for clinical and operational decisions.

---

## 24. Project Documentation

Additional project documentation:

- [Architecture Documentation](https://github.com/GandikotiRavi/TransplantIQ/blob/main/TransplantIQ/docs/ARCHITECTURE.md)
- [IBM Db2 Technical Deep Dive](https://github.com/GandikotiRavi/TransplantIQ/blob/main/TransplantIQ/docs/DB2_DEEP_DIVE.md)
- [Pitch and Demo Script](https://github.com/GandikotiRavi/TransplantIQ/blob/main/TransplantIQ/docs/PITCH_DEMO_SCRIPT.md)
- [Db2 Connector Guide](https://github.com/GandikotiRavi/TransplantIQ/blob/main/TransplantIQ/docs/DB2_CONNECTOR.md)

---

## 25. Conclusion

TransplantIQ brings together Agentic AI, IBM Db2, clinical decision-support concepts, and human-supervised coordination into a unified organ transplant coordination platform.

By dividing complex activities among specialized agents, the system aims to organize clinical information, evaluate compatibility factors, assist with transportation planning, and provide explainable recommendations.

Its most important principle is that **AI supports medical professionals, while authorized humans retain responsibility for clinical and operational decisions.**

**TransplantIQ – Smarter Organ Coordination. Explainable AI. Human-Led Decisions.**

---

## License

Add the appropriate open-source license to this repository before publishing or distributing the project.
