"""Metadata from Operator Catalog Pipeline API Service"""
from urllib.parse import urljoin
import requests
from requests import ConnectionError as RequestConnectionError
import logging

class OperatorMetadata():
  """Wrapper class to provide the functionality"""
  def __init__(self, operator_api_service_url: str = 'http://localhost:8081'):
    self.service_url = operator_api_service_url

  def get_image_operators(self, image_names: list):
    """Make the request to API Service"""
    payload = {'name': image_names}
    try:
      req = requests.get(urljoin(self.service_url, 'image/operators'), params=payload)
      operators = req.json()
    except RequestConnectionError as err:
      logging.error('Failed to establish connection: %s', self.service_url)
      logging.debug(err)
      operators = dict()
    return operators
