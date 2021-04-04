import org.json.JSONObject;

public class WeatherAPIParser extends Weather {

    WeatherAPIParser(String city){
        this.name = "Weather API";
        parse(city);
    }

    public void parse (String city) {
        String url = "http://api.weatherapi.com/v1/current.json?key=1eeb20af5e1c486999c135756201412&q=" + city;
        String content = get_content(url);
        try {
            JSONObject json = new JSONObject(content);
            this.last_city = city;
            this.current_weather = json.getJSONObject("current").getJSONObject("condition").getString("text");
            this.feels_like = json.getJSONObject("current").getInt("feelslike_c");
            this.temperature = json.getJSONObject("current").getInt("temp_c");
            this.wind_speed = json.getJSONObject("current").getInt("wind_kph");
            this.parse_successful = true;
        } catch (Exception e) {
            this.parse_successful = false;
        }
    }
}
