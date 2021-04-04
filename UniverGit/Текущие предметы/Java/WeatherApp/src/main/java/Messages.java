public class Messages {

    public static void help_msg (Settings settings) {
        if (settings.getLanguage().equals("en")) {
            System.out.println(" ");
            System.out.println("Current API: " + getServiceName(settings.getService()));
            System.out.println("Current city: " + settings.getCity());
            System.out.println(" ");
            System.out.println("Enter \"change language\" to change language");
            System.out.println("Enter \"change api\" to change API");
            System.out.println("Enter \"change city\" to change city");
            System.out.println("Enter \"weather\" to get current weather");
            System.out.println("Enter \"drop\" to drop settings");
            System.out.println("Enter \"help\" to show this message again");
        }
    }

    public static void change_api_msg (Settings settings) {
        if (settings.getLanguage().equals("en")) {
            System.out.println(" ");
            System.out.println("Choose API:");
            System.out.println(" ");
            System.out.println("- OpenWeather API = \"ow\"");
            System.out.println("- WeatherStack API = \"ws\"");
            System.out.println("- Weather API = \"wa\"");
            System.out.println(" ");
            System.out.println("Enter required API: ");
        }
    }

    public static void change_city_msg (Settings settings) {
        if (settings.getLanguage().equals("en")) {
            System.out.println(" ");
            System.out.println("Enter required city in english: ");
        }
    }

    public static void change_language_msg (Settings settings) {
        if (settings.getLanguage().equals("en")) {
            System.out.println(" ");
            System.out.println("Supported languages: ");
            System.out.println(" ");
            System.out.println("English = \"en\"");
            System.out.println(" ");
            System.out.println("Enter required Language: ");
        }
    }

    public static void valid_change_msg (Settings settings) {
        System.out.println(" ");
        if (settings.getLanguage().equals("en")) {
            System.out.println("Please, enter valid value from list: ");
        }
    }

    public static void valid_city_change_msg (Settings settings) {
        System.out.println(" ");
        if (settings.getLanguage().equals("en")) {
            System.out.println("Please, enter valid city name: ");
        }
    }

    public static void city_change_success_msg (Settings settings) {
        System.out.println(" ");
        if (settings.getLanguage().equals("en")) {
            System.out.println("You successfully changed the city for: " + settings.getCity());
        }
    }

    public static void api_change_success_msg (Settings settings) {
        System.out.println(" ");
        if (settings.getLanguage().equals("en")) {
            System.out.println("You successfully changed API for: " + getServiceName(settings.getService()));
        }
    }

    public static void language_change_success_msg (Settings settings) {
        System.out.println(" ");
        if (settings.getLanguage().equals("en")) {
            System.out.println("You successfully changed the language for: " + settings.getLanguage());
        }
    }

    private static String getServiceName (String service) {
        String name = null;
        if (service.equals("ws")) { name = "WeatherStack API"; }
        if (service.equals("ow")) { name = "OpenWeather API"; }
        if (service.equals("wa")) { name = "Weather API"; }
        return name;
    }
}
