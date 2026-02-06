import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ParcoursDeMiel {

    private static List<Point> points = new ArrayList<>();
    private static double[][] dist;
    private static int n = 0;

    private static final class Point {
        final double x;
        final double y;
        Point(double x, double y) { this.x = x; this.y = y; }
    }

    private static List<Point> readPoints(String filename) throws IOException {
        List<Point> result = new ArrayList<>();
        for (String line : Files.readAllLines(Paths.get(filename))) {
            String trimmed = line.trim();
            if (trimmed.isEmpty()) continue;
            String[] parts = trimmed.split(",");
            double x = Double.parseDouble(parts[0].trim());
            double y = Double.parseDouble(parts[1].trim());
            result.add(new Point(x, y));
        }
        return result;
    }

    private static double[][] distanceMatrix(List<Point> pts) {
        int size = pts.size();
        double[][] matrix = new double[size][size];
        for (int i = 0; i < size; i++) {
            Point a = pts.get(i);
            for (int j = 0; j < size; j++) {
                Point b = pts.get(j);
                matrix[i][j] = Math.hypot(b.x - a.x, b.y - a.y);
            }
        }
        return matrix;
    }

    private static void initialize(String filename) throws IOException {
        points = readPoints(filename);
        n = points.size();
        dist = distanceMatrix(points);
    }

    private static double calculateLength(List<Integer> parcours) {
        if (parcours == null) return -1.0;
        double totalDistance = 0.0;
        int numPoints = parcours.size();
        for (int i = 0; i < numPoints; i++) {
            int u = parcours.get(i);
            int v = parcours.get((i + 1) % numPoints);
            totalDistance += dist[u][v];
        }
        return totalDistance;
    }

    private static List<Integer> adviseHoneybee() {
        
        // *** recommandation : écrire votre code ici ***

        return null;
    }

    public static void main(String[] args) throws IOException {
        initialize("input_demo.txt");

        // parcours_exemple = [i for i in range(n)]
        List<Integer> parcoursExemple = IntStream.range(0, n).boxed().collect(Collectors.toList());
        double length = calculateLength(parcoursExemple);
        System.out.println(parcoursExemple);
        System.out.println(length);

        // For input_demo.txt, the best route is [1, 0, 6, 5, 3, 2, 4]
        // 27.699768073747965
        // parcours_exemple = [1, 0, 6, 5, 3, 2, 4]

        List<Integer> bestAnswer = adviseHoneybee();
        System.out.println(bestAnswer);
        System.out.println(calculateLength(bestAnswer));
    }
}
