# TransplantIQ – 3-Minute Hackathon Winning Pitch & Demo Script
**Db2Hack 2026 · Grand Finale Presentation Guide**

---

## ⏱️ Executive Summary & Value Proposition

- **Problem:** Every year, over 40,000 viable donor organs go to waste globally due to coordination bottlenecks, slow manual cross-matching, and miscalculated Cold Ischemia Times (the biological clock ticking the moment an organ is harvested: 4-6 hours for a heart).
- **Existing Systems:** Today's hospital systems are passive databases. They **store** records, but they **cannot coordinate, cross-match, or reason** in real-time under intense biological time pressure.
- **The Breakthrough:** **TransplantIQ** — an Agentic AI clinical coordination platform natively engineered on top of **IBM Db2**. A swarm of 6 specialized clinical agents works alongside transplant surgeons to find compatible donors, calculate multi-city flight paths, enforce strict bioethical parity, and reconstruct historical waitlists using Db2 Temporal Tables.

---

## 🎤 3-Minute Live Pitch Script (Word-for-Word)

### [0:00 - 0:45] The Hook & The Problem
> *"Distinguished judges, imagine this: At 2:00 AM, a deceased donor's heart becomes available in Chennai. In New Delhi, 2,000 kilometers away, a 12-year-old child has less than 48 hours to live.  
> Between them is a ticking clock: **Cold Ischemia Time**. A human heart remains viable outside the body for only 4 to 6 hours.  
> Right now, transplant coordinators are manually calling hospitals, cross-referencing paper logs, and guessing flight feasibility. Delays of just 30 minutes cause viable organs to be discarded while children die on waiting lists.  
> Why? Because our databases store records, but they don't coordinate them. Today, we introduce **TransplantIQ**."*

### [0:45 - 1:45] The Solution & Agentic Architecture
> *"TransplantIQ is not an autonomous allocator — it is an **Agentic Clinical Decision Support Swarm** governed by strict Human-in-the-Loop oversight.  
> On top of an **IBM Db2** enterprise system of record, our collaborative multi-agent swarm activates in parallel:  
> 1. **The Patient Agent** securely queries HIPAA/DISHA de-identified donor and recipient cohorts.  
> 2. **The Clinical Matching Agent** computes 5-locus HLA allele compatibility, ABO blood barriers, and MELD urgency scores.  
> 3. **The Logistics & Cold Ischemia Agent** calculates great-circle geodesic distances between hospital coordinates, checks helipad readiness, and dispatches air charters with real-time countdown clocks.  
> 4. **The Bioethics Agent** guarantees compliance with NOTTO and UNOS principles — prioritizing pediatric patients and eliminating demographic bias.  
> 5. And **The Coordination Agent** prepares an auditable allocation dossier for clinician sign-off."*

### [1:45 - 2:30] Live System Demonstration
> *(Screen switch to TransplantIQ Dashboard)*  
> *"Let's see it live:  
> 1. We issue a clinical directive: **'Find potential heart matches for urgent pediatric candidate within 4-hour ischemic limit.'**  
> 2. Watch the live Agent Execution Graph: In under 200 milliseconds, the agents retrieve candidates, cross-match HLA loci, and calculate air ambulance transit from Chennai to Bengaluru.  
> 3. Look at the result: A 78.7/100 composite match with a 2.5-hour transit time and a safe 2.5-hour ischemia buffer.  
> 4. Notice the **Human-in-the-Loop** checkpoint: No organ is dispatched automatically. Dr. Sarah Chen reviews the dossier, enters clinical notes, and digitally authorizes the dispatch.  
> 5. Instantly, an immutable SHA-256 cryptographic certificate is generated for the surgical team."*

### [2:30 - 3:00] The IBM Db2 Superpower & Close
> *"Judges, why is IBM Db2 essential for this mission?  
> When a regulatory body asks, 'Why was Patient A chosen over Patient B three months ago?', traditional databases cannot answer without complex audit logs.  
> With **IBM Db2 Temporal Tables**, we execute `FOR SYSTEM_TIME AS OF` queries to reconstruct the exact hospital waitlist at any historical microsecond. Combined with **Db2 Spatial Extender** and **pureScale zero-downtime clustering**, Db2 is the ultimate healthcare foundation.  
> TransplantIQ turns passive hospital data into life-saving action. Thank you."*

---

## 🎯 Anticipated Judge Q&A & Winning Answers

### Q1: "Is this replacing doctors? What if the AI makes a bad recommendation?"
**Winning Answer:**
> *"Absolutely not. TransplantIQ is strictly a clinical decision-support system, not an autonomous allocator. By design, the Coordination Agent only creates **PENDING** requests. No status changes, no surgical theater bookings, and no organ couriers can move without two-factor human clinician review and digital authorization. Furthermore, our matching engine is 100% explainable — we output factor-by-factor HLA and ischemic breakdowns, not a black-box neural score."*

### Q2: "How deeply does this actually use IBM Db2 features?"
**Winning Answer:**
> *"TransplantIQ relies on three core Db2 capabilities that no generic database provides as cleanly:  
> 1. **Db2 Temporal Tables (System-Period Data Versioning):** Mandatory for healthcare audit compliance under UNOS and NOTTO regulations, enabling instant point-in-time waitlist reconstruction via `FOR SYSTEM_TIME AS OF`.  
> 2. **Db2 Spatial Extender:** Computes geodesic coordinates between hospital helipads to enforce biological Cold Ischemia Time boundaries.  
> 3. **Db2 pureScale:** Active-active high availability cluster ensuring zero seconds of downtime during critical organ dispatch."*

### Q3: "How does this prevent algorithmic bias in organ distribution?"
**Winning Answer:**
> *"Our dedicated **Bioethics & Allocation Compliance Agent** explicitly audits proposals against national allocation ethics (such as NOTTO Section 4.2). It enforces objective medical criteria (urgency, MELD score, waiting days, pediatric tier) and rigorously blocks subjective or non-clinical demographic factors."*

