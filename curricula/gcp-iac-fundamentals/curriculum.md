---
title: Learning GCP Infrastructure as Code — Interactive Curriculum
tags: [gcp, iac, infrastructure-as-code, terraform, deployment-manager, cloud-build]
updated: 2025-08-09
---

## How to Use This Curriculum

**Follow these steps for each phase:**

1. **📖 Read** the Core Ideas to build foundational knowledge
2. **🤖 Ask the AI Teacher** using the copy-paste prompts provided
3. **✏️ Do the Activity** (planning/design only, no coding)
4. **🤔 Reflect** using the template questions
5. **✅ Check** your understanding against success criteria

**Time commitment:** 20-30 minutes per phase • Work at your own pace • Use any AI assistant

---

## Overview

This curriculum teaches Infrastructure as Code fundamentals on Google Cloud Platform, covering core GCP services, automation tools, and production deployment strategies for beginners.

## Learning Outcomes

- Explain Infrastructure as Code (IaC) concepts and benefits in Google Cloud Platform
- Identify and describe core GCP building blocks including Projects, IAM, VPC, Compute, and Storage services
- Compare Deployment Manager and Terraform for GCP infrastructure automation
- Design an automated CI/CD workflow using Google Cloud Build for infrastructure deployment
- Create a comprehensive deployment plan for a small, production-ready GCP environment

---

## Phase 1 — Understanding Infrastructure as Code Fundamentals

**Estimated time:** 25 minutes
**Goal:** Understand what Infrastructure as Code means and why it's valuable for cloud deployments.

### Phase 1 Core Ideas

- Infrastructure as Code (IaC) treats infrastructure like software - versioned, tested, and automated
- IaC eliminates manual configuration drift and enables consistent, repeatable deployments
- Google Cloud provides native tools and supports third-party IaC solutions
- IaC enables faster scaling, better disaster recovery, and improved compliance
- Version control for infrastructure allows rollbacks and change tracking

### Phase 1 Ask the AI Teacher

**Copy this prompt to your AI assistant:**

> You are an expert in Google Cloud Platform and Infrastructure as Code. I'm learning about IaC fundamentals as part of a structured curriculum.
>
> Please help me understand: What are the main benefits of using Infrastructure as Code compared to manual cloud resource management?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

**Copy this prompt to your AI assistant:**

> You are an expert in cloud infrastructure and DevOps practices. I'm learning about Infrastructure as Code fundamentals.
>
> Please help me understand: How does IaC help with compliance and security in cloud environments?
>
> Provide specific examples and ask me a follow-up question to test my comprehension.

### Phase 1 Activity (no code)

Create a comparison table listing 5 manual infrastructure management tasks versus their IaC equivalents. Include time estimates and risk factors for each approach.

**What Good Looks Like:**

- Clear before/after scenarios (e.g., "Manual: SSH into 10 servers to update config" vs "IaC: Update config file, run deployment")
- Realistic time estimates based on team size
- Risk assessment includes human error, consistency, and rollback capabilities

### Phase 1 Reflect

**Template:** Fill in your answers:

- What manual infrastructure tasks in your current or past experience could benefit most from automation?
- What concerns do you have about treating infrastructure like code?
- What would convince your team to adopt IaC practices?

**Success Criteria:** You can explain IaC benefits and identify 3+ manual tasks that could be automated.

---

## Phase 2 — Exploring GCP Core Building Blocks

**Estimated time:** 25 minutes
**Goal:** Identify and understand the fundamental GCP services that form the foundation of most cloud architectures.

### Phase 2 Core Ideas

- GCP Projects provide organizational boundaries and resource isolation
- Identity and Access Management (IAM) controls who can access what resources
- Virtual Private Cloud (VPC) creates secure network environments
- Compute services (Compute Engine, GKE, Cloud Run) run your applications
- Storage services (Cloud Storage, Cloud SQL, Firestore) persist your data

### Phase 2 Ask the AI Teacher

**Copy this prompt to your AI assistant:**

> You are an expert in Google Cloud Platform architecture. I'm learning about GCP core building blocks as part of a structured curriculum.
>
> Please help me understand: How do GCP Projects, folders, and organizations work together to structure cloud resources?
>
> Provide a clear explanation with a practical example, and ask me a follow-up question to check my understanding.

