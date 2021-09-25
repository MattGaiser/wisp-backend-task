from flask import Blueprint, jsonify
from functools import lru_cache

# Normally the prefix would be '/api', but that was not what you specified
bp = Blueprint('api', __name__, url_prefix='')


@lru_cache(maxsize=None)
def special_math(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + special_math(n - 1) + special_math(n - 2)


@bp.route('/health')
def ping():
    data = {'success': True}
    return jsonify(data), 200


@bp.route('/specialmath', defaults={'math_input': None})
# Int can also be enforced here, but I wanted to write a custom error message instead
@bp.route('/specialmath/<math_input>')
def specialmath(math_input):
    if math_input is None:
        return jsonify({"error": "A value is needed to perform the special math calculation"}), 400
    elif not math_input.isdigit():
        return jsonify({"error": "An invalid value was provided for the special math calculation"}), 422

    return jsonify({"result": special_math(int(math_input))})
