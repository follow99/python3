__author__ = 'd15123547'

from math import pi,acos,sin,cos


def getDistanceBetweenAirports(airportCode1,airportCode2):


    airportlist={'DUB':(53.42133,-6.270075),
                 'LHR':(51.4775,-0.461389),
                 'JFK':(40.639751,-73.778925),
                 'AAL':(57.092789, 9.849164),
                 'CDG':(49.012779,2.55),
                 'SYD':(-33.946111,151.177222)
                 }
    if airportCode1 or airportCode2 not in airportlist:
        return print('The city not on our database list lol!! ')
    LatitudeA = airportlist[airportCode1][0]
    LongitudeA = airportlist[airportCode1][1]
    LatitudeB = airportlist[airportCode2][0]
    LongitudeB = airportlist[airportCode2][1]
    LatA = (90-LatitudeA)*2*pi/360
    LonA = LongitudeA*2*pi/360
    LatB = (90-LatitudeB)*2*pi/360
    LonB = LongitudeB*2*pi/360
    distance=acos(sin(LatA)*sin(LatB)*cos(LonA-LonB)+cos(LatA)*cos(LatB))*6371
    return print('The distance between',airportCode1,'and',airportCode2,'is','{:.2f}'.format(distance),'Km')
def main():
    a1=input('FROM:(AIRPORT 3 letter code):').upper()
    a2=input('TO:  (AIRPORT 3 letter code):').upper()
    getDistanceBetweenAirports(a1,a2)
main()