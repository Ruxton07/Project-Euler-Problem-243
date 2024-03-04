import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.HashMap;
import java.util.Scanner;
class BigIntegerProbablePrimeVerification {
    public static void main(String[] args) throws FileNotFoundException {
        System.out.println("hi");
        BigInteger thresholdBI = new BigInteger("1000000");
        boolean loop = true;
        HashMap<BigInteger, Boolean> sixmilprimes = new HashMap<BigInteger, Boolean>();
            Scanner scan = new Scanner(new File("C:/Users/rtkel/Documents/WindowsPowerShell/newcomplete.txt"));
            while (scan.hasNextLine()) {
                BigInteger cLine = new BigInteger(String.format("%d", scan.nextInt()));
                scan.nextLine();
                sixmilprimes.put(cLine, true);
            }
            scan.close();
        for (BigInteger i = new BigInteger("3"); i.compareTo(thresholdBI)==-1 && loop; i=i.add(new BigInteger("1"))) {
            //System.out.println("i: " + i.toString());
            boolean actualPrime = (sixmilprimes.get(i) != null) ? sixmilprimes.get(i) : false;
            // for (BigInteger j = new BigInteger("2"); j.compareTo(i.sqrt().add(new BigInteger("2")))==-1; j=j.add(new BigInteger("1"))) {
            //     System.out.println("j: " + j.toString());
            //     if (i.mod(j).compareTo(new BigInteger("0"))==0) {
            //         actualPrime = false;
            //     }
            // } //Manually calculating primes, using a file for a list instead
            boolean probPrime = i.isProbablePrime(8);
            if (probPrime != actualPrime) {
                System.out.println("Mismatch: (probPrime: " + probPrime + "), (actualPrime: " + actualPrime + "), (BigInteger: " + i.toString() + ")");
                loop = false;
                break;
            }
        }
        System.out.println("YAY THEY ALL WORK");
    }
}