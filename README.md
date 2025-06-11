# cloud-monitoring-automation-pipeline
This project simulates a production cloud environment and demonstrates how to monitor AWS infrastructure, respond to incidents automatically, and implement operational controls using AWS services.
Objectives

Configure system monitoring for EC2 instances

Trigger alerts using Amazon CloudWatch and SNS

Implement auto-remediation using AWS Lambda

Provision infrastructure using Terraform (optional step)

Follow IAM best practices for secure automation

Document incident response and operational runbooks

Architecture

EC2 Instance --> CloudWatch Alarm --> SNS Topic --> Lambda Function --> Auto Remediation

Technologies

AWS EC2 – Simulated application instance

AWS CloudWatch – Performance monitoring (CPU threshold alerts)

Amazon SNS – Notification service for alert delivery

AWS Lambda – Remediation logic (e.g., restart EC2 instance)

IAM – Role-based access for automation services

Terraform – (Optional) Infrastructure as Code

Python – Lambda function logic

Features

1. EC2 Setup

Launch a t2.micro EC2 instance with Amazon Linux 2

Install a sample workload (e.g., CPU stress script)

2. CloudWatch Alarm

Set a CPU utilization threshold at 80%

Alarm sends message to SNS topic

3. SNS + Lambda Integration

SNS triggers Lambda

Lambda uses AWS SDK (boto3) to reboot the instance

4. IAM Roles & Policies

Create execution roles for Lambda with least-privilege permissions

Allow SNS to invoke Lambda securely

5. Terraform IaC (Optional)

Automate provisioning of EC2, IAM, CloudWatch, SNS, and Lambda

6. Documentation

Markdown-based runbooks for incident resolution

Comments in code for clarity and maintainability

Repository Structure

📁 /cloud-monitoring-pipeline
├── terraform/                # IaC files (optional)
├── lambda/                   # Python scripts
│   └── auto_remediate.py
├── runbooks/                # Markdown runbooks
│   └── EC2-CPU-High.md
├── screenshots/             # Monitoring dashboard samples
├── README.md

Getting Started

Clone the repo: git clone https://github.com/Blein7/cloud-monitoring-pipeline

Deploy EC2 manually or via Terraform

Set CloudWatch alarm

Subscribe Lambda to SNS

Simulate high CPU load to test alerting and auto-remediation