**Copy this prompt to your AI assistant:**

> You are a GCP solutions architect. I'm learning about fundamental GCP services.
>
> Please help me understand: When should I use Compute Engine versus Cloud Run versus Google Kubernetes Engine?
>
> Give me decision criteria with examples, and ask me a scenario-based question to test my understanding.

### Phase 2 Activity (no code)

Design a simple three-tier web application architecture on GCP. Sketch out which GCP services you'd use for the web layer, application layer, and database layer, including networking and security considerations.

**What Good Looks Like:**

- Clear separation of concerns (web/app/data layers)
- Appropriate GCP service selection with justification
- Basic security considerations (IAM, VPC, firewalls)
- Scalability considerations for each layer

### Phase 2 Reflect

**Template:** Fill in your answers:

- Which GCP building block seems most complex to you, and what specific aspect would you want to learn more about?
- How would you explain the relationship between Projects, IAM, and VPC to a colleague?
- What questions would you ask when designing a new GCP architecture?

**Success Criteria:** You can identify appropriate GCP services for common use cases and explain their relationships.

---

## Phase 3 — Comparing IaC Tools: Deployment Manager vs Terraform

**Estimated time:** 25-30 minutes
**Goal:** Understand the strengths and use cases of GCP's native Deployment Manager versus the popular third-party tool Terraform.

### Phase 3 Core Ideas

- Deployment Manager is GCP's native IaC tool with deep Google Cloud integration
- Terraform is a multi-cloud IaC tool that supports GCP and many other providers
- Both tools use declarative configuration files to define desired infrastructure state
- Deployment Manager uses YAML/Jinja2 templates, Terraform uses HCL (HashiCorp Configuration Language)
- Tool choice depends on team skills, multi-cloud needs, and ecosystem preferences

### Phase 3 Ask the AI Teacher

**Copy this prompt to your AI assistant:**

> You are an expert in Infrastructure as Code tools, specifically Google Cloud Deployment Manager and Terraform. I'm learning about IaC tool comparison.
>
> Please help me understand: What are the key advantages of using Deployment Manager for GCP-only infrastructure?
>
> Provide specific examples and ask me a follow-up question about tool selection criteria.

**Copy this prompt to your AI assistant:**

> You are a DevOps engineer experienced with both Deployment Manager and Terraform. I'm comparing IaC tools.
>
> Please help me understand: In what scenarios would Terraform be a better choice than Deployment Manager?
>
> Give me decision criteria with real-world examples, and ask me a scenario-based question.

### Phase 3 Activity (no code)

Create a decision matrix comparing Deployment Manager and Terraform across 6 factors: learning curve, GCP integration, multi-cloud support, community resources, enterprise features, and maintenance overhead. Rate each tool 1-5 for each factor.

**What Good Looks Like:**

- Objective evaluation based on research, not bias
- Clear rating criteria (what does "5" mean for each factor?)
- Consideration of different team contexts and requirements
- Acknowledgment of trade-offs rather than declaring a "winner"

### Phase 3 Reflect

**Template:** Fill in your answers:

- Based on your current team's skills and infrastructure needs, which tool would you recommend and why?
- What additional factors would influence your decision in a real project?
- How would you approach learning whichever tool you didn't choose?

**Success Criteria:** You can articulate the trade-offs between tools and make a reasoned recommendation for a specific context.

---

## Phase 4 — Building Automated Workflows with Cloud Build

**Estimated time:** 25 minutes
**Goal:** Design CI/CD pipelines that automatically deploy infrastructure changes using Cloud Build.

### Phase 4 Core Ideas

- Cloud Build automates infrastructure deployment triggered by code changes
- Build triggers can respond to Git commits, pull requests, or manual execution
- Cloud Build can execute both Deployment Manager and Terraform deployments
- Pipeline stages typically include validation, planning, approval, and deployment
- Integration with Cloud Source Repositories, GitHub, and Bitbucket enables GitOps workflows

### Phase 4 Ask the AI Teacher

**Copy this prompt to your AI assistant:**

