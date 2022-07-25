#!/bin/bash
psql -U intranet -d delivery_app_db -c "CREATE EXTENSION IF NOT EXISTS postgis;"
