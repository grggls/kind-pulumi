# Pulumi Kind Cluster with Istio, Backstage, Grafana, and Eclipse Ditto

This project provisions a local Kubernetes cluster using [kind](https://kind.sigs.k8s.io/) and configures it with:

- **Istio** – for service mesh, traffic management, and observability
- **Backstage** – as a developer portal and service catalog
- **Grafana** – for monitoring and observability dashboards
- **Eclipse Ditto** – as an open-source IoT framework to simulate and manage digital twins

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

### 5. Deploy with Pulumi

```bash
pulumi up
```

Pulumi will provision the cluster components: Istio, Backstage, Grafana, and Eclipse Ditto.

## Accessing Services

- **Istio Dashboard**: http://localhost:15014 (or configured port)
- **Backstage**: http://localhost:7000
- **Grafana**: http://localhost:3000
- **Eclipse Ditto**: Refer to service port mapping or UI URL after deployment

## CI/CD Pipeline

This project uses **GitHub Actions** for CI/CD automation. The workflow is defined in `.github/workflows/deploy.yml`, covering:

- Linting and formatting
- Pulumi preview and update
- Provisioning a local `kind` cluster
- Test stubs for future integration

## Cleanup

To tear down the environment:

```bash
pulumi destroy
kind delete cluster --name pulumi-kind
```

## Roadmap

- Add IoT telemetry generator and ingestion service
- Integrate Loki and Tempo for full observability stack
- Extend GitHub Actions workflow to support PR-based previews and multi-environment deployment

## License

MIT

---

This project is part of my platform engineering portfolio. Learn more: https://github.com/grggls