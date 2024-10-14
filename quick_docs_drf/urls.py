from quick_docs_drf.views import documentation_view, documentation_schema_view
from django.urls import path

quick_docs_urls = [
    path("documentation/", documentation_view, name="documentation"),
    path("quick_schema", documentation_schema_view, name="quick-schema"),
]
