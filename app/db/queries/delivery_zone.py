# flake8: noqa
"""
SQL queries related to delivery zone services
"""

INSERT_DELIVERY_ZONE_POLYGON = \
"""
INSERT INTO "delivery_zone"
    ("area")
VALUES (
    ST_GeomFromText('POLYGON(({}))')
)
RETURNING id
"""
