from sqlalchemy import Table, Column, Integer, String, Numeric, Date, ForeignKey

from app.database import metadata

# This is an example of a table definition from the Automations
# process lookup table. This informs the ORM on how to interact with
# the table.
PROCESS_LK = Table(
    "PROCESS_LK",
    metadata,
    Column("PROCESS_ID", Integer, nullable=False),
    Column("PROCESS_NAME", String(100), nullable=False),
    Column("PROJECT", String(100)),
    Column("STATUS_ID", Integer),
    Column("JIRA_ID", String(20)),
    Column("OUTAGE_ID", Integer, nullable=False),
    Column("OUTAGE_COMMS", String(1)),
    Column("AUTOMATOR_ID", Integer),
)

# Table definition for customer debt information
DEBT_CUSTOMER = Table(
    "DEBT_CUSTOMER",
    metadata,
    Column("DC_ID", Integer, primary_key=True),
    Column("DATE_ADDED", Date),
    Column("LAST_UPDATED", Date),
    Column("LAST_UPDATED_BY", String(50)),
    Column("CUSTOMER_ID", Integer, nullable=False),
    Column("ACCOUNT_STATUS", String(50)),
    Column("ACCOUNT_VOID", String(4)),
    Column("ACCOUNT_TYPE", String(50)),
    Column("SUPER_CUSTOMER_ID", Integer),
    Column("CUSTOMER_NAME", String(100)),
    Column("CUSTOMER_TITLE", String(20)),
    Column("CUSTOMER_INITIAL", String(3)),
    Column("CUSTOMER_FORENAME", String(100)),
    Column("CUSTOMER_SURNAME", String(100)),
    Column("MAILING_ADDRESS", String(500)),
    Column("CUSTOMER_PHONE_NO", String(40)),
    Column("PHONE_NO_DAY", String(40)),
    Column("PHONE_NO_EVE", String(40)),
    Column("PHONE_NO_MOBILE", String(40)),
    Column("VULNERABILITY_CODES", String(80)),
    Column("VULNERABILITY_INFO", String(4000)),
    Column("CUSTOMER_EMAIL", String(200)),
    Column("FLAG_LIST", String(400)),
    Column("VAC_NO_FORWARDING", String(5)),
    schema="CBT",
)

# As a bonus, here's an example of a table definition from CRM
ENQUIRIES = Table(
    "ENQUIRIES",
    metadata,
    Column('MPANCORE', String(13), nullable=True),
    Column('RAISED_BY', String(30), nullable=True),
    Column('DATE_RAISED', Date, nullable=True),
    Column('CONTACT_TYPE', Numeric(30, 0), nullable=True),
    Column('REQUEST_TYPE', Numeric(30, 0), nullable=True),
    Column('DUE_DATE', Date, nullable=True),
    Column('COMMENTS_1', String(4000), nullable=True),
    Column('COMMENTS_2', String(4000), nullable=True),
    Column('RESOLVED', String(1), nullable=True),
    Column('RESOLVED_COMMENTS', String(4000), nullable=True),
    Column('RESOLVED_BY', String(30), nullable=True),
    Column('DATE_RESOLVED', Date, nullable=True),
    Column('OWNER', String(30), nullable=True),
    Column('ACTUAL_DATE_RAISED', Date, nullable=True),
    Column('TIMED_OUT', String(1), nullable=True),
    Column('CUSTOMER_ID', Numeric, nullable=True),
    Column('SITE_ID', Numeric, nullable=True),
    Column('RECORD_ID', Numeric, nullable=True),
    Column('SYSTEM_ROLE', String(1), nullable=True),
    Column('EXPIRY_CODE', String(1), nullable=True),
    schema="ENQUIRY",
)
