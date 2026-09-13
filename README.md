# ElevenVector clock

This public repository supplies only an hourly clock for the canonical production
scheduler. It contains no ElevenVector source, data, database credentials, provider
credentials, or business logic.

Repository configuration:

- encrypted Actions secret `FOOTBALL_CRON_SECRET`
- non-secret Actions variable `ELEVENVECTOR_PRODUCTION_SHA`, set to the exact active
  40-character production commit
- standard GitHub-hosted Ubuntu runners only

The invocation workflow has no manual, pull-request, issue, or dispatch trigger. It
targets one hardcoded HTTPS endpoint, sends the secret only as an Authorization header,
and logs only an allowlisted receipt. The endpoint rejects a missing, malformed, or
stale expected production SHA before database access.

The twice-monthly heartbeat makes a small default-branch commit using the repository's
ephemeral `GITHUB_TOKEN`. It does not receive the scheduler secret and cannot invoke the
production endpoint. Pushes made with `GITHUB_TOKEN` do not trigger additional workflow
runs, and neither workflow defines a push trigger.

Production activation is a separate governed operation. Disable the private clock
before enabling this schedule, update the expected SHA on each production release, and
observe two genuine schedule events before retiring the previous clock.

