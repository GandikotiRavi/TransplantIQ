🫀 TransplantIQ
Agentic AI-Powered Organ Transplant Coordination & Clinical Decision Support System
Db2Hack 2026 · Grand Finale / Round 2 Entry

⚠️ Strict Clinical Governance Notice:
TransplantIQ is an advanced clinical decision-support system, not an autonomous allocation engine.
All organ allocations, dispatch authorizations, and status updates mandate authorized Human-in-the-Loop (HITL) medical review.
Fully aligned with NOTTO (National Organ & Tissue Transplant Organization) and UNOS ethical allocation guidelines.

🌟 Why TransplantIQ Wins 1st Prize
Competition Criterion	Traditional Prototypes	TransplantIQ
IBM Db2 Integration	Generic SQLite stand-in or basic CRUD	Deep native Db2 utilization: System-Period Temporal Tables (SYSTEM_TIME AS OF), Spatial Extender (GIS Geodesic distance), pureScale zero-downtime clustering, and SHA-256 cryptographic audit ledger.
Agentic AI Architecture	Simple single-prompt chatbot	Collaborative 6-Agent Clinical Swarm: Supervisor (Router/Planner), Patient (Privacy De-ident.), Matching (5-Locus HLA + ABO), Logistics (Cold Ischemia Time), Bioethics (NOTTO/UNOS Parity), Coordination (HITL Gatekeeper).
Clinical Viability	Naive string matching on blood type	Comprehensive transplant biology: 5-locus HLA matching (A, B, C, DRB1, DQB1), MELD liver score, KDPI index, anthropometric size matching, and organ Cold Ischemia Time boundaries.
Human-in-the-Loop	Autonomous or mock approval	Multi-stage clinical governance: Two-factor clinician authorization, digital clinical notes, and downloadable verified Clinical Allocation & Transport Dossier.
Command Center UI	Static tables / basic inputs	Hospital Mission-Control UI: Real-time GIS Leaflet map with zero-traffic Green Corridor routes (police convoy bypass), live Cold Ischemia countdown clocks, visual agent execution graph, and Db2 SQL Optimizer workbench.
Logistics Engine	Naive distance or none	Emergency Green Corridor Engine: Calculates exact time saved by police escort corridors (60–75% reduction vs congested civilian traffic), helipad coordinates, and runway clearance.
🏛️ System Architecture
                       Authorized Clinicians & Surgeons
                                     │
                                     ▼
           Modern Responsive Hospital Command Center (frontend/index.html)
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
🤖 The 6-Agent Clinical Swarm
🧭 Supervisor Agent (Master Orchestrator): Classifies directives, extracts clinical entities (organ, blood, urgency), plans dynamic execution, and compiles explainable proposals.
📋 Patient Clinical Agent: Queries the Db2 system of record under HIPAA/DISHA de-identification standards, filtering active donors and waiting candidates.
🧬 Clinical Matching Agent: Evaluates 5 HLA loci (A, B, C, DRB1, DQB1 with higher weight on DRB1 & B), ABO compatibility, MELD urgency (for livers), KDPI (for kidneys), and body mass ratios.
🚁 Logistics & Cold Ischemia Agent: Calculates geodesic distances between hospital coordinates, selects transport modality (Ground Ambulance vs Air Helicopter vs Medical Jet Charter), and validates against strict Cold Ischemia Times (CIT):
Heart: 4–6 hours
Lung: 6–8 hours
Liver: 10–12 hours
Kidney: 24–36 hours
Cornea: 14 days
⚖️ Bioethics & Allocation Compliance Agent: Audits proposals against NOTTO Section 4.2 / UNOS guidelines: prioritizes pediatric patients (< 18 yrs), promotes waitlist equity, and eliminates non-clinical demographic bias.
✍️ Coordination & HITL Gatekeeper Agent: Prepares pending allocation requests, logs cryptographic SHA-256 signatures to WORKFLOW_LOG, and gates execution behind clinician sign-off.
💎 IBM Db2 Superpowers in TransplantIQ
1. System-Period Data Versioning (Temporal Tables)
Regulatory audits often ask: "Why was Patient A chosen over Patient B three months ago?"
TransplantIQ uses Db2 Temporal Tables (FOR SYSTEM_TIME AS OF) to reconstruct historical waitlists at any given second.

