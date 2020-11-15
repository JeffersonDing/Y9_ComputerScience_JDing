import java.util.Random;

public class MathUtil {

    private static final Random randomGen = new Random();


     // StdX = (X-u)/sigma
     // X = sigma * StdX + u


    public static double stdGaussian(double sigma, double u) {
        double X = randomGen.nextGaussian();
        return sigma * X + u;
    }

}
