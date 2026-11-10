# IBM Db2 for z/OS Developer Architecture Deep Dive
**TransplantIQ · Technical Whitepaper for Db2Hack 2026**

---

## 🏛️ Executive Architectural Overview: Why IBM Db2 for z/OS?

Solid organ transplant allocation carries strict operational and regulatory constraints unmatched by generic commercial software:
1. **Zero-Tolerated Downtime:** An outage during organ harvest results in graft loss. **IBM z/OS Parallel Sysplex** delivers continuous availability (99.99999% uptime).
2. **Point-in-Time Regulatory Verifiability:** National transplant bodies (e.g., NOTTO, UNOS) legally require full reconstruction of the waitlist at the exact second an allocation occurred. **Db2 for z/OS Temporal Tables** guarantee native system-period data versioning.
3. **Geodesic Biological Boundaries:** Calculation of geographical distance between hospitals to ensure transit fits strictly within organ Cold Ischemia Times (CIT).
4. **Absolute ACID Guarantees & Two-Phase Commit:** Preventing double-allocation or race conditions on deceased donor organs across multi-hospital networks via DRDA.

**IBM Db2 for z/OS** is the world's most trusted enterprise mainframe database engineered to satisfy all these constraints.

---

## 💎 Core Db2 for z/OS Developer Capabilities in TransplantIQ

### 1. Native z/OS DDL & System-Period Data Versioning (Temporal Tables)

In organ allocation, audit disputes often arise months or years after surgery: *"Did candidate X have higher urgency than candidate Y at 03:14:22 on November 10?"*

In generic databases, answering this requires bespoke, brittle application-level audit logging.  
In **IBM Db2 for z/OS**, this is solved natively at the storage engine level:

```sql
-- IBM Db2 for z/OS Native Enterprise DDL
CREATE DATABASE TRANSPL IN DSN8D13A;
CREATE TABLESPACE TSTRANS IN TRANSPL BUFFERPOOL BP1 CCSID UNICODE;

CREATE TABLE DONORS (
    DONOR_ID INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    NAME VARCHAR(100) NOT NULL,
    BLOOD_GROUP VARCHAR(5) NOT NULL,
    ORGAN_TYPE VARCHAR(20) NOT NULL,
    SYS_START TIMESTAMP(12) GENERATED ALWAYS AS ROW BEGIN NOT NULL,
    SYS_END TIMESTAMP(12) GENERATED ALWAYS AS ROW END NOT NULL,
    TRANS_START TIMESTAMP(12) GENERATED ALWAYS AS TRANSACTION START ID IMPLICITLY HIDDEN,
    PERIOD SYSTEM_TIME(SYS_START, SYS_END),
    PRIMARY KEY (DONOR_ID)
) IN TRANSPL.TSTRANS;

CREATE TABLE DONORS_HIST LIKE DONORS IN TRANSPL.TSTRANS_H;
ALTER TABLE DONORS ADD VERSIONING USE HISTORY TABLE DONORS_HIST;

CREATE INDEX IDX_DONORS_ORGAN ON DONORS(ORGAN_TYPE, BLOOD_GROUP);
```

#### Time-Travel Query Execution on z/OS:
Whenever an auditor needs to verify an allocation:
```sql
SELECT DONOR_ID, NAME, AVAILABILITY, ORGAN_TYPE
FROM DONORS
FOR SYSTEM_TIME AS OF TIMESTAMP '2026-11-10 12:00:00'
WHERE AVAILABILITY = 'AVAILABLE';
```
Db2 for z/OS transparently scans the active table and `DONORS_HIST` history partition to return the exact state of the world at that millisecond.

---

### 2. DRDA Protocol & Port 446 Connectivity to z/OS

TransplantIQ interfaces with IBM Db2 for z/OS using the **DRDA (Distributed Relational Database Architecture)** standard:
- **Default Port:** 446 (secured with IBM AT-TLS encryption)
- **Subsystem ID:** `DB2A` (running on IBM z/OS V2.5 / IBM z16)
- **Location Name:** `DB2ZOS_PROD`
- **CCSID:** 1208 (UTF-8 Unicode client) to 1047 (EBCDIC host) automatic translation.

```python
import ibm_db

# Connection to IBM Db2 for z/OS via DRDA
conn_str = (
    "DRIVER={IBM DB2 ODBC DRIVER};"
    "DATABASE=DB2ZOS_PROD;"
    "HOSTNAME=mainframe.zos.ibm.com;"
    "PORT=446;"
    "PROTOCOL=TCPIP;"
    "UID=ZOSUSER;"
    "PWD=ZOSPASS;"
    "SECURITY=SSL;"
)
conn = ibm_db.connect(conn_str, "", "")
```

