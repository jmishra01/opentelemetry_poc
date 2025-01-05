
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.sdk.resources import Resource

import requests
import opentelemetry.instrumentation.requests

opentelemetry.instrumentation.requests.RequestsInstrumentor().instrument()
import time

# Jaeger Address
hostname = "localhost"
port = 4317


processor = BatchSpanProcessor(
    OTLPSpanExporter(
        endpoint=f"http://{hostname}:{port}"
    )
)


resources = Resource(
    attributes={
        "service.name": "Running Addition Testing",
        "os-version": "2025",
        "cluster": "abc"
    }
)

provider = TracerProvider(resource=resources)
provider.add_span_processor(processor)

trace.set_tracer_provider(provider)


tracer = trace.get_tracer("my.tracer.name")

@tracer.start_as_current_span("running adding function")
def running_add_function(first, second):
    current_span = trace.get_current_span()
    current_span.set_status(trace.StatusCode.OK)

    current_span.set_attributes(
        attributes={
            "first-value": first,
            "second-value": second
        }
    )
    result = first + second


    current_span.add_event(
        name="running add function calculation",
        attributes={
            "first": first,
            "second": second
        },
        timestamp=time.time_ns()
    )

    time.sleep(0.1)


    current_span.add_event(
        name="running add function calculation result",
        attributes={
            "result": result
        },
        timestamp=time.time_ns()
    )

    return result


@tracer.start_as_current_span("add function")
def add(first, second):

    current_span = trace.get_current_span()
    current_span.set_status(trace.StatusCode.OK)

    current_span.set_attributes(
        attributes={
            "first-value": first,
            "second-value": second
        }
    )

    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    current_span.add_event(name="Addition Event", attributes={"first": first, "second": second}, timestamp=time.time_ns())
    for val in range(first + 1, second):
        first = running_add_function(first, val)
    current_span.add_event(name="Addition Event Result", attributes={"Result": first}, timestamp=time.time_ns())



    return first


if __name__ == '__main__':
    ret = add(100, 33)
    print(f"The result is: {ret}")
