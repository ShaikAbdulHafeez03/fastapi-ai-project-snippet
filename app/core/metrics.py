# from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
# from fastapi import Response

# REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'http_status'])
# REQUEST_LATENCY = Histogram('http_request_latency_seconds', 'Latency per endpoint', ['endpoint'])

# def record_request(method, endpoint, status, latency):
#     REQUEST_COUNT.labels(method=method, endpoint=endpoint, http_status=str(status)).inc()
#     REQUEST_LATENCY.labels(endpoint=endpoint).observe(latency)

# async def metrics_endpoint():
#     data = generate_latest()
#     return Response(content=data, media_type=CONTENT_TYPE_LATEST)
