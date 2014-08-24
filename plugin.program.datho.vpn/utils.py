#
# Copyright (C) 2014 Datho Digital Inc., All rights reserved
#
# Permission must be obtained from the copyright holder for any commercial use, distribution or modification of this software.
#



import xbmc


class Logger:

    LOG_DEBUG = xbmc.LOGDEBUG
    LOG_INFO = xbmc.LOGINFO
    LOG_WARNING = xbmc.LOGWARNING
    LOG_ERROR = xbmc.LOGERROR
    LOG_FATAL = xbmc.LOGFATAL

    @classmethod
    def log(cls, msg, level = LOG_INFO, prefix = "Datho VPN"):

        return xbmc.log("%s %s" % (prefix, msg), level)