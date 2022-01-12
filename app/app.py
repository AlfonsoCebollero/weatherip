import json

from requests import HTTPError
from flask import Flask
from weather_api import IPWeatherFinder
from log import log

app = Flask(__name__)


weather_api = IPWeatherFinder()
logger = log.setup_custom_logger('main')


@app.route('/weather/<string:ip>', methods=["GET"])
def get_ip_weather(ip: str):
    """

    :param ip: the ip to get the current weather from
    :return: The weather data if it is obtained
    """
    try:
        weather_api.set_ipaddress(ip)
        weather = weather_api.get_weather()
        return json.dumps(weather)
    except HTTPError as err:
        if err.response.status_code == 500:
            return 'INTERNAL SERVER ERROR'
        elif err.response.status_code == 400:
            return 'NO DATA FOUND FOR THIS IP'
        else:
            return 'BAD REQUEST'
    except KeyError:
        return 'INTERNAL SERVER ERROR'
    except ValueError as err:
        logger.error(err)
        return 'ENTER A VALID IP VALUE'
    except TypeError as err:
        logger.error(err)
        return 'BAD REQUEST'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
