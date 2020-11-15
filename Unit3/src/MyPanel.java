import javax.swing.*;
import java.awt.*;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

/**
 Main Panel
 */
public class MyPanel extends JPanel implements Runnable {


    public MyPanel() {
        super();
        this.setBackground(new Color(0x444444));
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        g.setColor(new Color(0x00ff00));//Set Hospital Border
        //Draw Hospital
        g.drawRect(Hospital.getInstance().getX(), Hospital.getInstance().getY(),
                Hospital.getInstance().getWidth(), Hospital.getInstance().getHeight());
        g.setFont(new Font("arial", Font.BOLD, 16));
        g.setColor(new Color(0x00ff00));
        g.drawString("Hospital", Hospital.getInstance().getX() + Hospital.getInstance().getWidth() / 4, Hospital.getInstance().getY() - 16);
        //Draw particles to represent suspects
        List<Person> people = PersonPool.getInstance().getPersonList();
        if (people == null) {
            return;
        }
        for (Person person : people) {
            switch (person.getState()) {
                case Person.State.NORMAL: {
                    //healthy
                    g.setColor(new Color(0xdddddd));
                    break;
                }
                case Person.State.INCUBATION: {
                    //Incubation
                    g.setColor(new Color(0xffee00));
                    break;
                }

                case Person.State.CONFIRMED: {
                    //Infected
                    g.setColor(new Color(0xff0000));
                    break;
                }
                case Person.State.ISOLATED: {
                    //Isolated
                    g.setColor(new Color(0x48FFFC));
                    break;
                }
                case Person.State.DEATH: {
                    //Death

                    g.setColor(new Color(0x000000));
                    break;
                }
            }
            person.update();//Update Status
            g.fillOval(person.getX(), person.getY(), 3, 3);

        }

        int captionStartOffsetX = 700 + Hospital.getInstance().getWidth() + 40;
        int captionStartOffsetY = 40;
        int captionSize = 24;

        //Display Data
        g.setColor(Color.WHITE);
        g.drawString("Total Suspects:" + Constants.TOTAL_SUSPECTS, captionStartOffsetX, captionStartOffsetY);
        g.setColor(new Color(0xdddddd));
        g.drawString("Healthy:" + PersonPool.getInstance().getPeopleSize(Person.State.NORMAL), captionStartOffsetX, captionStartOffsetY + captionSize);
        g.setColor(new Color(0xffee00));
        g.drawString("Incubation:" + PersonPool.getInstance().getPeopleSize(Person.State.INCUBATION), captionStartOffsetX, captionStartOffsetY + 2 * captionSize);
        g.setColor(new Color(0xff0000));
        g.drawString("Infected:" + PersonPool.getInstance().getPeopleSize(Person.State.CONFIRMED), captionStartOffsetX, captionStartOffsetY + 3 * captionSize);
        g.setColor(new Color(0x48FFFC));
        g.drawString("Isolated:" + PersonPool.getInstance().getPeopleSize(Person.State.ISOLATED), captionStartOffsetX, captionStartOffsetY + 4 * captionSize);
        g.setColor(new Color(0x00ff00));
        g.drawString("Remaining Hospital Spots:" + Math.max(Constants.BED_COUNT - PersonPool.getInstance().getPeopleSize(Person.State.ISOLATED), 0), captionStartOffsetX, captionStartOffsetY + 5 * captionSize);
        g.setColor(new Color(0xE39476));
        //Emergency Hospital Spots => NEED = Infected - Isolated
        //
        int needBeds = PersonPool.getInstance().getPeopleSize(Person.State.CONFIRMED)
                - PersonPool.getInstance().getPeopleSize(Person.State.ISOLATED);

        g.drawString("Emergency:" + (needBeds > 0 ? needBeds : 0), captionStartOffsetX, captionStartOffsetY + 6 * captionSize);
        g.setColor(new Color(0xccbbcc));
        g.drawString("Death:" + PersonPool.getInstance().getPeopleSize(Person.State.DEATH), captionStartOffsetX, captionStartOffsetY + 7 * captionSize);
        g.setColor(new Color(0xffffff));
        g.drawString("World Time(Day):" + (int) (worldTime / 10.0), captionStartOffsetX, captionStartOffsetY + 8 * captionSize);

    }


    public static int worldTime = 0;//Init World Time

    public Timer timer = new Timer();

    class MyTimerTask extends TimerTask {
        @Override
        public void run() {
            MyPanel.this.repaint();
            worldTime++;
        }
    }

    @Override
    public void run() {
        timer.schedule(new MyTimerTask(), 0, 100);//Start World Time


    }
}
