from main import Logger, LogViewer


logger = Logger()
logger.log("Something", "This is bad as well i guess but i dont actually know")

viewer = LogViewer()
viewer.view_log()

viewer.search_logs_by_tag("Something")
viewer.check_by_time("days", 3)
viewer.export_log("example.log")
