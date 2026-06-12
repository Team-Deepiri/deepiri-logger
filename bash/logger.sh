#!/usr/bin/env bash
ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
cat <<JSON
{"timestamp":"$ts","level":"INFO","service_name":"bash-service","version":"0.0.1","trace_id":"stub","message":"hello from bash","context":{}}
JSON
