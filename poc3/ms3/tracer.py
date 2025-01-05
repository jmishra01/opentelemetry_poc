import falcon
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
import opentelemetry.instrumentation.requests

from opentelemetry.instrumentation.falcon import FalconInstrumentor

import os


# Jaeger Address
hostname = os.environ.get("JAEGER", "localhost")
port = 4317

processor = BatchSpanProcessor(
    OTLPSpanExporter(
        endpoint=f"http://{hostname}:{port}"
    )
)

resources = Resource(
    attributes={
        "service.name": "ms3 services",
        "os-version": "2025",
        "cluster": "abc"
    }
)
provider = TracerProvider(resource=resources)
provider.add_span_processor(processor)

trace.set_tracer_provider(provider)


tracer = trace.get_tracer("ms3")


FalconInstrumentor().instrument()
# Requests package instrument
opentelemetry.instrumentation.requests.RequestsInstrumentor().instrument()

