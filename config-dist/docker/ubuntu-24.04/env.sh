#!/usr/bin/env bash
set -e
docker compose -f env.yml run --rm builder

