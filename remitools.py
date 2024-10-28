import argparse
import logging

import coloredlogs
import remi

def start(app_class: type, description: str = "My fabulous remi app", title: str|None = None):
    """Boiler plate code for bootstrapping a remi app

    Args:
        app_class (type): Your app class
        description (str, optional): Name of app, visible in the -h help and tab of the web browser. Defaults to "My fabulous remi app".
        title (str | None, optional): Optional short name to be used in the tab of the webbrowser. Defaults to None in which case `description `will be use.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-a", "--any-interface", action="store_true", default=False, help="Bind to 0.0.0.0 instead of 127.0.0.1")
    parser.add_argument("-p", "--port", type=int, default=0, help="Port to bind to (random by default)")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Enable app debug logging")
    parser.add_argument("-d", "--debug", action="store_true", default=False, help="Enable remi debug logging")
    parser.add_argument("-b", "--open-browser", action="store_true", default=False, help="Open app in browser")
    parser.add_argument("-i", "--update-interval", type=int, default=0, help="Update interval (default 0.1)")
    parser.add_argument("--user", type=str, default=None, help="User name for htaccess (default to none)")
    parser.add_argument("--password", type=str, default=None, help="Password for htaccess (default to none)")
    parser.add_argument("-m", "--multiple-instance", action="store_true", default=False, help="Allow multiple instances")

    # TODO: Handle the following parameters when the need arise
    # enable_file_cache=True
    # websocket_timeout_timer_ms=1000
    # pending_messages_queue_length=1000,
    # certfile=None,
    # keyfile=None,
    # ssl_version=None,
    # userdata=()

    args = parser.parse_args()
    if args.user != args.password:  # Hint, that is xor
        parser.error("Both user name and password must be specified")

    address: str = "0.0.0.0" if args.any_interface else "127.0.0.1"
    fmt: str = "%(asctime)s %(name)-20s [%(lineno)4d] | %(message)s"
    coloredlogs.install(level = logging.DEBUG if args.verbose else logging.INFO, fmt=fmt)
    remi.start(app_class,
                title = description if description else title,
                debug = args.debug,
                address = address,
                port = args.port,
                start_browser = args.open_browser,
                update_interval = args.update_interval,
                username=args.user,
                password=args.password,
                multiple_instance=args.multiple_instance,
            )

