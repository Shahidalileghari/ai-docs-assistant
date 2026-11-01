# Engineering Handbook

## Deployment review
Every production deployment must be linked to an approved pull request. The pull request must have at least one reviewer approval, passing automated tests, and a successful CI pipeline. Database migrations must be reviewed separately and include a rollback plan.

## Incident response
The on-call engineer acknowledges a production incident within ten minutes. Record the timeline, customer impact, mitigation, and follow-up actions in the incident report. Do not include secrets or personal data in incident channels.

## Backups
Production databases are backed up nightly. Restore exercises are performed quarterly. Backup access is restricted to the infrastructure team.
