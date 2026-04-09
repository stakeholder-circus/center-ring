# Security baseline

Default branch policy for live public repositories:

- pull requests required before merge
- required status checks
- conversation resolution
- signed commits
- linear history
- no force pushes
- no branch deletion
- squash merge only

Local baseline:

- SSH commit signing
- core.hooksPath=.githooks
- provenance trailers on commits
- least-privilege GitHub Actions permissions
