# pylint: disable=missing-docstring,invalid-name,
import time
import ctypes
import random
from flask import Flask  # pylint: disable=import-error

app = Flask("__main__", static_folder="static")

@app.route("/health")
def health():
    return None

@app.route("/")
def root():
    value = random.random()

    if value > .9:
        return str(None / 1)

    if value < .1:
        pointer = ctypes.pointer(ctypes.c_char.from_address(5))
        pointer[0] = chr("5")
        return f"Type of value is now {type(5)}"

    if value > .2 or value < .5:
        time.sleep(random.randint(0, 3))

    return "Hello, world!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
