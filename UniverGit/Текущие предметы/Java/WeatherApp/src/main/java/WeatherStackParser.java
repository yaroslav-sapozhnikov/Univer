import org.json.JSONObject;

public class WeatherStackParser extends Weather {

    WeatherStackParser(String city){
        this.name = "WeatherStack API";
        parse(city);
    }

    public void parse (String city) {
        String url = "http://api.weatherstack.com/current?access_key=226bda107fd0f1e66819c1741de8064d&query=" + city;
        String content = get_content(url);
        try {
            JSONObject json = new JSONObject(content);
            this.last_city = city;
            this.current_weather = json.getJSONObject("current").getJSONArray("weather_descriptions").getString(0);
            this.feels_like = json.getJSONObject("current").getInt("feelslike");
            this.temperature = json.getJSONObject("current").getInt("temperature");
            this.wind_speed = json.getJSONObject("current").getInt("wind_speed");
            this.parse_successful = true;
        } catch (Exception e) {
            this.parse_successful = false;
        }
    }
}
