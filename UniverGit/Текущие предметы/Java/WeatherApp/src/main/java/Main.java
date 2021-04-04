import java.util.Scanner;

public class Main {

    public static void main (String args[]) throws Exception {

        Scanner scanner = new Scanner(System.in);
        Settings settings = new Settings();

        while (true) {

            if (settings.getService().equals("null")) {
                api_input(settings);
            }
            if (settings.getCity().equals("null")) {
                city_input(settings);
            }

            Messages.help_msg(settings);

            while (true) {

                String response = scanner.nextLine();

                if (response.equals("weather")) {
                    if (settings.getService().equals("ow")) {
                        OpenWeatherParser ow_parser = new OpenWeatherParser(settings.getCity());
                        ow_parser.print_weather();

                    } else if (settings.getService().equals("ws")) {
                        WeatherStackParser ws_parser = new WeatherStackParser(settings.getCity());
                        ws_parser.print_weather();
                    } else if (settings.getService().equals("wa")) {
                        WeatherAPIParser wa_parser = new WeatherAPIParser(settings.getCity());
                        wa_parser.print_weather();
                    }

                } else if (response.equals("change api")) {
                    api_input(settings);
                } else if (response.equals("change city")) {
                    city_input(settings);
                } else if (response.equals("change language")) {
                    language_input(settings);
                } else if (response.equals("help")) {
                    Messages.help_msg(settings);
                } else if (response.equals("drop")) {
                    settings.drop();
                    System.out.println("You successfully dropped your settings");
                    break;
                } else {
                    System.out.println("Wrong input");
                }
            }
        }
    }

    private static String api_input (Settings settings) {
        Messages.change_api_msg(settings);
        while (true) {
            Scanner scanner_api = new Scanner(System.in);
            String api = scanner_api.nextLine();
            if (api.equals("ow") | api.equals("ws") | api.equals("wa")){
                settings.setSetting("service", api);
                Messages.api_change_success_msg(settings);
                return api;
            } else {
                Messages.valid_change_msg(settings);
            }
        }
    }

    private static String city_input (Settings settings) {
        Messages.change_city_msg(settings);
        while (true) {
            Scanner scanner_city = new Scanner(System.in);
            String city = scanner_city.nextLine();
            boolean city_validation = false;
            if (settings.getService().equals("ow")) {
                city_validation = new OpenWeatherParser(city).is_parse_successful();
            } else if (settings.getService().equals("ws")) {
                city_validation = new WeatherStackParser(city).is_parse_successful();
            } else if (settings.getService().equals("wa")) {
                city_validation = new WeatherAPIParser(city).is_parse_successful();
            }
            if (city_validation) {
                settings.setSetting("city", city);
                Messages.city_change_success_msg(settings);
                return city;
            } else {
                Messages.valid_city_change_msg(settings);
            }
        }
    }

    private static String language_input (Settings settings) {
        Messages.change_language_msg(settings);
        while (true) {
            Scanner scanner_lang = new Scanner(System.in);
            String language = scanner_lang.nextLine();
            if (language.equals("en")){
                settings.setSetting("language", language);
                Messages.language_change_success_msg(settings);
                return language;
            } else {
                Messages.valid_change_msg(settings);
            }
        }
    }
}
