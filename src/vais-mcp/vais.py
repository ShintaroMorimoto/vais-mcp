from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine


def call_vais(
    search_query: str,
    google_cloud_project_id: str,
    vais_engine_id: str,
    vais_location: str,
    page_size: int,
    max_extractive_segment_count: int,
) -> discoveryengine.SearchResponse:
    client_options = (
        ClientOptions(api_endpoint=f"{vais_location}-discoveryengine.googleapis.com")
        if vais_location != "global"
        else None
    )

    client = discoveryengine.SearchServiceClient(client_options=client_options)
    serving_config = f"projects/{google_cloud_project_id}/locations/{vais_location}/collections/default_collection/engines/{vais_engine_id}/servingConfigs/default_config"

    content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
        extractive_content_spec=discoveryengine.SearchRequest.ContentSearchSpec.ExtractiveContentSpec(
            max_extractive_segment_count=max_extractive_segment_count
        )
    )

    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=search_query,
        page_size=page_size,
        content_search_spec=content_search_spec,
        spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
            mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
        ),
    )

    response = client.search(request)
    return response
