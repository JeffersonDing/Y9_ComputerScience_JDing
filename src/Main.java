import javax.swing.*;

import java.awt.*;
import java.util.List;
import java.util.Random;

public class Main {

    public static void main(String[] args) {
        initHospital();
        initPanel();
        initInfected();
    }
    private static void initPanel() {
        MyPanel p = new MyPanel();
        Thread panelThread = new Thread(p);
        JFrame frame = new JFrame();
        frame.add(p);
        frame.setSize(Constants.CITY_WIDTH + hospitalWidth + 400, Constants.CITY_HEIGHT);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        frame.setTitle("COVID Simulation");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panelThread.start();
    }

    private static int hospitalWidth;
    // Initialize Hospital
    private static void initHospital() {
        hospitalWidth = Hospital.getInstance().getWidth();
    }
    // Initialize Infected
    private static void initInfected() {
        List<Person> people = PersonPool.getInstance().getPersonList();//Get All Suspects
        for (int i = 0; i < Constants.ORIGINAL_COUNT; i++) {
            Person person;
            do {
                person = people.get(new Random().nextInt(people.size() - 1));//Choose Random Suspect
            } while (person.isInfected());//If Already Infected, Re-choose
            person.Infect();//Set Status to Infected
        }
    }

}
