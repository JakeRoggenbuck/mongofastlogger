import fire
import main


LOGGER = main.Logger()
VIEWER = main.LogViewer()


class Serpent(object):
    def search(self, tag):
        VIEWER.search_logs_by_tag(tag)

    def clear(self):
        VIEWER.clear_data()

    def log(self, tag, message):
        LOGGER.log(tag, message)

    def view(self):
        VIEWER.view_log()

    def export(self, filename):
        VIEWER.export_log(filename)

    def last(self, metric, amount):
        VIEWER.check_by_time(metric, amount)


if __name__ == "__main__":
    fire.Fire(Serpent)
