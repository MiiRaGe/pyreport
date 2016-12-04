from datetime import datetime

DEBUG = 'debug'
CRITICAL = 'critical'
WARNING = 'warning'
INFO = 'info'
ERROR = 'debug'
EXCEPTION = 'exception'


class Report(object):
    entries = []

    def create_report(self):
        self.entries = []

    def finalize_report(self):
        html_page = ''
        for entry in self.entries:
            html_page += entry.render_as_html()
        self.entries = []
        return html_page

    def debug(self, msg, *args, **kwargs):
        """
        Add entry 'msg % args' with severity 'DEBUG' to the report.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        report.debug("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        self.add_report_entry(DEBUG, msg, args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """
        Add entry 'msg % args' with severity 'INFO' to the report.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        report.info("Houston, we have a %s", "interesting problem", exc_info=1)
        """
        self.add_report_entry(INFO, msg, args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """
        Add entry 'msg % args' with severity 'WARNING' to the report.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        report.warning("Houston, we have a %s", "bit of a problem", exc_info=1)
        """
        self.add_report_entry(WARNING, msg, args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        Add entry 'msg % args' with severity 'ERROR' to the report.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        report.error("Houston, we have a %s", "major problem", exc_info=1)
        """
        self.add_report_entry(ERROR, msg, args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        """
        Convenience method for reporting an ERROR with exception information.
        """
        self.add_report_entry(EXCEPTION, msg, args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """
        Add entry 'msg % args' with severity 'CRITICAL' to the report.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        report.critical("Houston, we have a %s", "major disaster", exc_info=1)
        """
        self.add_report_entry(CRITICAL, msg, *args, **kwargs)

    def add_report_entry(self, level, msg, *args, **kwargs):
        """
        Low-level reporting routine which creates a LogRecord and then calls
        all the handlers of this report to handle the record.
        """
        # exc_info=None, extra=None
        self.entries.append(Entry(level, msg, *args, **kwargs))


class Entry(object):
    level = None
    msg = None
    args = None
    kwargs = None

    def __init__(self, level, msg, *args, **kwargs):
        self.level = level
        self.msg = msg
        self.args = args
        self.kwargs = kwargs
        self.date = datetime.now()

    def render_as_html(self):
        return u'<p class="%s"><span class="time">%s:%s:%s.%s</span> - %s</p>' % (
            self.level, self.date.hour, self.date.minute, self.date.second, self.date.microsecond,
            self.msg)
