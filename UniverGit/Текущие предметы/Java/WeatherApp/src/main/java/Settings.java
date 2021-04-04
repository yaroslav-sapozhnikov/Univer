import org.json.JSONObject;
import java.io.FileWriter;
import java.util.Scanner;
import java.io.FileReader;

public class Settings {

    private String service;
    private String language;
    private String city;

    Settings() throws Exception {
        this.service = getJSON().getString("service");
        this.language = getJSON().getString("language");
        this.city = getJSON().getString("city");
    }

    public void setSetting(String setting, String value) {
        if (setting.equals("service")) {
            this.service = value;
        } else if (setting.equals("city")) {
            this.city = value;
        } else if (setting.equals("language")) {
            this.language = value;
        }
        try{
            JSONObject settings = getJSON();
            settings.put(setting, value);
            FileWriter fw = new FileWriter("src/main/java/settings.json");
            fw.write(settings.toString());
            fw.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public void drop() {
        setSetting("city", "null");
        setSetting("service", "null");
        setSetting("language", "en");
    }

    private JSONObject getJSON() throws Exception {
        FileReader fr = new FileReader("src/main/java/settings.json");
        Scanner scanner = new Scanner(fr);
        JSONObject settings = new JSONObject(scanner.nextLine());
        fr.close(); scanner.close();
        return settings;
        }

    public String getService() {
        return this.service;
    }

    public String getLanguage() { return this.language; }

    public String getCity() { return this.city; }
}

