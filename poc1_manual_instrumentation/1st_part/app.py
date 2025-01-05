
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter
)


processor = BatchSpanProcessor(ConsoleSpanExporter())

provider = TracerProvider()
provider.add_span_processor(processor)

trace.set_tracer_provider(provider)


tracer = trace.get_tracer("my.tracer.name")

@tracer.start_as_current_span("add function")
def add(first, second):
    return first + second


if __name__ == '__main__':
    ret = add(100, 33)
    print(f"The result is: {ret}")
