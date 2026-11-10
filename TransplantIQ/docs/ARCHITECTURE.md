# TransplantIQ Architecture Specification
**Db2Hack 2026 · Enterprise Agentic AI Coordination System**

---

## 🏗️ High-Level System Architecture

```
                       Authorized Clinicians & Surgeons
                                     │
                                     ▼
                Modern Responsive Command Center (frontend/index.html)
                                     │  REST API / WebSockets
                                     ▼
                      FastAPI Backend Engine (backend/main.py)
                                     │
                ┌────────────────────┴────────────────────┐
                ▼                                         ▼
   Multi-Agent Clinical Swarm (backend/agents.py)    IBM Db2 Enterprise Layer (backend/db.py)
   ┌─────────────────────────────────────────┐       ┌─────────────────────────────────────┐
   │ 1. Supervisor Agent (Planner & Router)  │       │ • Db2 Temporal Tables (System-Time) │
   │ 2. Patient Agent (Privacy De-ident.)    │◄─────►│ • Db2 Spatial Extender (Geodesic)   │
   │ 3. Clinical Matching Agent (5-HLA+ABO)  │       │ • pureScale Active-Active Cluster   │
   │ 4. Logistics Agent (Cold Ischemia Time) │       │ • Cryptographic Audit Ledger        │
   │ 5. Bioethics Agent (NOTTO/UNOS Parity)  │       │ • 100% Parameterized Access Layer   │
   │ 6. Coordination Agent (HITL Gatekeeper) │       │ • ibm_db / ibm_db_dbi Native Driver │
   └─────────────────────────────────────────┘       └─────────────────────────────────────┘
```

---

## 🤖 The 6-Agent Clinical Swarm

| Agent | Responsibilities | Inputs | Core Outputs |
|---|---|---|---|
| **Supervisor Agent** | Intent classification, dynamic execution planning, routing, consensus synthesis. | Natural Language query, clinical directives. | Execution plan, summarized clinical response. |
| **Patient Agent** | Privacy-preserving query of active donor records and waiting candidates. | Organ filter, blood group filter, donor ID. | De-identified donor and recipient cohorts. |
| **Clinical Matching Agent** | 5-Locus HLA matching (A, B, C, DRB1, DQB1), ABO compatibility, MELD urgency scoring, anthropometric size ratio check. | Donor & recipient medical records. | Ranked candidate pairs with explainable scoring (0-100). |
| **Logistics & Cold Ischemia Agent** | Geodesic hospital distance calculation, transport modality selection (Ambulance / Helicopter / Jet), and Cold Ischemia Time boundary check. | Hospital lat/lon, organ type, distance in km. | Transit duration, ischemia margin, viability verdict (FEASIBLE vs EXCEEDS LIMIT). |
| **Bioethics & Allocation Compliance Agent** | Audits candidate queues against NOTTO/UNOS principles: pediatric priority, waitlist equity, absence of non-clinical demographic bias. | Candidate waitlist history, age, medical utility. | Ethical Allocation Certificate, compliance score. |
| **Coordination & HITL Agent** | Creates pending allocation requests, formats surgical dispatch dossiers, and writes cryptographic SHA-256 signatures to Db2 audit ledger. | Top validated clinical match. | Pending Request ID, verification hash, Human-in-the-Loop review queue. |

---

## 🔒 Human-in-the-Loop (HITL) Governance

1. **Strict Decision-Support Rule:** The AI swarm cannot alter patient allocation states to `ALLOCATED` or dispatch couriers autonomously.
2. **Review Checkpoint:** Every viable match produces a row in `TRANSPLANT_REQUESTS` with status `PENDING`.
3. **Clinician Authorization:** The Chief Transplant Officer reviews the side-by-side dossier, enters clinical rationale notes, and executes digital sign-off (`APPROVED` or `REJECTED`).
4. **Cryptographic Trail:** Both agent steps and clinician actions generate immutable SHA-256 signatures logged to `WORKFLOW_LOG`.

---

## 🗄️ Database Schema & Db2 Compatibility

The database comprises 5 primary tables and 2 system temporal history tables:
1. `HOSPITALS`: Center name, city, latitude, longitude, airport code, helipad flag, ICU capacity.
2. `DONORS`: Clinical profiles, blood group, organ, 5 HLA loci, KDPI, ischemic start timestamp, system temporal columns (`SYS_START`, `SYS_END`).
3. `DONORS_HISTORY`: Historical versions for Db2 `FOR SYSTEM_TIME AS OF` reconstruction.
4. `RECIPIENTS`: Medical urgency, MELD score, PRA %, pediatric flag, dialysis duration, waiting days.
5. `RECIPIENTS_HISTORY`: Temporal archive of recipient waitlist state.
6. `TRANSPLANT_REQUESTS`: Multi-agent scores (Composite, HLA, Logistics, Bioethics), transit mode, ischemia safety margin, clinician sign-off notes, audit hash.
7. `WORKFLOW_LOG`: Immutable audit trail with SHA-256 signatures.
