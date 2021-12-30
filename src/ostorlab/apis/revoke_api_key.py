"""Revokes the API key.
"""

from ostorlab.apis import request
from typing import Dict, Optional
import json
import logging

logger = logging.getLogger(__name__)


class RevokeAPIKeyAPIRequest(request.APIRequest):
    """Revokes the API key.
    """

    def __init__(self, api_key_id: str):
        """Constructs all the necessary attributes for the object.

        Args:
           api_key_id: The API key id used to revoke the API key.
        """
        self._api_key_id = api_key_id

    @property
    def query(self) -> Optional[str]:
        """Defines the query to revoke the API key.

        Returns:
            The query to revoke the API key
        """
        return """
         mutation RevokeApiKey($apiKeyId: String!) {
               revokeApiKey(apiKeyId: $apiKeyId) {
                  result
               }
            }
        """

    @property
    def endpoint(self):
        return request.AUTHENTICATED_GRAPHQL_ENDPOINT

    @property
    def data(self) -> Optional[Dict]:
        """Sets the query and variables to revoke the API key.

        Returns:
              The query and variables to revoke the API key.
        """
        data = {
            'query': self.query,
            'variables': json.dumps({'apiKeyId': self._api_key_id})
        }
        return data
