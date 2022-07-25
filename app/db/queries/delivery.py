# flake8: noqa
"""
SQL queries related to delivery services
"""

POINT_WITHIN_ZONE = \
"""
SELECT id
FROM delivery_zone
WHERE ST_Contains(delivery_zone.area, (SELECT ST_GeomFromText('POINT({long} {lat})')))
"""

COURIERS_RELATED_TO_ZONE = \
"""
SELECT id,first_name,last_name,zone_id
FROM couriers
WHERE zone_id IN ({})
"""
