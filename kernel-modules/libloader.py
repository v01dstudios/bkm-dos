#libloader by ichbinmusti
#bkm-dos prompt libloader

class bkm:
    class examplemusic:
        musictype = 'example'
        musicauthor = 'ichbinmusti'
        musicname = 'examplemusic'
    class exampleapp:
        appname = 'examplename'
        appauthor = 'ichbinmusti'
        appdesc = 'example desc.'
        appId = '3X4MPL3-example'
    class exampleotherlib:
        other = 'b3RoZXJhcHAvYmttYXBwcyAtIExJQkxPQURFUipJQ0hCSU5NVVNUSQ=='
        licensetype = other

musicfile = bkm.examplemusic
appfile = bkm.exampleapp
otherfile = bkm.exampleotherlib
otherlicense = otherfile.licensetype
print(otherlicense)
print('_' *70)
print(musicfile.musicname)
print('_' *70)
print(appfile.appname, appfile.appId)
print('_' *70)
print('libloader bkmdos kullandığın için teşekkürler.')