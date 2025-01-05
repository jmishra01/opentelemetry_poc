
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

from opentelemetry.sdk.resources import Resource

import time

resources = Resource(
    attributes={
        "service.name": "MyLaptop",
        "os-version": "2025",
        "cluster": "abc"
    }
)


processor = BatchSpanProcessor(ConsoleSpanExporter())

provider = TracerProvider(resource=resources)
provider.add_span_processor(processor)

trace.set_tracer_provider(provider)


tracer = trace.get_tracer("my.tracer.name")

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

    time.sleep(1)

    current_span.add_event(name="myEventAddFunction", attributes={"foo": "bar", "process": "complete"},
                           timestamp=time.time_ns())
    return first + second


if __name__ == '__main__':
    ret = add(100, 33)
    print(f"The result is: {ret}")
