import falcon
import requests
import mysql.connector

from opentelemetry import trace

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource

from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.instrumentation.mysql import MySQLInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
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
        "service.name": os.environ["SERVICE_NAME"],
        "os-version": "2025"
    }
)
provider = TracerProvider(resource=resources)
provider.add_span_processor(processor)

trace.set_tracer_provider(provider)



tracer = trace.get_tracer(os.environ["SERVICE_NAME"])

MySQLInstrumentor().instrument()
FalconInstrumentor().instrument()
# Requests package instrument
RequestsInstrumentor().instrument()