> You are an expert in Google Cloud Build and CI/CD pipelines for infrastructure. I'm learning about automated infrastructure workflows.
>
> Please help me understand: How would you set up a Cloud Build pipeline that requires manual approval before deploying to production?
>
> Provide a step-by-step approach with practical considerations, and ask me about pipeline security.

**Copy this prompt to your AI assistant:**

> You are a DevOps engineer specializing in GitOps and infrastructure automation. I'm learning about Cloud Build workflows.
>
> Please help me understand: What are the security best practices for managing service account permissions in Cloud Build?
>
> Give me specific recommendations with examples, and ask me about potential security risks.

### Phase 4 Activity (no code)

Design a complete CI/CD workflow for infrastructure deployment. Map out the stages from developer commit to production deployment, including validation steps, approval gates, and rollback procedures.

**What Good Looks Like:**

- Clear workflow diagram with decision points
- Appropriate validation steps (syntax, security, cost estimation)
- Manual approval gates for production changes
- Rollback strategy and monitoring integration
- Consideration of different environments (dev/staging/prod)

### Phase 4 Reflect

**Template:** Fill in your answers:

- What potential risks do you see with automated infrastructure deployment, and how would you mitigate them?
- How would you balance automation speed with safety controls?
- What metrics would you track to measure pipeline effectiveness?

**Success Criteria:** You can design a secure, automated deployment pipeline with appropriate safety controls.

---

## Phase 5 — Designing Production-Ready Deployment Strategies

**Estimated time:** 30 minutes
**Goal:** Plan comprehensive deployment strategies that address scalability, security, disaster recovery, and operational requirements.

### Phase 5 Core Ideas

- Production deployments require multiple environments (dev, staging, production)
- Infrastructure should be designed for high availability and disaster recovery
- Security considerations include network isolation, encryption, and access controls
- Monitoring and logging must be built into the infrastructure from day one
- Cost optimization through right-sizing, scheduling, and resource lifecycle management

### Phase 5 Ask the AI Teacher

**Copy this prompt to your AI assistant:**

> You are a senior cloud architect specializing in production-ready GCP deployments. I'm learning about production deployment strategies.
>
> Please help me understand: What are the essential components of a production-ready GCP architecture for a web application?
>
> Provide a comprehensive checklist with priorities, and ask me about disaster recovery planning.

**Copy this prompt to your AI assistant:**

> You are an expert in cloud operations and disaster recovery. I'm learning about production readiness.
>
> Please help me understand: How would you design a disaster recovery strategy for a GCP-based application?
>
> Give me specific approaches with trade-offs, and ask me about recovery time objectives.

### Phase 5 Activity (no code)

Create a production readiness checklist for a small startup's GCP infrastructure. Include sections for security, scalability, disaster recovery, monitoring, and cost optimization. Prioritize items as "must-have," "should-have," or "nice-to-have."

**What Good Looks Like:**

- Comprehensive coverage of operational concerns
- Realistic prioritization based on startup constraints
- Specific, actionable items rather than vague goals
- Consideration of both technical and business requirements
- Balance between robustness and complexity

### Phase 5 Reflect

**Template:** Fill in your answers:

- What aspect of production infrastructure deployment concerns you most, and what would you need to learn to feel confident about it?
- How would you approach convincing stakeholders to invest in "invisible" infrastructure improvements?
- What would your 30-60-90 day plan look like for improving production readiness?

**Success Criteria:** You can create a comprehensive production readiness plan with appropriate prioritization.

---

## Final Project

Choose one capstone project that synthesizes your learning across all phases:

### Option 1: Infrastructure Blueprint

Design a complete infrastructure blueprint for a three-tier web application on GCP, including networking, security, compute, and storage components with detailed deployment planning.

### Option 2: Migration Strategy Document

Create a comprehensive comparison matrix and migration strategy document for moving from manual infrastructure management to automated IaC workflows on GCP.

### Option 3: Production Readiness Plan

Develop a production readiness checklist and deployment timeline for a small startup's GCP infrastructure, including disaster recovery and scaling considerations.

### Deliverables

- Short write-up (1-2 pages) with an architecture diagram or process flow
- List of GCP services, tools, and decisions with justifications
- Three key lessons learned and next steps for implementation
