//Hospital Spot Class
public class Bed extends Point {
    public Bed(int x, int y) {
        super(x, y);
    }
    //Whether bed is occupied
    private boolean isEmpty = true;

    public boolean isEmpty() {
        return isEmpty;
    }

    public void setEmpty(boolean empty) {
        isEmpty = empty;
    }
}
