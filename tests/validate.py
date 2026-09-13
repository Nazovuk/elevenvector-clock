from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLOCK = (ROOT / ".github/workflows/football-clock.yml").read_text()
HEARTBEAT = (ROOT / ".github/workflows/keepalive.yml").read_text()
README = (ROOT / "README.md").read_text()

assert 'cron: "23 * * * *"' in CLOCK
assert 'cron: "41 3 1,15 * *"' in HEARTBEAT
assert "runs-on: ubuntu-latest" in CLOCK
assert "permissions: {}" in CLOCK
assert "contents: write" in HEARTBEAT
assert "https://elevenvector.vercel.app/api/cron/football" in CLOCK
assert "X-Football-Expected-SHA" in CLOCK
assert "github-public-schedule" in CLOCK
assert "FOOTBALL_CRON_SECRET" in CLOCK
assert "FOOTBALL_CRON_SECRET" not in HEARTBEAT
assert "Authorization" in CLOCK
assert '"Authorization"' not in README
assert "uses:" not in CLOCK + HEARTBEAT
assert "workflow_dispatch" not in CLOCK + HEARTBEAT
assert "pull_request" not in CLOCK + HEARTBEAT
assert "repository_dispatch" not in CLOCK + HEARTBEAT
assert "artifact" not in CLOCK.lower() + HEARTBEAT.lower()
assert "cache" not in CLOCK.lower() + HEARTBEAT.lower()
assert "curl" not in CLOCK
assert "print(raw" not in CLOCK
assert "print(secret" not in CLOCK
assert "github.token" in HEARTBEAT
assert "[skip ci]" in HEARTBEAT
assert "push:" not in CLOCK + HEARTBEAT

print("PUBLIC_CLOCK_PROTOTYPE_VALIDATION=PASS")
