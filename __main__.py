from pathlib import Path

main_py_exported = """import pulumi
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts, FetchOpts
from pulumi_kubernetes.core.v1 import Namespace

# Define namespaces
istio_ns = Namespace("istio-system", metadata={"name": "istio-system"})
grafana_ns = Namespace("grafana", metadata={"name": "grafana"})
backstage_ns = Namespace("backstage", metadata={"name": "backstage"})
ditto_ns = Namespace("eclipse-ditto", metadata={"name": "eclipse-ditto"})

# Istio
istio = Chart(
    "istio-base",
    ChartOpts(
        chart="base",
        version="1.20.1",
        fetch_opts=FetchOpts(
            repo="https://istio-release.storage.googleapis.com/charts"
        ),
        namespace=istio_ns.metadata["name"]
    )
)
pulumi.export("istio_status", "Istio chart deployed")

# Grafana
grafana = Chart(
    "grafana",
    ChartOpts(
        chart="grafana",
        version="6.58.7",
        fetch_opts=FetchOpts(
            repo="https://grafana.github.io/helm-charts"
        ),
        namespace=grafana_ns.metadata["name"]
    )
)
pulumi.export("grafana_status", "Grafana chart deployed")

# Backstage
backstage = Chart(
    "backstage",
    ChartOpts(
        chart="backstage",
        fetch_opts=FetchOpts(
            repo="https://backstage.github.io/charts"
        ),
        namespace=backstage_ns.metadata["name"]
    )
)
pulumi.export("backstage_status", "Backstage chart deployed")

# Eclipse Ditto
eclipse_ditto = Chart(
    "eclipse-ditto",
    ChartOpts(
        chart="ditto",
        fetch_opts=FetchOpts(
            repo="https://eclipse-ditto.github.io/helm-charts"
        ),
        namespace=ditto_ns.metadata["name"]
    )
)
pulumi.export("eclipse_ditto_status", "Eclipse Ditto chart deployed")
"""

Path("__main__.py").write_text(main_py_exported)
