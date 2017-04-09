class Singleton(object):
  _instances = {}
  def __new__(class_, *args, **kwargs):
    if class_ not in class_._instances:
        class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
    return class_._instances[class_]

class PersistentData(Singleton):
    pass

    ISOFile = ""
    ISODownloadImg = ""
    SSID = ""
    Settings = {}
    DiskSD = ""

    def setISOFile(self, f):
        PersistentData.ISOFile = f

    def getISOFile(self):
        return PersistentData.ISOFile

    def setISODownloadImg(self, iso):
        PersistentData.ISODownloadImg = iso

    def getISODownloadImg(self):
        return PersistentData.ISODownloadImg

    def setSSID(self, ssid):
        PersistentData.SSID = ssid

    def getSSID(self):
        return PersistentData.SSID

    def setSettings(self, settings):
        PersistentData.Settings = settings

    def getSettings(self):
        return PersistentData.Settings
    def setDiskSD(self, disk):
        PersistentData.DiskSD = disk

    def getDiskSD(self):
        return PersistentData.DiskSD
