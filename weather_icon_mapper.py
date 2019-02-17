# weather_icon_mapper.py
#
# Maps weather icon IDs from OpenWeatherMap to weather icons from https://github.com/erikflowers/weather-icons

from datetime import datetime

class WeatherIconMapper:
    def __init__(self):
        pass

    @staticmethod
    def convertIcon(iconId, sunrise, sunset):
        """ Converts an OpenWeatherMap icon ID to a weather icon file name.
            Returns a tuple of the form: (icon-filename, description). """

        iconFileName, description = WeatherIconMapper._iconIdToBaseFileName(iconId)

        # IDs in 7xx and 9xx do not have a day-/night- prefix
        if iconId not in range(700, 799) and iconId not in range(900, 999):
            prefix = "day" if WeatherIconMapper.isDaytime(sunrise, sunset) else "night"
            iconFileName = "{}-{}".format(prefix, iconFileName)

        iconFileName = "wi-{}.png".format(iconFileName)

        return iconFileName, description

    @staticmethod
    def isDaytime(sunrise, sunset):
        currentTime = datetime.now().time()
        if sunrise <= currentTime <= sunset:
            return True
        else:
            return False

    @staticmethod
    def _iconIdToBaseFileName(iconId):
        """ Convert icon ID to a base file name.
            Returns a tuple of the form: (base-filename, label). """

        label = ""
        icon = ""
        if iconId == 200:
            label = "thunderstorm with light rain"
            icon = "storm-showers"

        elif iconId == 201:
            label = "thunderstorm with rain"
            icon = "storm-showers"

        elif iconId == 202:
            label = "thunderstorm with heavy rain"
            icon = "storm-showers"

        elif iconId == 210:
            label = "light thunderstorm"
            icon = "storm-showers"

        elif iconId == 211:
            label = "thunderstorm"
            icon = "thunderstorm"

        elif iconId == 212:
            label = "heavy thunderstorm"
            icon = "thunderstorm"

        elif iconId == 221:
            label = "ragged thunderstorm"
            icon = "thunderstorm"

        elif iconId == 230:
            label = "thunderstorm with light drizzle"
            icon = "storm-showers"

        elif iconId == 231:
            label = "thunderstorm with drizzle"
            icon = "storm-showers"

        elif iconId == 232:
            label = "thunderstorm with heavy drizzle"
            icon = "storm-showers"

        elif iconId == 300:
            label = "light intensity drizzle"
            icon = "sprinkle"

        elif iconId == 301:
            label = "drizzle"
            icon = "sprinkle"

        elif iconId == 302:
            label = "heavy intensity drizzle"
            icon = "sprinkle"

        elif iconId == 310:
            label = "light intensity drizzle rain"
            icon = "sprinkle"

        elif iconId == 311:
            label = "drizzle rain"
            icon = "sprinkle"

        elif iconId == 312:
            label = "heavy intensity drizzle rain"
            icon = "sprinkle"

        elif iconId == 313:
            label = "shower rain and drizzle"
            icon = "sprinkle"

        elif iconId == 314:
            label = "heavy shower rain and drizzle"
            icon = "sprinkle"

        elif iconId == 321:
            label = "shower drizzle"
            icon = "sprinkle"

        elif iconId == 500:
            label = "light rain"
            icon = "rain"

        elif iconId == 501:
            label = "moderate rain"
            icon = "rain"

        elif iconId == 502:
            label = "heavy intensity rain"
            icon = "rain"

        elif iconId == 503:
            label = "very heavy rain"
            icon = "rain"

        elif iconId == 504:
            label = "extreme rain"
            icon = "rain"

        elif iconId == 511:
            label = "freezing rain"
            icon = "rain-mix"

        elif iconId == 520:
            label = "light intensity shower rain"
            icon = "showers"

        elif iconId == 521:
            label = "shower rain"
            icon = "showers"

        elif iconId == 522:
            label = "heavy intensity shower rain"
            icon = "showers"

        elif iconId == 531:
            label = "ragged shower rain"
            icon = "showers"

        elif iconId == 600:
            label = "light snow"
            icon = "snow"

        elif iconId == 601:
            label = "snow"
            icon = "snow"

        elif iconId == 602:
            label = "heavy snow"
            icon = "snow"

        elif iconId == 611:
            label = "sleet"
            icon = "sleet"

        elif iconId == 612:
            label = "shower sleet"
            icon = "sleet"

        elif iconId == 615:
            label = "light rain and snow"
            icon = "rain-mix"

        elif iconId == 616:
            label = "rain and snow"
            icon = "rain-mix"

        elif iconId == 620:
            label = "light shower snow"
            icon = "rain-mix"

        elif iconId == 621:
            label = "shower snow"
            icon = "rain-mix"

        elif iconId == 622:
            label = "heavy shower snow"
            icon = "rain-mix"

        elif iconId == 701:
            label = "mist"
            icon = "sprinkle"

        elif iconId == 711:
            label = "smoke"
            icon = "smoke"

        elif iconId == 721:
            label = "haze"
            icon = "day-haze"

        elif iconId == 731:
            label = "sand dust whirls"
            icon = "cloudy-gusts"

        elif iconId == 741:
            label = "fog"
            icon = "fog"

        elif iconId == 751:
            label = "sand"
            icon = "cloudy-gusts"

        elif iconId == 761:
            label = "dust"
            icon = "dust"

        elif iconId == 762:
            label = "volcanic ash"
            icon = "smog"

        elif iconId == 771:
            label = "squalls"
            icon = "day-windy"

        elif iconId == 781:
            label = "tornado"
            icon = "tornado"

        elif iconId == 800:
            label = "clear sky"
            icon = "sunny"

        elif iconId == 801:
            label = "few clouds"
            icon = "cloudy"

        elif iconId == 802:
            label = "scattered clouds"
            icon = "cloudy"

        elif iconId == 803:
            label = "broken clouds"
            icon = "cloudy"

        elif iconId == 804:
            label = "overcast clouds"
            icon = "cloudy"

        elif iconId == 900:
            label = "tornado"
            icon = "tornado"

        elif iconId == 901:
            label = "tropical storm"
            icon = "hurricane"

        elif iconId == 902:
            label = "hurricane"
            icon = "hurricane"

        elif iconId == 903:
            label = "cold"
            icon = "snowflake-cold"

        elif iconId == 904:
            label = "hot"
            icon = "hot"

        elif iconId == 905:
            label = "windy"
            icon = "windy"

        elif iconId == 906:
            label = "hail"
            icon = "hail"

        elif iconId == 951:
            label = "calm"
            icon = "sunny"

        elif iconId == 952:
            label = "light breeze"
            icon = "cloudy-gusts"

        elif iconId == 953:
            label = "gentle breeze"
            icon = "cloudy-gusts"

        elif iconId == 954:
            label = "moderate breeze"
            icon = "cloudy-gusts"

        elif iconId == 955:
            label = "fresh breeze"
            icon = "cloudy-gusts"

        elif iconId == 956:
            label = "strong breeze"
            icon = "cloudy-gusts"

        elif iconId == 957:
            label = "high wind near gale"
            icon = "cloudy-gusts"

        elif iconId == 958:
            label = "gale"
            icon = "cloudy-gusts"

        elif iconId == 959:
            label = "severe gale"
            icon = "cloudy-gusts"

        elif iconId == 960:
            label = "storm"
            icon = "thunderstorm"

        elif iconId == 961:
            label = "violent storm"
            icon = "thunderstorm"

        elif iconId == 962:
            label = "hurricane"
            icon = "cloudy-gusts"

        return (icon, label)
