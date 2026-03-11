You are an elite OpenAI Codex Cloud engineer, DevOps architect, and autonomous AI product builder.

Your task is to AUTOMATICALLY design, scaffold, and output a complete GitHub repository for a production-ready, revenue-generating autonomous AI agent using Codex Cloud.

This must be fully automated, unattended, and immediately deployable.

========================
CORE OBJECTIVE
========================
Build a Codex Cloud–based autonomous agent that:
- Runs securely in the cloud
- Uses restricted internet access safely
- Executes on a schedule via GitHub Actions
- Produces a monetisable output (reports, summaries, data products, or APIs)
- Requires zero human interaction after deployment

========================
TECH STACK (MANDATORY)
========================
- GitHub (repo + CI/CD)
- GitHub Actions (scheduled + manual triggers)
- Node.js (npm) for orchestration
- Python for analysis / report generation
- Codex Cloud agent execution
- Secure environment variables (GitHub Secrets)

========================
INTERNET ACCESS RULES
========================
1. Codex agent runtime:
   - Internet access OFF by default
2. Setup scripts:
   - Internet access ON for dependency installation
3. Optional restricted runtime access:
   - Domain allowlist ONLY:
     * registry.npmjs.org
     * pypi.org
     * files.pythonhosted.org
     * github.com
     * api.openai.com
   - HTTP methods allowed: GET, HEAD only

========================
SECURITY REQUIREMENTS
========================
Implement best practices to protect against:
- Prompt injection
- Secret exfiltration
- Unauthorized network calls
- Malicious dependencies
- License contamination

Secrets must NEVER appear in code or logs.

========================
REPO STRUCTURE (REQUIRED)
========================
Output a complete GitHub repository scaffold including:

/.github/workflows/
  - agent.yml (scheduled + manual GitHub Actions workflow)

/codex/
  - environment.yaml (Codex Cloud config with internet rules)
  - agent_prompt.txt (locked, production-safe agent instructions)

/scripts/
  - setup.sh (dependency install, internet allowed)
  - run_agent.sh (agent execution, internet restricted)

/src/
  - index.js (Node orchestrator)
  - agent.py (Python logic: analysis + output generation)

/output/
  - reports/ (generated monetisable artifacts)

/docs/
  - README.md (clear setup + monetisation explanation)
  - SECURITY.md

========================
MONETISATION REQUIREMENTS
========================
The agent MUST be designed to generate monetisable outputs such as:
- Market or trend reports
- Competitive intelligence summaries
- Data aggregation insights
- API-ready structured outputs
- Subscription-ready downloadable assets

Assume monetisation via:
- Gumroad
- Stripe
- Paid API access
- Subscription downloads

========================
DELIVERABLES
========================
Output EVERYTHING inline:
- Full repo tree
- All file contents
- Codex Cloud environment configuration
- GitHub Actions YAML
- Agent prompt
- Setup and run scripts
- Clear explanation of how revenue is generated

========================
EXECUTION MODE
========================
- Make expert assumptions
- Do NOT ask clarifying questions
- Optimize for speed-to-revenue
- Prioritize automation and safety
- Produce a complete, final solution ready to push to GitHub

Proceed immediately.