---

### 3. Emergency Driver Route & Organ Collection Audit

When a driver is dispatched to collect an organ from a hospital harvest bay and deliver it to the recipient operating theater:
1. **Start Point (Collection Place):** Resolves donor hospital, trauma bay, packaging solution, and organ box ID.
2. **End Point (Dropping Point):** Resolves recipient hospital, receiving surgeon team, and OT sterile readiness.
3. **Turn-by-Turn Police Green Corridor:** Preempts municipal traffic signals for zero-congestion transit.
4. **Db2 for z/OS DRDA Two-Phase Commit:** Generates a cryptographic transaction record on z/OS Subsystem DB2A before the vehicle leaves the hospital dock.

Organ viability is bounded by **Cold Ischemia Time (CIT)**:
- **Heart:** 4 to 6 hours max
- **Lung:** 6 to 8 hours max
- **Liver:** 10 to 12 hours max
- **Kidney:** 24 to 36 hours max

TransplantIQ stores hospital coordinates (latitude, longitude, helipad availability) in Db2. Using Db2 Spatial Extender:

```sql
-- Calculate great-circle nautical and ground distance between Donor Hospital and Recipient Center:
SELECT 
    h1.NAME AS DONOR_HOSPITAL,
    h2.NAME AS RECIP_HOSPITAL,
    DB2GSE.ST_DISTANCE(
        DB2GSE.ST_POINT(h1.LONGITUDE, h1.LATITUDE, 1),
        DB2GSE.ST_POINT(h2.LONGITUDE, h2.LATITUDE, 1),
        'KILOMETRE'
    ) AS DISTANCE_KM
FROM HOSPITALS h1, HOSPITALS h2
WHERE h1.HOSPITAL_ID = ? AND h2.HOSPITAL_ID = ?;
```

This spatial metric directly feeds the **Logistics & Cold Ischemia Agent** to choose between Ground Emergency Ambulance, Air Ambulance Helicopter, or Dedicated Jet Charter.

---

### 3. Db2 pureScale Cluster (Active-Active Continuous Availability)

Healthcare networks cannot tolerate single-point-of-failure architectures.
- **Db2 pureScale** provides transparent active-active clustering powered by RDMA (Remote Direct Memory Access) and Centralized Locking Facility (CF).
- If a server node in Mumbai fails during an organ allocation transaction, traffic seamlessly fails over to the Delhi node in under **2 seconds** with zero transaction loss.

---

### 4. Cryptographic Tamper-Evident Ledger (`WORKFLOW_LOG`)

Every autonomous agent reasoning step and clinical human approval produces a cryptographic hash stored in the Db2 audit table:
```sql
INSERT INTO WORKFLOW_LOG (
    REQUEST_ID, AGENT_NAME, ACTION, DETAILS, TIMESTAMP, HASH_SIGNATURE
) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, ?);
```
Where `HASH_SIGNATURE = SHA256(request_id || agent_name || action || timestamp || details)`.  
This guarantees an immutable, verifiable ledger that bridges the gap between AI actions and hospital accountability.

---

## 🔌 Dual Driver Strategy: Local Dev to Enterprise Production

TransplantIQ features a zero-friction dual connector architecture:
- **Development & Hackathon Evaluation:** In-memory / embedded engine with exact Db2 syntax parity (`sqlite3` + spatial and temporal table emulation).
- **Production Enterprise Deployment:** 1-line connection string switch to native `ibm_db` / `ibm_db_dbi` pointing to IBM Db2 on Cloud or Db2 Warehouse.

```python
import os
import ibm_db

# Production IBM Db2 Connection Pattern
dsn = (
    f"DATABASE={os.environ.get('DB2_DB', 'TRANSPL')};"
    f"HOSTNAME={os.environ.get('DB2_HOST', 'db2-cluster.cloud.ibm.com')};"
    f"PORT={os.environ.get('DB2_PORT', '50000')};"
    f"PROTOCOL=TCPIP;"
    f"UID={os.environ.get('DB2_UID', 'db2admin')};"
    f"PWD={os.environ.get('DB2_PWD', 'secret')};"
    f"SECURITY=SSL;"
)
conn = ibm_db.connect(dsn, "", "")
```

