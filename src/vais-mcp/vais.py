from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine
from google.cloud.discoveryengine_v1.services.search_service import pagers
from google.protobuf.json_format import MessageToDict

from .google_cloud import get_credentials


def _get_contents(response: pagers.SearchPager) -> list[str]:
    contents = []

    for r in response.results:
        r_dct = MessageToDict(r._pb)
        segments = r_dct["document"]["derivedStructData"]["extractive_segments"]
        for segment in segments:
            contents.append(segment["content"])

    return contents


def call_vais(
    search_query: str,
    google_cloud_project_id: str,
    vais_engine_id: str,
    vais_location: str,
    page_size: int,
    max_extractive_segment_count: int,
) -> list[str]:
    client_options = (
        ClientOptions(api_endpoint=f"{vais_location}-discoveryengine.googleapis.com")
        if vais_location != "global"
        else None
    )
    credentials = get_credentials(
        project_id=google_cloud_project_id,
    )
    client = discoveryengine.SearchServiceClient(
        credentials=credentials, client_options=client_options
    )

    serving_config = f"projects/{google_cloud_project_id}/locations/{vais_location}/collections/default_collection/engines/{vais_engine_id}/servingConfigs/default_config"

    content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
        extractive_content_spec=discoveryengine.SearchRequest.ContentSearchSpec.ExtractiveContentSpec(
            max_extractive_segment_count=max_extractive_segment_count
        )
    )

    try:
        request = discoveryengine.SearchRequest(
            serving_config=serving_config,
            query=search_query,
            page_size=page_size,
            content_search_spec=content_search_spec,
            spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
                mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
            ),
        )
    except Exception as e:
        print(f"Error: {e}")
        return None

    response = client.search(request)
    contents = _get_contents(response)
    return contents
    return contents
