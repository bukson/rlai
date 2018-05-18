import cProfile
import io
import pstats


class SimpleProfiler:

    def __init__(self):
        self.pr = cProfile.Profile()

    def __enter__(self):
        self.pr.enable()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pr.disable()
        self.print_stats()

    def print_stats(self, sortby='cumulative'):
        stream = io.StringIO()
        ps = pstats.Stats(self.pr, stream=stream).sort_stats(sortby).reverse_order()
        ps.print_stats()
        print(stream.getvalue())
        print(120 * '#')
