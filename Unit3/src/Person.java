import java.util.List;
import java.util.Random;

public class Person extends Point {
    private City city;

    private MoveTarget moveTarget;
    double targetXU;
    double targetYU;
    double targetSig = 50;

    public interface State {
        int NORMAL = 0;
        int SUSPECTED = NORMAL + 1;
        int INCUBATION = SUSPECTED + 1;
        int CONFIRMED = INCUBATION + 1;
        int ISOLATED = CONFIRMED + 1;

        //Cured will be turned to NORMAL
        int DEATH = ISOLATED + 1;
    }

    public Person(City city, int x, int y) {
        super(x, y);
        this.city = city;
        //Suspects @ N(x,100) Normal Distribution
        targetXU = MathUtil.stdGaussian(100, x);
        targetYU = MathUtil.stdGaussian(100, y);

    }

    private int state = State.NORMAL;

    public int getState() {
        return state;
    }

    public void setState(int state) {
        this.state = state;
    }

    int infectedTime = 0;//Infected Instance
    int confirmedTime = 0;//Confirmed Instance
    int dieMoment = 0;//Death Time 0=>Uncertain 1=>Dead -1=>Immune


    public boolean isInfected() {
        return state >= State.INCUBATION;
    }

    public void Infect() {
        state = State.INCUBATION;
        infectedTime = MyPanel.worldTime;
    }

    public double distance(Person person) {
        return Math.sqrt(Math.pow(getX() - person.getX(), 2) + Math.pow(getY() - person.getY(), 2));
    }
    private void action() {

        if (state == State.ISOLATED || state == State.DEATH) {
            return;//If isolated or Dead, could not move
        }
        if (moveTarget == null || moveTarget.isArrived()) {
            double targetX = MathUtil.stdGaussian(targetSig, targetXU);
            double targetY = MathUtil.stdGaussian(targetSig, targetYU);
            moveTarget = new MoveTarget((int) targetX, (int) targetY);

        }

        //Calculate Movement
        int dX = moveTarget.getX() - getX();
        int dY = moveTarget.getY() - getY();

        double length = Math.sqrt(Math.pow(dX, 2) + Math.pow(dY, 2));//Get distance

        if (length < 1) {
            //check whether arrived
            moveTarget.setArrived(true);
            return;
        }

        int udX = (int) (dX / length);//X axis dx movement
        if (udX == 0 && dX != 0) {
            if (dX > 0) {
                udX = 1;
            } else {
                udX = -1;
            }
        }


        int udY = (int) (dY / length);
        if (udY == 0 && dY != 0) {
            if (dY > 0) {
                udY = 1;
            } else {
                udY = -1;
            }
        }

        //Horizontal Border
        if (getX() > Constants.CITY_WIDTH || getX() < 0) {
            moveTarget = null;
            if (udX > 0) {
                udX = -udX;
            }
        }
        //Vertical Border
        if (getY() > Constants.CITY_HEIGHT || getY() < 0) {
            moveTarget = null;
            if (udY > 0) {
                udY = -udY;
            }
        }
        moveTo(udX, udY);

    }

    public Bed useBed;

    public void update() {

        if (state == State.ISOLATED || state == State.DEATH) {
            return;//If Dead or Isolated
        }

        //Update Infected
        if (state == State.CONFIRMED && dieMoment == 0) {

            int result = new Random().nextInt(10000) + 1;//Lucky "Number"
            if (1 <= result && result <= (int) (Constants.FATALITY_RATE * 10000)) {


                dieMoment = confirmedTime + (int) Constants.DEATH_TIME;//Determine Death Moment
            } else {
                dieMoment = -1;//Got lucky
            }
        }

        if (state == State.CONFIRMED
                && MyPanel.worldTime - confirmedTime >= Constants.HOSPITAL_RESPONSE_TIME) {
            //If Infected && (WorldTime-ConfirmedTime)>Hospital Response time
            Bed bed = Hospital.getInstance().pickBed();//Find Bed
            if (bed == null) {


            } else {
                //Place Suspect
                useBed = bed;
                state = State.ISOLATED;
                setX(bed.getX());
                setY(bed.getY());
                bed.setEmpty(false);
            }
        }

        //Update Death
        if ((state == State.CONFIRMED || state == State.ISOLATED) && MyPanel.worldTime >= dieMoment && dieMoment > 0) {
            state = State.DEATH;//Infected => Death
            Hospital.getInstance().returnBed(useBed);//Empty out a bed
        }
        double stdRnIncubationTime = MathUtil.stdGaussian(25, Constants.INCUBATION_TIME / 2);//Random Incubation time
        //Update Incubation Period Suspects
        if (MyPanel.worldTime - infectedTime > stdRnIncubationTime && state == State.INCUBATION) {
            state = State.CONFIRMED;//Incubation => Confirmed
            confirmedTime = MyPanel.worldTime;//Refresh World Time
        }
        action();
        List<Person> people = PersonPool.getInstance().personList;
        if (state >= State.INCUBATION) {
            return;
        }
        //Use Lucky Choice and Distance to Determine Whether Infect
        for (Person person : people) {
            if (person.getState() == State.NORMAL) {
                continue;
            }
            float random = new Random().nextFloat();
            if (random < Constants.RATE && distance(person) < Constants.SAFE_DIST) {
                this.Infect();
                break;
            }
        }
    }
}
