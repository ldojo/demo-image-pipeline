import json
import unittest
from test.operators.utils import JSON_OPERATOR_METADATA_RESPONSE
import responses
from operators.metadata import OperatorMetadata

class OperatorMetadataTest(unittest.TestCase):
  def setUp(self):
    responses.add(
      responses.Response(
        method='GET',
        url='http://localhost:8081/images/operators?name=image%3Aa&name=image%3Ab',
        json=json.loads(JSON_OPERATOR_METADATA_RESPONSE)
      )
    )
    self.metadata_instance = OperatorMetadata()

  @responses.activate
  def test_get_image_operators(self):
    operators = self.metadata_instance.get_image_operators(['image:a', 'image:b'])
    self.assertDictEqual(operators, json.loads(JSON_OPERATOR_METADATA_RESPONSE))
