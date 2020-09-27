from inspect import currentframe, getframeinfo
from pymongo import MongoClient
from datetime import datetime
from termcolor import colored
import arrow


class Database:
    def __init__(self, location: str = "localhost", port: int = 27017):
        """Set default location and port"""
        self.location = location
        self.port = port
        self.connect()

    def connect(self):
        """Nake client, database, and collection"""
        self.client = MongoClient(self.location, self.port)
        self.database = self.client.logging_test_db
        self.collection = self.database.collection


class Logger:
    def __init__(self):
        """Setup database"""
        self.db = Database()

    def time(self):
        """Get data and time"""
        return datetime.utcnow()

    def log(self, tag: str, message: str):
        """Add item to log"""
        cf = currentframe()
        linenum = cf.f_back.f_lineno
        filename = getframeinfo(cf.f_back).filename
        # Make document with time, tag, and message
        document = {
            "tag": tag,
            "time": self.time(),
            "message": message,
            "line": linenum,
            "file": filename
        }
        # Insert doc into collection
        self.db.collection.insert_one(document)

    def view_log_line(self, document):
        """Make log view"""
        filename = document["file"]
        linenum = document["line"]
        # Get tag and make yellow
        tag = colored(document["tag"], "yellow")
        # Get message from document
        message = document["message"]
        # Get time and convert it to arrow
        time = arrow.get(document['time'])
        # Get time in full format
        full = time.format('HH:mm:ss MM-DD-YY')
        # Get short human readable time
        short = colored(time.humanize(), "green")
        # Return string in readable format
        location = colored(f"{filename}::{linenum}", 'blue')
        return f"{tag}\t{full} {location} {short} {message}"

    def export_log(self, filename):
        """Export log to file"""
        with open(filename, 'w') as file:
            for x in self.db.collection.find({}):
                file.write(self.view_log_line(x) + "\n")

    def view_log(self):
        """View each log item"""
        for x in self.db.collection.find({}):
            print(self.view_log_line(x))
