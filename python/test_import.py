import sys

sys.path.insert(0, './python')

try:
    import deepiri_logger.config as cfg
    import deepiri_logger.processors as proc
    print('OK')
    print('config.init doc:', cfg.init.__doc__)
    print('processors public:', [name for name in dir(proc) if not name.startswith('_')])
except Exception as e:
    print('ERROR', type(e).__name__, e)
