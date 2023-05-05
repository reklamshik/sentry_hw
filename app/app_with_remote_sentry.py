from flask import Flask, request, jsonify
from loguru import logger
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://09d1c33ac877406ca6b78ce56121fb2b@o4505052612984832.ingest.sentry.io/4505085755654144",
    integrations=[FlaskIntegration()],
    
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)


@app.route('/division', methods=['GET'])
def check_division():
    first_num = request.args.get('first')
    second_num = request.args.get('second')
    if second_num == '0':
        raise ZeroDivisionError
    
    result = float(first_num) / float(second_num)
    logger.info(result)
    
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
