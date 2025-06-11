# Incident Runbook: EC2 High CPU Utilization

## Overview
This runbook outlines steps to diagnose and remediate high CPU utilization on EC2 instances monitored by CloudWatch.

## Symptoms
- CloudWatch alarm triggers when CPU utilization > 80% for 2 consecutive periods.
- Notifications sent via SNS, triggering Lambda function to reboot instance.

## Immediate Actions
1. Confirm alarm status in CloudWatch console.
2. Review instance metrics for CPU spikes and related logs.
3. Check running processes on the instance to identify CPU-consuming tasks.

## Automated Remediation
- Lambda function automatically reboots the instance when alarm triggers.

## Manual Remediation Steps (if automation fails)
1. Log in to the instance via SSH.
2. Run `top` or `htop` to identify resource hogs.
3. Restart or kill problematic processes.
4. Review application logs for errors or infinite loops.
5. Consider scaling vertically or horizontally if high CPU persists.

## Post-Incident Actions
- Analyze root cause.
- Update scripts or application code if needed.
- Adjust CloudWatch alarm thresholds if appropriate.
- Document findings and update runbook.

## Contacts
- Cloud Operations Team: ops-team@example.com
- On-call engineer: oncall@example.com

## Notes
- Ensure IAM roles have appropriate permissions for remediation.
- Monitor for recurring alarms to prevent alert fatigue.
