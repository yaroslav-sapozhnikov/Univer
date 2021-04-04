import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Weather {

    protected String current_weather;
    protected long temperature;
    protected long feels_like;
    protected int wind_speed;
    protected boolean parse_successful;
    protected String name;
    protected String last_city;

    Weather(){}

    public void print_weather() {
        if (this.parse_successful == true) {
            System.out.println(" ");
            System.out.println("API: " + this.name);
            System.out.println("City: " + this.last_city);
            System.out.println(" ");
            System.out.println("Current weather: " + this.current_weather);
            System.out.println("Temperature: " + this.temperature + " C");
            System.out.println("Feels Like: " + this.feels_like + " C");
            System.out.println("Wind speed: " + this.wind_speed + " m/s");
        }
    }

    protected String get_content (String str_url){
        HttpURLConnection connection = null;
        StringBuilder sb = new StringBuilder();
        try {
            URL url = new URL(str_url);
            connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.connect();

            if(HttpURLConnection.HTTP_OK == connection.getResponseCode()) {
                BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                String line;

                while ((line = in.readLine()) != null) {
                    sb.append(line);
                }

                this.parse_successful = true;

            } else {
                System.out.println("Error: wrong city");
                this.parse_successful = false;
            }

        } catch (Exception e) {
            System.out.println("Error: no connection");
        } finally {
            if (connection != null) {
                connection.disconnect();
            }
        }

        return sb.toString();

    }

    public boolean is_parse_successful () { return parse_successful; }
}
