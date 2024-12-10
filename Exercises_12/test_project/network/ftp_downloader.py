
"""
ftp_downloader.py  : ftp downloader
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"
import ftplib
import settings.ftp as settings

# Make the connection
ftp = ftplib.FTP(settings.FTP_ubuntu['URL'])
# Anonymous login
ftp.login() 
# Change to the correct directory
ftp.cwd(settings.FTP_ubuntu["PATH"])
# Retrieve the file
ftp.retrbinary("RETR " + settings.FTP_ubuntu["FILENAME"], open(settings.FTP_ubuntu["FILENAME"], 'wb').write)
ftp.quit()