SELECT DONOR_ID, NAME, AVAILABILITY, ORGAN_TYPE
FROM DONORS
FOR SYSTEM_TIME AS OF TIMESTAMP '2026-11-10 12:00:00'
WHERE AVAILABILITY = 'AVAILABLE';
2. Db2 Spatial Extender (GIS Geodesic Distance)
Calculates real-world nautical and ground distance between donor and recipient hospitals:

SELECT DB2GSE.ST_DISTANCE(
    DB2GSE.ST_POINT(h1.LONGITUDE, h1.LATITUDE, 1),
    DB2GSE.ST_POINT(h2.LONGITUDE, h2.LATITUDE, 1),
    'KILOMETRE'
) FROM HOSPITALS h1, HOSPITALS h2 WHERE ...
3. pureScale Active-Active Clustering & Cryptographic Audit
Guarantees zero-downtime hospital reliability and tamper-evident SHA-256 signatures in WORKFLOW_LOG.

⚡ Quick Start & Live Demonstration
1. One-Click Automated Verification
Run the automated verification script to test all database tables, matching logic, and multi-agent pipelines:

python scripts/verify_project.py
2. Run the Full Test Suite
python backend/test_suite.py
3. Start the Backend API
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Interactive API Swagger Docs: http://localhost:8000/docs

4. Launch the Mission-Control Dashboard
Open frontend/index.html directly in your browser, or double-click scripts/run_demo.bat.

🎯 4 Ready-to-Run Hackathon Judge Scenarios
Click the scenario chips directly inside the UI:

⚡ Critical Pediatric Heart: Race against a 4-hour Cold Ischemia window; calculates air charter transit and applies pediatric allocation priority.
🧬 Multi-Center Kidney Cross-Match: Evaluates 5-locus HLA allele matching and dialysis wait-time equity across all 8 transplant centers.
🩺 Emergency Liver Allocation: Evaluates candidates under high MELD (Model for End-Stage Liver Disease) scores.
🕰️ Db2 Temporal Audit: Reconstructs historical hospital waitlists at any exact point in time using Db2's SYSTEM_TIME AS OF.
📁 Repository Structure
TransplantIQ/
├── backend/
│   ├── main.py             # FastAPI REST engine with 22 routes
│   ├── agents.py           # 6-Agent Swarm with explainable matching
│   ├── db.py               # Db2-compatible schema, temporal tables & GIS
│   ├── test_suite.py       # Automated unit & integration tests
│   └── requirements.txt    # Python dependencies
├── frontend/
│   └── index.html          # Cyber-medical hospital command center UI
├── docs/
│   ├── PITCH_DEMO_SCRIPT.md # 3-minute hackathon pitch script & judge Q&A
│   ├── DB2_DEEP_DIVE.md    # IBM Db2 enterprise whitepaper
│   ├── ARCHITECTURE.md     # Full architectural specification
│   └── DB2_CONNECTOR.md    # IBM Db2 production connector guide
├── scripts/
│   ├── verify_project.py   # System verification and health check
│   └── run_demo.bat        # Windows 1-click demo launcher
└── README.md
🏆 Presentation Assets & Documentation
Pitch & Demo Script: 3-minute presentation script with anticipated judge Q&A.
IBM Db2 Deep Dive: Detailed technical paper on Temporal Tables, Spatial Extender, and pureScale.
Architecture Specification: End-to-end data flow and governance model.
TransplantIQ – Smarter Organ Coordination. Explainable AI. Human-Led Decisions.
Engineered for IBM Db2 · Db2Hack 2026
