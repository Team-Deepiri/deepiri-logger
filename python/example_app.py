import sys

sys.path.insert(0, './python')

from deepiri_logger import get_logger, init


def main():
    init(service_name="diri-cyrex", version="0.0.1")
    log = get_logger()
    log.info("User login attempt", user="alice@example.com", api_key="sk_test_12345", extra={"note": "sensitive: token=abcd"})


if __name__ == '__main__':
    main()
