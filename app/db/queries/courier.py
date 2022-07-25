# flake8: noqa
"""
SQL queries related to courier services
"""

INSERT_COURIER = \
"""
INSERT INTO "couriers"
    ("first_name", "last_name", "zone_id")
VALUES (
    '{first_name}', '{last_name}', '{zone_id}'
)
RETURNING id, first_name, last_name, zone_id;
"""
