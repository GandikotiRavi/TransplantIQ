# IBM Db2 Connector Notes

## Recommended driver

```bash
pip install ibm_db ibm_db_dbi
```

## Example connection (production)

```python
import ibm_db
import os

dsn = (
    f"DATABASE={os.environ['DB2_DATABASE']};"
    f"HOSTNAME={os.environ['DB2_HOST']};"
    f"PORT={os.environ.get('DB2_PORT', '50000')};"
    f"PROTOCOL=TCPIP;"
    f"UID={os.environ['DB2_USER']};"
    f"PWD={os.environ['DB2_PASSWORD']};"
)

conn = ibm_db.connect(dsn, "", "")

# Parameterized query (always use parameters – never string concatenation)
sql = "SELECT donor_id, blood_group, organ_type FROM donors WHERE availability = ?"
stmt = ibm_db.prepare(conn, sql)
ibm_db.execute(stmt, ("AVAILABLE",))

row = ibm_db.fetch_assoc(stmt)
while row:
    print(row)
    row = ibm_db.fetch_assoc(stmt)

ibm_db.close(conn)
```

## Mapping from the prototype

| Prototype (SQLite) | Production (Db2) |
|--------------------|------------------|
| `sqlite3` + `db.py` helpers | `ibm_db` / `ibm_db_dbi` |
| `/tmp/transplantiq.db` | Db2 database / schema |
| Same table & column names | Same DDL (minor type differences only) |

The agent code never issues raw SQL; it always goes through the data-access helpers in `db.py`.  
Replacing those helpers with `ibm_db` equivalents is the only change required for a full Db2 backend.
