# Deepiri Logger

Unified, multi-language logging foundation for Deepiri services.

## Repository Layout

- `shared/`: language-agnostic logging contract
- `python/`: Python adapter (`deepiri_logger`)
- `nodejs/`: Node.js adapter (`@deepiri/logger`)
- `rust/`: Rust adapter (`deepiri_logger_rs`)

## Golden Schema

All adapters emit the same event shape:

- `timestamp`: ISO8601 timestamp
- `level`: `DEBUG|INFO|WARNING|ERROR|CRITICAL`
- `service_name`: microservice identifier
- `version`: service/application version
- `trace_id`: request trace identifier
- `message`: readable event message
- `context`: structured metadata object

Schema source of truth: `shared/schema.json`.

## PII Policy

PII masking patterns are defined in `shared/pii-patterns.yml` and should be mirrored by all adapters.

## Initial Scope

This bootstrap provides:

- shared schema and PII policy files
- Python adapter scaffold with masking and init entrypoint
- Node.js adapter scaffold with formatter and middleware
- Rust adapter scaffold with subscriber setup hooks

Service integrations are intentionally out of scope for this pitstop and should be done in follow-up PRs.

This repository is otherwise self-contained and PR-ready. After this PR lands,
the remaining work is to integrate `deepiri-logger` into downstream repos that
need it.

## Quick Start: Local Setup

### Python

```bash
cd python
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

Run the example:

```bash
cd python && python example_app.py
```

### Node.js

```bash
cd nodejs
npm install
npm run build
npm run example
```

### Rust

```bash
cd rust
cargo build
```

## Validation

Run the parity validator to check that Python and Node adapters produce compliant, masked JSON:

```bash
python3 scripts/validate_parity.py
```

Expected output: schema validation and masking checks pass for Python and Node adapters.

## Language Support

- **Python** (`python/`): mature, structlog-based with PII masking.
- **Node.js** (`nodejs/`): mature, winston-based with PII masking and Express middleware.
- **Rust** (`rust/`): scaffold, tracing-based subscriber setup.
- **C++, Ruby, Bash** (`cplusplus/`, `ruby/`, `bash/`): reference stubs.

## CI/CD

The repository includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that:
- Installs Python and Node.js dependencies.
- Builds all adapters.
- Builds the Rust adapter with `cargo build`.
- Runs the parity validator to ensure schema compliance and PII masking.

## Integration / Submodule

Recommended workflow to add `deepiri-logger` as a git submodule in a service repo:

```bash
git submodule add https://github.com/Team-Deepiri/deepiri-logger.git deps/deepiri-logger
git commit -m "Add deepiri-logger submodule"
```

Then in Python services replace local logger init with:

```python
sys.path.insert(0, 'deps/deepiri-logger/python')
from deepiri_logger import get_logger, init

init(service_name='my-service', version='1.0.0', log_file='/tmp/my-service.log')
log = get_logger(__name__)
log.info('event_name', key='value')
```

### Node.js Example

```js
const { createLogger, requestLogger } = require('./deps/deepiri-logger/nodejs/dist/index');
const logger = createLogger('my-service', '1.0.0', {
	logDir: './logs',
	enableConsole: true,
});

// Express example
app.use(requestLogger(logger));
logger.info('event_name', { key: 'value' });  // PII is auto-masked
```

## Publishing

Publishing is optional and only needed when you want to release the packages
outside this repository. It is not required for the repo itself to be PR-ready
or for later downstream integration.

If you do want to publish, use:

- **Python**: `cd python && python -m build && twine upload dist/*`
- **Node.js**: `cd nodejs && npm publish`
- **Rust**: `cd rust && cargo publish`
