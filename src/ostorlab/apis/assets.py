"""Create Asset via an API Request."""
import json
from typing import Dict, Optional

from ostorlab.apis import request
from ostorlab.assets import asset as base_asset


class CreateAssetAPIRequest(request.APIRequest):
    """Persist asset API request"""

    def __init__(self, asset: base_asset.Asset) -> None:
        """Initializer"""
        self._asset = asset

    @property
    def query(self) -> Optional[str]:
        """Sets the query of the API request.

        Returns:
            The query to create the asset.
        """
        return """
            mutation CreateAsset($asset: AssetInputType!){
                createAsset(asset: $asset) {
                    asset{
                        ... on AndroidAssetType{
                            id
                        }
                        ... on IOSAssetType{
                            id
                        }
                        ... on AndroidFileAssetType{
                            id
                        }
                        ... on IOSFileAssetType{
                            id
                        }
                        ... on AndroidStoreAssetType{
                            id
                        }
                        ... on IOSStoreAssetType{
                            id
                        }
                        ... on UrlAssetType{
                            id
                        }
                        ... on DomainAssetType{
                            id
                        }
                        ... on SourceCodeAssetType{
                            id
                        }
                        ... on FileAssetType{
                            id
                        }
                        ... on IpAssetType{
                            id
                        }
                        ... on IpV4AssetType{
                            id
                        }
                        ... on IpV6AssetType{
                            id
                        }
                    }
                }
            }
        """

    @property
    def data(self) -> Optional[Dict]:
        """Sets the body of the API request.

        Returns:
            The body of the create asset request.
        """
        asset_type = type(self._asset).__name__

        variables = {
            'asset': {
                'tags': []
            }
        }
        asset_type_variables = self.__get_asset_variables(asset_type)
        variables['asset'].update(asset_type_variables)

        map_variables = _get_map_variables(asset_type)

        data = {
            'operations': json.dumps({'query': self.query,
                                      'variables': json.dumps(variables)}),
            'map': json.dumps(map_variables)
        }
        return data

    @property
    def files(self) -> Optional[Dict] :
        """Sets the file for multipart upload to create the asset.

        Returns:
            The file mapping of the create asset request.
        """
        asset_type = type(self._asset).__name__
        if asset_type in ('AndroidAab', 'AndroidApk', 'File', 'IOSIpa'):
            return {'0': self._asset.content}
        else:
            return None

    def __get_asset_variables(self, asset_type):
        asset_type_variables = {}
        if asset_type == 'AndroidAab' or asset_type == 'AndroidApk':
            asset_type_variables = {
                'androidFile': {
                    'file': self._asset.content
                }
            }
        elif asset_type == 'IOSIpa':
            asset_type_variables = {
                'iosFile':{
                    'file': self._asset.content
                }
            }
        elif asset_type == 'File':
            asset_type_variables = {
                'file':{
                    'content': self._asset.content,
                    'path': self._asset.path
                }
            }
        elif asset_type == 'DomainName':
            asset_type_variables = {
                'domain':{
                    'domain': self._asset.name
                }
            }
        elif asset_type == 'IP':
            asset_type_variables = {
                'ip':{
                    'host': self._asset.host,
                    'mask': self._asset.mask,
                    'version': self._asset.version
                }
            }
        elif asset_type == 'IPv4':
            asset_type_variables = {
                'ipV4':{
                    'host': self._asset.host,
                    'mask': self._asset.mask,
                    'version': self._asset.version
                }
            }
        elif asset_type == 'IPv6':
            asset_type_variables = {
                'ipV6':{
                    'host': self._asset.host,
                    'mask': self._asset.mask,
                    'version': self._asset.version
                }
            }

        return asset_type_variables

def _get_map_variables(asset_type):
    map_variables = {}
    if asset_type in ['AndroidAab', 'AndroidApk'] :
        map_variables = {
            '0': ['variables.asset.androidFile.file']
        }
    elif asset_type == 'IOSIpa':
        map_variables = {
            '0': ['variables.asset.iosFile.file']
        }
    elif asset_type == 'File':
        map_variables = {
            '0': ['variables.asset.file.content']
        }

    return map_variables
