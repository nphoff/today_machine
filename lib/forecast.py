from bs4 import BeautifulSoup
import requests

class Forecast:
    def getExtendedForecastHtml(self) -> str:
        return requests.get(
            "https://weather.gc.ca/forecast/public_bulletins_e.html?Bulletin=fpcn50.cwvr"
        ).text

    def getExtendedForecast(self):
        text = self.getExtendedForecastHtml()
        soup = BeautifulSoup(text, 'html.parser')
        pre = soup.find('pre').get_text()
        return pre

    def filterExtendedForecast(self, forecast: str):
        cities_i_care_about = ['Metro Vancouver', 'Whistler']
        end_character = '\n\n'
        parts = []
        for city in cities_i_care_about:
            start = forecast.find(city)
            end = forecast.find(end_character, start)
            parts.append(forecast[start:end])
        return parts



def main():
    forecast = Forecast()
    print(forecast.filterExtendedForecast(forecast.getExtendedForecast()))

if __name__ == '__main__':
    main()
