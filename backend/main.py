from http import HTTPStatus
import json

from flask import Flask, request
from schematics.exceptions import DataError, ValidationError
from schematics.models import Model
from schematics.types import DateTimeType, IntType, StringType


class LoggingInfo(Model):
    id = IntType(required=True)
    userId = StringType(required=True)
    actionType = StringType(required=True)
    timestamp = DateTimeType(required=True)
    extra = StringType(required=False)


app = Flask(__name__)

@app.route('/log', methods=['POST'])
def receive_log():
    try:
        log_data = LoggingInfo(request.json)
        log_data.validate()
    except (ValidationError, DataError) as data_exception:
        return {'error': json.loads(str(data_exception))}, HTTPStatus.BAD_REQUEST
    print(log_data.to_primitive())
    return '{"message": "Logged successfully"}'


