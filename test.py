from main import Logger, LogViewer


# Make logger
logger = Logger()
# Log message with tag of "Something"
logger.log("Something", "This is bad as well i guess but i dont actually know")
# Log message with tag of "Something" and display log in console
logger.log("Something", "This is a message", display=True)

# Make Viewer
viewer = LogViewer()
# Print all logs
viewer.view_log()

# Search logs that have the tag "Something"
viewer.search_logs_by_tag("Something")
# Search logs in the last 3 days
viewer.check_by_time("days", 3)
# Export logs to example.log
viewer.export_log("example.log")
