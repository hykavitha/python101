class _Timer(object):
    """Timer for diagnostic timing"""
    def __enter__(self):
        self._start = timer()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end = timer()

    def elapsed(self):
        elapsed = self._end - self._start
        # start with μs
        elapsed = elapsed * 1000000
        unit = "μs"
        if elapsed > 1000:
            # switch to ms
            elapsed = elapsed / 1000
            unit = "ms"
        return "{:.3f} {}".format(float(elapsed), unit)
