/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package firefoxperftesting;
import java.io.*;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.*;
import java.lang.InterruptedException;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxProfile;

import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Main  {
    public static void main(String[] args) {
        FirefoxProfile profile = new FirefoxProfile();

        File firebug = new File("/Users/shriamin/Development/firebug_ext/firebug-1.12.6.xpi");
        File netExport = new File("/Users/shriamin/Development/firebug_ext/netExport-0.9b4.xpi");

        try
        {
            profile.addExtension(firebug);
            profile.addExtension(netExport);
        }
        catch (IOException err)
        {
            System.out.println(err);
        }

        // Set default Firefox preferences
        profile.setPreference("app.update.enabled", false);

        String domain = "extensions.firebug.";

        // Set default Firebug preferences
        profile.setPreference(domain + "currentVersion", "1.12.6");
        profile.setPreference(domain + "allPagesActivation", "on");
        profile.setPreference(domain + "defaultPanelName", "net");
        profile.setPreference(domain + "net.enableSites", true);

        // Set default NetExport preferences
        profile.setPreference(domain + "netexport.alwaysEnableAutoExport", true);
        profile.setPreference(domain + "netexport.showPreview", false);
        profile.setPreference(domain + "netexport.defaultLogDir", "/Users/shriamin/Development");

        WebDriver driver = new FirefoxDriver(profile);

        try
        {
            // Wait till Firebug is loaded
            Thread.sleep(5000);

            // Load test page
            driver.get("http://www.google.com");

            // Wait till HAR is exported
            Thread.sleep(10000);
        }
        catch (InterruptedException err)
        {
            System.out.println(err);
        }

        driver.quit();
    }
}







/**
 *
 * @author shriamin
 */
//public class Main {

    /**
     * @param args the command line arguments
     */
/*
    public static void main(String[] args) {
        // TODO code application logic here
    }

}
*/