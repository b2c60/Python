import urllib

link = "https://developer.apple.com/library/ios/documentation/MultipeerConnectivity/Reference/MultipeerConnectivityFramework/"
f = urllib.request.urlopen(link)
myfile = f.read()
print(myfile)
