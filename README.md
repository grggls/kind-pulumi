# Pulumi Kind Cluster with Istio, Backstage, Grafana, and Eclipse Hono

This project provisions a local Kubernetes cluster using [kind](https://kind.sigs.k8s.io/) and configures it with:

- **Istio** – for service mesh, traffic management, and observability
- **Backstage** – as a developer portal and service catalog
- **Grafana** – for monitoring and observability dashboards
- **Eclipse Hono** – a messaging framework for scalable IoT device communication

Provisioning and deployment are managed using [Pulumi](https://www.pulumi.com/) with the Python SDK.

## Goals

- Demonstrate infrastructure-as-code best practices with Pulumi
- Build a local developer experience stack aligned with SPAN’s platform engineering vision
- Simulate a microservices + IoT environment with integrated observability and developer tooling

## Prerequisites

- [Docker](https://www.docker.com/)
- [Pulumi](https://www.pulumi.com/docs/get-started/install/)
- [Python 3.8+](https://www.python.org/)
- [kind](https://kind.sigs.k8s.io/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/) (optional, depending on how services are installed)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/grggls/kind-pulumi.git
cd kind-pulumi
```

### 2. Set up a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a kind cluster

```bash
kind create cluster --name pulumi-kind
```

> Optional: Use a custom configuration in `kind-config.yaml` if needed.

### 5. Configure Pulumi for local usage

To avoid being prompted for a passphrase:

#### For Bash/Zsh:

```bash
export PULUMI_BACKEND_URL=file://$HOME/.pulumi
export PULUMI_CONFIG_PASSPHRASE=notasecret
```

Add these to your `~/.bashrc` or `~/.zshrc` to make them persistent.

#### For Fish shell:

```fish
set -Ux PULUMI_BACKEND_URL file://$HOME/.pulumi
set -Ux PULUMI_CONFIG_PASSPHRASE notasecret
```

### 6. Initialize Pulumi stack and deploy

```bash
pulumi login --local
pulumi stack init dev  # Run only once
pulumi up --yes
```

Pulumi will provision the cluster components: Istio, Backstage, Grafana, and Eclipse Hono.

## Accessing Services

- **Istio Dashboard**: http://localhost:15014 (or configured port)
- **Backstage**: http://localhost:7000
- **Grafana**: http://localhost:3000
- **Eclipse Hono**: Refer to service port mapping or UI URL after deployment

## CI/CD Pipeline

This project uses **GitHub Actions** for CI/CD automation. The workflow is defined in:

- `.github/workflows/deploy.yml`: for provisioning with Pulumi
- `.github/workflows/test.yml`: for verifying that services are accessible and running correctly

## Pre-commit Hooks

This project uses [pre-commit](https://pre-commit.com/) to enforce consistent code quality and syntax.

### Setup

1. Install pre-commit and related tools:

```bash
pip install pre-commit black isort flake8
```

2. Install pre-commit hooks:

```bash
pre-commit install
```

3. Run manually (optional):

```bash
pre-commit run --all-files
```

## Cleanup

To tear down the environment:

```bash
pulumi destroy
kind delete cluster --name pulumi-kind
```

## Roadmap

- Add IoT telemetry generator and ingestion service
- Integrate Loki and Tempo for full observability stack
- Extend GitHub Actions workflows for multi-environment support and service-level validation

## License

MIT

---

This project is part of my platform engineering portfolio. Learn more: https://github.com/grggls
